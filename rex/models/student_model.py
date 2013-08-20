from mongokit import Document
from rex import app, db
import validators

__author__ = 'cazamagni'

class Student(Document):
    __collection__ = 'students'

    structure = {
        'first_name': unicode,
        'last_name': unicode,
        'email': unicode,
    }
    validators = {
        'first_name': validators.max_length(50),
        'last_name': validators.max_length(50),
        'email': validators.max_length(120)
    }
    use_dot_notation = True

    def __repr__(self):
        return '<Student %r %r>' % (self.first_name, self.last_name)

db.register([Student])