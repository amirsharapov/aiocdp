from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields
from typing import Optional


@dataclass
class Node(ABC):
    parent: Optional['Node'] = field(
        init=False,
        repr=False
    )

    raw: dict

    @abstractmethod
    def resolve(self, parent: Optional['Node']):
        ...

    def __post_init__(self):
        self.parent = None


def resolve_parent_refs(node: 'Node'):
    for field_ in fields(node):
        if field_.name == 'parent':
            continue

        item = getattr(node, field_.name)

        if isinstance(item, Node):
            item.parent = node
            resolve_parent_refs(item)

        elif isinstance(item, list):
            for item_ in item:
                if isinstance(item_, Node):
                    item_.parent = node
                    resolve_parent_refs(item_)

        elif isinstance(item, dict):
            for item_ in item.values():
                if isinstance(item_, Node):
                    item_.parent = node
                    resolve_parent_refs(item_)
