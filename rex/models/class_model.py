from mongokit import Document
from rex import app, db
import validators

__author__ = 'carlozamagni'

class Class(Document):
    __collection__ = 'classes'

    structure = {
        'name': unicode,
        'academic_year': unicode,
    }
    validators = {
        'name': validators.max_length(50),
        'academic_year': validators.academic_year()
    }
    use_dot_notation = True

    def __repr__(self):
        return '<Class %r>' % self.name

db.register([Class])