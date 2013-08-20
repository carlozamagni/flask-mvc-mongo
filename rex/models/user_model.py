from mongokit import Document
from rex import app, db
import validators

__author__ = 'cazamagni'

class User(Document):
    __collection__ = 'users'

    structure = {
        'name': unicode,
        'email': unicode,
        'role': int,
    }
    validators = {
        'name': validators.max_length(50),
        'email': validators.max_length(120)
    }
    use_dot_notation = True

    def __repr__(self):
        return '<User %r>' % self.name

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get_role(self):
        return

db.register([User])