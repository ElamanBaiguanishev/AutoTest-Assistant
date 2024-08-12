from typing import List, Optional
from api.models.Test import Test, test_id
from api.repositories.base_repository import BaseRepository
from view.utils.file_manager import FileManager


class TestRepository(BaseRepository[Test, test_id]):
    def __init__(self):
        self.file_manager = FileManager('resources/db/tests.json')

    def get_all(self) -> List[Test]:
        return self.file_manager.load_data(Test)

    def find_by_id(self, _id: test_id) -> Optional[Test]:
        tests = self.file_manager.load_data(Test)
        return next((test for test in tests if test.id == _id), None)

    def add(self, test: Test):
        tests = self.file_manager.load_data(Test)
        tests.append(test)
        self.file_manager.save_data(tests)

    def update(self, _id: test_id, updated_test: Test):
        tests = self.file_manager.load_data(Test)
        for index, test in enumerate(tests):
            if test.id == _id:
                tests[index] = updated_test
                break
        self.file_manager.save_data(tests)

    def delete(self, _id: test_id):
        tests = self.file_manager.load_data(Test)
        tests = [test for test in tests if test.id != _id]
        self.file_manager.save_data(tests)
