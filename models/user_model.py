from mongokit import Document
import validators

__author__ = 'cazamagni'


class User(Document):
    structure = {
        'name': unicode,
        'email': unicode,
    }
    validators = {
        'name': validators.max_length(50),
        'email': validators.max_length(120)
    }
    use_dot_notation = True

    def __repr__(self):
        return '<User %r>' % self.name