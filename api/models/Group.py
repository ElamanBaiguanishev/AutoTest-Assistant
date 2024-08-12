from dataclasses import dataclass
from typing import TypeAlias

from api.models.Lesson import lesson_id
from api.models.Student import student_id

group_id: TypeAlias = str


@dataclass
class Group:
    id: group_id
    name: str
    students: list[student_id]
    lessons: list[lesson_id]
