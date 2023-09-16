import ast
import contextlib
from _ast import comprehension
from typing import Any, TypedDict


class RenderContextDict(TypedDict):
    expand: bool


def get_render_context(node: ast.AST) -> RenderContextDict:
    if hasattr(node, 'render_context'):
        assert isinstance(node.render_context, dict)

        return {
            'expand': False,
            **node.render_context
        }

    else:
        return {
            'expand': False
        }


# noinspection PyTypeChecker
class SourceCodeGenerator(ast.NodeVisitor):
    def __init__(self):
        self.source = ''
        self.indent_length = 0
        self.hierarchy = []

    @property
    def indent(self):
        return ' ' * self.indent_length

    @contextlib.contextmanager
    def _indent_context(self):
        self.indent_length += 4
        yield
        self.indent_length -= 4

    def _zip_args_and_defaults(self, node: ast.arguments):
        defaults = getattr(node, 'defaults', [])
        args = getattr(node, 'args', [])

        while len(defaults) < len(args):
            defaults.insert(
                0,
                None
            )

        return zip(args, defaults)

    def generate(self, module: ast.Module):
        self.visit(module)
        return self.source

    def visit(self, node: ast.AST) -> Any:
        self.hierarchy.append(node)
        super().visit(node)
        self.hierarchy.pop()

    def visit_alias(self, node: ast.alias) -> Any:
        self.source += node.name

        if hasattr(node, 'asname') and node.asname:
            self.source += f' as {node.asname}'

    def visit_arg(self, node: ast.arg) -> Any:
        self.source += node.arg

        if node.annotation:
            self.source += ': '
            self.visit(node.annotation)

    def visit_arg_with_default(self, node: ast.arg, default: ast.AST = None) -> Any:
        self.source += self.indent
        self.visit(node)
        if default:
            self.source += ' = '
            self.visit(default)

    def visit_arguments(self, node: ast.arguments) -> Any:
        with self._indent_context():
            for i, (arg, default) in enumerate(self._zip_args_and_defaults(node)):
                self.source += '\n'
                self.visit_arg_with_default(
                    arg,
                    default
                )

                if i != len(node.args) - 1:
                    self.source += ','

        self.source += '\n'

    def visit_comprehension(self, node: comprehension) -> Any:
        self.source += f'{self.indent}for '
        self.visit(node.target)
        self.source += ' in '
        self.visit(node.iter)

        if node.ifs:
            self.source += '\n'

            with self._indent_context():
                for i, if_ in enumerate(node.ifs):
                    self.source += self.indent
                    self.visit(if_)

                    if i != len(node.ifs) - 1:
                        self.source += '\n'

    def visit_keyword(self, node: ast.keyword) -> Any:
        self.source += f'{node.arg}='
        self.visit(node.value)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> Any:
        self.source += self.indent

        if node.value:
            self.source += f'{node.target.id}: '
            self.visit(node.annotation)
            self.source += ' = '
            self.visit(node.value)
        else:
            self.source += f'{node.target.id}: '
            self.visit(node.annotation)

    def visit_Assign(self, node: ast.Assign) -> Any:
        self.visit(node.targets[0])
        self.source += ' = '
        self.visit(node.value)
        self.source += '\n'

    def visit_Attribute(self, node: ast.Attribute) -> Any:
        self.visit(node.value)
        self.source += f'.{node.attr}'

    def visit_Call(self, node: ast.Call) -> Any:
        render_context = get_render_context(node)

        self.visit(node.func)
        self.source += '('

        with self._indent_context():
            if hasattr(node, 'args') and node.args:
                for i, arg_ in enumerate(node.args):
                    if render_context['expand']:
                        self.source += '\n'
                        self.source += self.indent

                    self.visit(arg_)

                    if i != len(node.args) - 1:
                        self.source += ','

                        if render_context['expand']:
                            self.source += '\n'
                        else:
                            self.source += ' '

            if hasattr(node, 'keywords') and node.keywords:
                for i, keyword in enumerate(node.keywords):
                    if render_context['expand']:
                        self.source += '\n'
                        self.source += self.indent

                    self.visit(keyword)

                    if i != len(node.keywords) - 1:
                        self.source += ','

                        if render_context['expand']:
                            self.source += '\n'
                        else:
                            self.source += ' '

        if render_context['expand']:
            self.source += '\n'
            self.source += self.indent

        self.source += ')'

    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        for decorator in node.decorator_list:
            self.source += f'{self.indent}@'
            self.visit(decorator)
            self.source += '\n'

        self.source += f'{self.indent}class {node.name}'

        if hasattr(node, 'bases') and node.bases:
            self.source += '('
            for base in node.bases:
                self.visit(base)
            self.source += ')'

        self.source += ':\n'

        with self._indent_context():
            for item in node.body:
                self.visit(item)
                self.source += '\n'

    def visit_Compare(self, node: ast.Compare) -> Any:
        lookup = {
            "Eq": "==",
            "NotEq": "!=",
            "Lt": "<",
            "LtE": "<=",
            "Gt": ">",
            "GtE": ">=",
            "Is": "is",
            "IsNot": "is not",
            "In": "in",
            "NotIn": "not in",
        }

        self.visit(node.left)
        self.source += f' {lookup[type(node.ops[0]).__name__]} '
        self.visit(node.comparators[0])

    def visit_Constant(self, node: ast.Constant) -> Any:
        if isinstance(node.value, str):
            self.source += f"'{node.value}'"
        else:
            self.source += str(node.value)

    def visit_Dict(self, node: ast.Dict) -> Any:
        render_context = get_render_context(node)

        self.source += '{'

        if node.keys:
            self.source += '\n'

        with self._indent_context():
            for key, value in zip(node.keys, node.values):
                self.source += f'{self.indent}'
                self.visit(key)
                self.source += ': '

                if render_context['expand']:
                    self.source += '(\n'
                    self.source += self.indent + 4 * ' '

                self.visit(value)

                if render_context['expand']:
                    self.source += '\n'
                    self.source += self.indent + ')'

                self.source += ',\n'

        if node.keys:
            self.source += f'{self.indent}'

        self.source += '}'

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        self.source += f'{self.indent}def {node.name}('

        if hasattr(node, 'args') and node.args:
            self.visit(node.args)
            self.source += self.indent

        self.source += ')'

        if hasattr(node, 'returns') and node.returns:
            self.source += ' -> '
            self.visit(node.returns)

        self.source += ':\n'

        prev = None

        with self._indent_context():
            for body in node.body:
                self.source += self.indent

                if isinstance(body, ast.If):
                    self.source += '\n'

                elif prev and type(prev) != type(body):
                    self.source += '\n'

                self.visit(body)

                if isinstance(body, (ast.Return, ast.Call)):
                    self.source += '\n'

                prev = body

    def visit_ImportFrom(self, node: ast.ImportFrom) -> Any:
        self.source += self.indent
        self.source += f'from {node.module} import ('

        with self._indent_context():
            for i, name in enumerate(node.names):
                self.source += '\n'
                self.source += self.indent
                self.visit(name)

                if i != len(node.names) - 1:
                    self.source += ','

            self.source += '\n'

        self.source += f'{self.indent})\n'

    def visit_If(self, node: ast.If) -> Any:
        self.source += f'{self.indent}if '
        self.visit(node.test)
        self.source += ':\n'

        with self._indent_context():
            for body in node.body:
                self.source += self.indent
                self.visit(body)

        if hasattr(node, 'orelse'):
            self.source += f'{self.indent}else:\n'

            with self._indent_context():
                for body in node.orelse:
                    self.visit(body)

    def visit_ListComp(self, node: ast.ListComp) -> Any:
        self.source += f'['

        with self._indent_context():
            self.source += f'\n{self.indent}'
            self.visit(node.elt)

            if node.generators:
                self.source += '\n'

            for i, generator in enumerate(node.generators):
                self.visit(generator)

                if i != len(node.generators) - 1:
                    self.source += '\n'

        self.source += '\n'
        self.source += f'{self.indent}]'

    def visit_Module(self, node: ast.Module) -> Any:
        for item in node.body:
            if isinstance(item, (ast.ClassDef, ast.FunctionDef)):
                self.source += '\n\n'
            if isinstance(item, ast.Assign):
                self.source += '\n'
            self.visit(item)

    def visit_Name(self, node: ast.Name) -> Any:
        self.source += node.id

    def visit_Return(self, node: ast.Return) -> Any:
        self.source += f'{self.indent}return '
        self.visit(node.value)

    def visit_Subscript(self, node: ast.Subscript) -> Any:
        render_context = get_render_context(node)

        self.visit(node.value)
        self.source += '['

        if render_context['expand']:
            self.source += '\n'

        with self._indent_context():

            if isinstance(node.slice, ast.Tuple):
                for i, element in enumerate(node.slice.elts):
                    if render_context['expand']:
                        self.source += self.indent

                    self.visit(element)

                    if i != len(node.slice.elts) - 1:
                        self.source += ','

                        if render_context['expand']:
                            self.source += '\n'
                        else:
                            self.source += ' '

            else:
                if render_context['expand']:
                    self.source += self.indent

                self.visit(node.slice)

        if render_context['expand']:
            self.source += '\n'
            self.source += self.indent

        self.source += ']'
