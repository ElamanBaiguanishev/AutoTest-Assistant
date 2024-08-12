import json
from typing import List, TypeVar, Type

T = TypeVar('T')


class FileManager:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_data(self, cls: Type[T]) -> List[T]:
        try:
            with open(self.filepath, encoding='utf-8') as file:
                data = json.load(file)
                return [cls(**item) for item in data]
        except FileNotFoundError:
            return []

    def save_data(self, data: List[T]):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump([item.__dict__ for item in data], file, ensure_ascii=False, indent=4)
