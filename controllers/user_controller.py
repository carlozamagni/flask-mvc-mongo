from flask import Blueprint

__author__ = 'cazamagni'

user = Blueprint('user', __name__, static_folder='static', template_folder='templates')
print user.name


@user.route('/', methods=['GET', 'POST'])
def list():
    return 'user'