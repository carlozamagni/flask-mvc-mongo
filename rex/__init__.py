from json import dumps
import json
from flask import Flask, send_from_directory
from flask.ext.login import login_required, LoginManager, current_user
from flask.ext.mongokit import MongoKit
from flask.templating import render_template
import os
import settings

__author__ = 'carlozamagni'

app = Flask(__name__)
app.config.from_object(settings)

db = MongoKit(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = '/auth/login'

from rex.controllers import user_controller
app.register_blueprint(blueprint=user_controller.user_ctrl, url_prefix='/user')

from rex.controllers import auth_controller
app.register_blueprint(blueprint=auth_controller.auth_ctrl, url_prefix='/auth')

from rex.controllers import class_controller
app.register_blueprint(blueprint=class_controller.class_ctrl, url_prefix='/class')

from rex.controllers import student_controller
app.register_blueprint(blueprint=student_controller.student_ctrl, url_prefix='/student')

from rex.controllers import teacher_controller
app.register_blueprint(blueprint=teacher_controller.teacher_ctrl, url_prefix='/teacher')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.route('/')
@login_required
def hello_world():
    return dumps({'user_name': current_user['name'],
                  'user_email': current_user['email']})
    #return render_template('home.html')

@app.route('/setup')
def setup():
    inserted = []

    # roles
    roles = [{"_id": 0, "role_name": "student", "home_page": "user/student_home.html"},
             {"_id": 1, "role_name": "teacher", "home_page": "user/teacher_home.html"},
             {"_id": 2, "role_name": "admin", "home_page": "user/admin_home.html"}]
    db['roles'].drop()
    db['roles'].insert(roles)
    inserted.append(roles)

    #test users
    users = [{"_id": 0, "name": "test student", "email": "teststudent@email.com", "username": "test_student", "password": "test", "role": 0},
             {"_id": 1, "name": "test teacher", "email": "testteacher@email.com", "username": "test_teacher", "password": "test", "role": 1},
             {"_id": 2, "name": "test admin", "email": "testadmin@email.com", "username": "test_admin", "password": "test", "role": 2}]

    db['users'].drop()
    db['users'].insert(users)
    inserted.append(users)

    return json.dumps(inserted)


