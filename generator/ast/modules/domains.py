import ast
from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from cdp.domains.domain import Domain


def generate(domains: Iterable['Domain']):
    root = ast.Module(
        body=[]
    )

    return root
