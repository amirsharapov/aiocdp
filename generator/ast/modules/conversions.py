import ast
from typing import Iterable

from generator.parser.types import Domain


def generate(domains: Iterable[Domain]):
    root = ast.Module(
        body=[]
    )

    ast_domain_names_dict = ast.Dict(
        keys=[],
        values=[]
    )

    ast_domain_method_names_dict = ast.Dict(
        keys=[],
        values=[]
    )

    ast_params_properties_dict = ast.Dict(
        keys=[],
        values=[]
    )

    ast_return_properties_dict = ast.Dict(
        keys=[],
        values=[]
    )

    for domain in domains:
        pass

    root.body.extend([
        ast.Assign(
            targets=[ast.Name('domain_names')],
            value=ast_domain_names_dict
        ),
        ast.Assign(
            targets=[ast.Name('method_names')],
            value=ast_domain_method_names_dict
        ),
        ast.Assign(
            targets=[ast.Name('params_properties')],
            value=ast_params_properties_dict
        ),
        ast.Assign(
            targets=[ast.Name('return_properties')],
            value=ast_return_properties_dict
        )
    ])

    return root
