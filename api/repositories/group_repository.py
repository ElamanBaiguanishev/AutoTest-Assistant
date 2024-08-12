from typing import List, Optional
from api.models.Group import Group, group_id
from api.repositories.base_repository import BaseRepository
from view.utils.file_manager import FileManager


class GroupRepository(BaseRepository[Group, group_id]):
    def __init__(self):
        self.file_manager = FileManager("resources/db/groups.json")

    def get_all(self) -> List[Group]:
        return self.file_manager.load_data(Group)

    def find_by_id(self, _id: group_id) -> Optional[Group]:
        groups = self.file_manager.load_data(Group)
        return next((group for group in groups if group.id == _id), None)

    def add(self, group: Group):
        groups = self.file_manager.load_data(Group)
        groups.append(group)
        self.file_manager.save_data(groups)

    def update(self, _id: group_id, updated_group: Group):
        groups = self.file_manager.load_data(Group)
        for index, group in enumerate(groups):
            if group.id == _id:
                groups[index] = updated_group
                break
        self.file_manager.save_data(groups)

    def delete(self, _id: group_id):
        groups = self.file_manager.load_data(Group)
        groups = [group for group in groups if group.id != _id]
        self.file_manager.save_data(groups)
