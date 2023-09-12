from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from cdp.domains.accessibility import Accessibility

if TYPE_CHECKING:
    from cdp.target import Target


@dataclass
class TargetDomains:
    target: 'Target'

    accessibility: 'Accessibility' = field(
        init=False
    )
