from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields
from typing import Optional


@dataclass
class Node(ABC):
    parent: Optional['Node'] = field(
        init=False,
        repr=False
    )

    def __post_init__(self):
        self.parent = None

    def resolve_parent_refs(self):
        for field_ in fields(self):
            if field_.name == 'parent':
                continue

            attribute = getattr(self, field_.name)

            if isinstance(attribute, Node):
                attribute.parent = self
                attribute.resolve_parent_refs()

            elif isinstance(attribute, list):
                for item in attribute:
                    if isinstance(item, Node):
                        item.parent = self
                        item.resolve_parent_refs()

            elif isinstance(attribute, dict):
                for item in attribute.values():
                    if isinstance(item, Node):
                        item.parent = self
                        item.resolve_parent_refs()


@dataclass
class ComplexNode(Node, ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass
