from dataclasses import dataclass

from generator.utils import MaybeUndefined, UNDEFINED
from generator.types.ref import Ref


@dataclass
class Items:
    type: MaybeUndefined[str]
    ref: MaybeUndefined[Ref]

    @classmethod
    def from_dict(cls, data):
        ref = data.get('$ref', None)

        if ref:
            ref = Ref.from_str(ref)

        return cls(
            type=data.get('type', UNDEFINED),
            ref=ref
        )
