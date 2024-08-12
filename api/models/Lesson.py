from dataclasses import dataclass
from typing import TypeAlias

from api.models.Test import test_id

lesson_id: TypeAlias = str


@dataclass
class Lesson:
    id: lesson_id
    name: str
    tests: list[test_id]
