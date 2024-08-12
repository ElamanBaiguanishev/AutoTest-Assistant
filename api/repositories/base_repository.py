from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')
ID = TypeVar('ID')


class BaseRepository(ABC, Generic[T, ID]):
    @abstractmethod
    def get_all(self) -> List[T]:
        """Возвращает список всех сущностей."""
        pass

    @abstractmethod
    def find_by_id(self, _id: ID) -> Optional[T]:
        """Находит сущность по идентификатору."""
        pass

    @abstractmethod
    def add(self, entity: T):
        """Добавляет новую сущность."""
        pass

    @abstractmethod
    def update(self, _id: ID, updated_entity: T):
        """Обновляет существующую сущность."""
        pass

    @abstractmethod
    def delete(self, _id: ID):
        """Удаляет сущность по идентификатору."""
        pass
