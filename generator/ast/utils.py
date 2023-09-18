import ast


def ast_imports(import_tree: dict[str, set[str]]) -> list[ast.ImportFrom]:
    imports = []

    modules = sorted(import_tree.keys())

    for module in modules:
        types = import_tree[module]
        types = sorted(types)

        imports.append(
            ast.ImportFrom(
                module=module,
                names=[
                    ast.alias(type_) for type_ in types
                ]
            )
        )

    return imports
