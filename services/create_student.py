import random
import string
from database import db


class CCreateStudent:
    id_digits = ''
    first_letters = ''
    last_letters = ''

    def __init__(self):
        self.id_digits = string.digits
        self.first_letters = string.ascii_uppercase
        self.last_letters = string.ascii_letters

    def create(self):
        for index in range(1000):
            data = {"id": self.get_random_value(self.id_digits),
                    "first_name": self.get_random_value(self.first_letters),
                    "last_name": self.get_random_value(self.last_letters)}
            done, err = db.create(data=data)
            if not done:
                return done, err
        return True, None

    def get_random_value(self, letters: str):
        return ''.join(random.choice(letters) for i in range(10))
