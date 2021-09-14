from database import db


class CUpdateStudent:
    data = None

    def __init__(self, data: dict):
        self.data = data

    def update_student(self):
        return db.update(data=self.data)
