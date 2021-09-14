from database import db


class CDeleteStudent:
    id = ''

    def __init__(self, id: str):
        self.id = id

    def delete_student(self):
        return db.delete(id=self.id)
