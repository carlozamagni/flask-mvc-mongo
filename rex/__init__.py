from flask import Flask, send_from_directory
from flask.ext.login import login_required, LoginManager
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

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.route('/')
@login_required
def hello_world():
    return render_template('home.html')


