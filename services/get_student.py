from database import db


class CGetStudent:
    id = ''

    def __init__(self, id):
        self.id = id

    def get_student(self):
        return db.get(id=self.id)