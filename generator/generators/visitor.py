import ast
import contextlib
from typing import Any


def indent_lines(lines: str | list[str], indent: int) -> str:
    if isinstance(lines, str):
        lines = lines.split('\n')

    indent_str = ' ' * indent

    return '\n'.join([
        f'{indent_str}{line}' for
        line in
        lines
    ])


def concat_lines(lines: list[str], trailing_newline: bool = False) -> str:
    lines = '\n'.join(lines)

    if trailing_newline:
        lines += '\n'

    return lines


def create_vertical_comma_separated_list(
        items: list[str],
        indent: int,
        trailing_comma: bool = True
) -> str:
    items = ',\n'.join(items)

    if trailing_comma:
        items += ','

    return indent_lines(
        items,
        indent
    )


# noinspection PyTypeChecker
class SourceCodeGenerator(ast.NodeVisitor):
    def __init__(self):
        self.source = ''
        self.indent_length = 0

    @property
    def indent(self):
        return ' ' * self.indent_length

    @contextlib.contextmanager
    def indent_context(self):
        self.indent_length += 4
        yield
        self.indent_length -= 4

    def generate(self, module: ast.Module):
        self.visit(module)
        return self.source

    def visit_alias(self, node: ast.alias) -> Any:
        self.source += f'{self.indent}{node.name}'

    def visit_arg(self, node: ast.arg) -> Any:
        self.source += f'{self.indent}{node.arg}'

        if node.annotation:
            self.source += ': '
            self.visit(node.annotation)

    def visit_arguments(self, node: ast.arguments) -> Any:
        self.source += '('

        with self.indent_context():
            for i, arg_ in enumerate(node.args):
                self.source += '\n'
                self.visit(arg_)

                if i != len(node.args) - 1:
                    self.source += ','

        self.source += '\n'
        self.source += f'{self.indent})'

    def visit_Assign(self, node: ast.Assign) -> Any:
        self.source += self.indent
        self.visit(node.targets[0])
        self.source += ' = '
        self.visit(node.value)
        self.source += '\n'

    def visit_Attribute(self, node: ast.Attribute) -> Any:
        self.visit(node.value)
        self.source += f'.{node.attr}'

    def visit_Call(self, node: ast.Call) -> Any:
        self.visit(node.func)
        self.source += '('

        with self.indent_context():
            for i, arg_ in enumerate(node.args):
                self.source += '\n'
                self.source += self.indent
                self.visit(arg_)

                if i != len(node.args) - 1:
                    self.source += ','

        self.source += '\n'
        self.source += f'{self.indent})'

    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        for decorator in node.decorator_list:
            self.source += f'{self.indent}@'
            self.visit(decorator)
            self.source += '\n'

        self.source += f'{self.indent}class {node.name}('

        for base in node.bases:
            self.visit(base)

        self.source += '):\n'

        with self.indent_context():
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
        self.source += node.value

    def visit_Dict(self, node: ast.Dict) -> Any:
        self.source += '{'

        if node.keys:
            self.source += '\n'

        with self.indent_context():
            for key, value in zip(node.keys, node.values):
                self.source += f'{self.indent}"'
                self.visit(key)
                self.source += '": '
                self.visit(value)
                self.source += ',\n'

        if node.keys:
            self.source += f'{self.indent}'

        self.source += '}'

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        self.source += f'{self.indent}def {node.name}'
        self.visit(node.args)
        self.source += ':\n'

        prev = None

        with self.indent_context():
            for body in node.body:
                if isinstance(body, ast.If):
                    self.source += '\n'

                elif prev and type(prev) != type(body):
                    self.source += '\n'

                self.visit(body)

                if isinstance(body, (ast.Return, ast.Call)):
                    self.source += '\n'

                prev = body

    def visit_ImportFrom(self, node: ast.ImportFrom) -> Any:
        self.source += f'from {node.module} import ('

        with self.indent_context():
            for i, name in enumerate(node.names):
                self.source += '\n'
                self.visit(name)

                if i != len(node.names) - 1:
                    self.source += ','

        self.source += '\n)\n'

    def visit_If(self, node: ast.If) -> Any:
        self.source += f'{self.indent}if '
        self.visit(node.test)
        self.source += ':\n'

        with self.indent_context():
            for body in node.body:
                self.visit(body)

        if hasattr(node, 'orelse'):
            self.source += f'{self.indent}else:\n'

            with self.indent_context():
                for body in node.orelse:
                    self.visit(body)

    def visit_Module(self, node: ast.Module) -> Any:
        for item in node.body:
            if isinstance(item, (ast.ClassDef, ast.FunctionDef)):
                self.source += '\n\n'
            self.visit(item)

    def visit_Name(self, node: ast.Name) -> Any:
        self.source += node.id

    def visit_Return(self, node: ast.Return) -> Any:
        self.source += f'{self.indent}return '
        self.visit(node.value)

    def visit_Subscript(self, node: ast.Subscript) -> Any:
        self.visit(node.value)
        self.source += '['
        self.visit(node.slice)
        self.source += ']'
