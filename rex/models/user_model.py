import datetime
from mongokit import Document
from rex import app, db
import validators

__author__ = 'cazamagni'


class User(Document):
    __collection__ = 'users'

    structure = {
        '_id': int,
        'name': unicode,
        'email': unicode,
        'username': unicode,
        'password': unicode,
        'role': int,
        'creation': datetime.datetime
    }
    validators = {
        'name': validators.max_length(50),
        'email': validators.max_length(120)
    }
    default_values = {'creation': datetime.datetime.utcnow()}
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
        return self.role

    def get_user_home(self, user_role):
        role = db['roles'].find_one({'_id': user_role})
        return role['home_page']


db.register([User])