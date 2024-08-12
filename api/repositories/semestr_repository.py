from typing import List, Optional
from api.models.Semestr import Semestr, semestr_id
from api.repositories.base_repository import BaseRepository
from view.utils.file_manager import FileManager


class SemestrRepository(BaseRepository[Semestr, semestr_id]):
    def __init__(self):
        self.file_manager = FileManager('resources/db/semestrs.json')

    def get_all(self) -> List[Semestr]:
        return self.file_manager.load_data(Semestr)

    def find_by_id(self, _id: semestr_id) -> Optional[Semestr]:
        semestrs = self.file_manager.load_data(Semestr)
        return next((semestr for semestr in semestrs if semestr.id == _id), None)

    def add(self, semestr: Semestr):
        semestrs = self.file_manager.load_data(Semestr)
        semestrs.append(semestr)
        self.file_manager.save_data(semestrs)

    def update(self, _id: semestr_id, updated_semestr: Semestr):
        semestrs = self.file_manager.load_data(Semestr)
        for index, semestr in enumerate(semestrs):
            if semestr.id == _id:
                semestrs[index] = updated_semestr
                break
        self.file_manager.save_data(semestrs)

    def delete(self, _id: semestr_id):
        semestrs = self.file_manager.load_data(Semestr)
        semestrs = [semestr for semestr in semestrs if semestr.id != _id]
        self.file_manager.save_data(semestrs)
