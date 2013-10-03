from mongokit import Document
from rex import app, db
import validators

__author__ = 'carlozamagni'

class Class(Document):
    __collection__ = 'classes'

    structure = {
        'name': unicode,
        'academic_year': unicode,
        'teachings': list
    }
    validators = {
        'name': validators.max_length(50),
        'academic_year': validators.academic_year()
    }

    default_values = {'teachings': []}

    use_dot_notation = True

    def __repr__(self):
        return '<Class %r>' % self.name


class Teaching(object):
    def __init__(self, subject_id=None, teacher_id=None):
        self.subject_id = subject_id
        self.teacher_id = teacher_id

    def get_teacher_id(self):
        return self.teacher_id

    def get_subject_id(self):
        return self.subject_id



db.register([Class])