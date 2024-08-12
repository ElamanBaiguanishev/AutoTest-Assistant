from dataclasses import dataclass
from typing import TypeAlias

student_id: TypeAlias = str


@dataclass
class Student:
    id: student_id
    fio: str
    login: str
    password: str
