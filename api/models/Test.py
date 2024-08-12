from dataclasses import dataclass
from typing import TypeAlias

test_id: TypeAlias = str


@dataclass
class Test:
    id: test_id
    name: str
    urls: list[str]
