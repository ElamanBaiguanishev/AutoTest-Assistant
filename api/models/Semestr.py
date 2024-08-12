from dataclasses import dataclass
from typing import TypeAlias

from api.models.Group import group_id

semestr_id: TypeAlias = str


@dataclass
class Semestr:
    id: semestr_id
    name: str
    groups: list[group_id]
