import ast


def init_alias(
        name: str,
        asname: str = None
):
    return ast.alias(
        name=name,
        asname=asname
    )


def init_arg(
        arg: str,
        annotation: ast.expr = None,
        type_comment: str = None
):
    return ast.arg(
        arg=arg,
        annotation=annotation,
        type_comment=type_comment
    )


def init_arguments(
        posonlyargs: list[ast.arg] = None,
        args: list[ast.arg] = None,
        vararg: ast.arg = None,
        kwonlyargs: list[ast.arg] = None,
        kw_defaults: list[ast.expr] = None,
        kwarg: ast.arg = None,
        defaults: list[ast.expr] = None
):
    return ast.arguments(
        posonlyargs=posonlyargs or [],
        args=args or [],
        vararg=vararg,
        kwonlyargs=kwonlyargs or [],
        kw_defaults=kw_defaults or [],
        kwarg=kwarg,
        defaults=defaults or []
    )


def init_class_def(
        name: str,
        bases: list[str] = None,
        decorator_list: list[str] = None,
        keywords: list[str] = None,
        body: list[ast.stmt] = None,
):
    return ast.ClassDef(
        name=name,
        bases=bases or [],
        decorator_list=decorator_list or [],
        keywords=keywords or [],
        body=body or []
    )


def init_function_def(
        name: str,
        args: ast.arguments = None,
        body: list[ast.stmt] = None,
        decorator_list: list[ast.expr] = None,
        returns: ast.expr = None,
        type_comment: str = None
):
    return ast.FunctionDef(
        name=name,
        args=args or init_arguments(),
        body=body or [],
        decorator_list=decorator_list or [],
        returns=returns,
        type_comment=type_comment
    )


def init_import_from(
        module: str = None,
        names: list[ast.alias] = None,
):
    return ast.ImportFrom(
        module=module,
        names=names or [],
        level=0
    )


def init_module(
        body: list[ast.stmt] = None,
        type_ignore: bool = False,
        type_ignores: list = None
):
    return ast.Module(
        body=body or [],
        type_ignore=type_ignore,
        type_ignores=type_ignores or []
    )


def init_name(
        id_: str
):
    return ast.Name(
        id=id_
    )


def init_subscript(
        value: ast.expr,
        slice_: ast.expr,
):
    return ast.Subscript(
        value=value,
        slice=slice_,
        ctx=ast.Load()
    )
