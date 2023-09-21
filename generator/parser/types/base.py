from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields
from typing import Optional


@dataclass
class Node(ABC):
    parent: Optional['Node'] = field(
        init=False,
        repr=False
    )

    raw: dict = field(
        repr=False
    )

    def __post_init__(self):
        self.parent = None


def recursively_link_children(node: 'Node'):
    for field_ in fields(node):
        if field_.name == 'parent':
            continue

        item = getattr(node, field_.name)

        if isinstance(item, Node):
            item.parent = node
            recursively_link_children(item)

        elif isinstance(item, list):
            for item_ in item:
                if isinstance(item_, Node):
                    item_.parent = node
                    recursively_link_children(item_)

        elif isinstance(item, dict):
            for item_ in item.values():
                if isinstance(item_, Node):
                    item_.parent = node
                    recursively_link_children(item_)
