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

#setattr(sys.modules['settings'],'mongoDb', Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT']))
#setattr(sys.modules['settings'],'mongoDb', db)

lm = LoginManager()
lm.init_app(app)
lm.login_view = '/user/login'

from rex.controllers import user_controller
app.register_blueprint(blueprint=user_controller.user, url_prefix='/user')

from rex.controllers import auth_controller
app.register_blueprint(blueprint=auth_controller.auth, url_prefix='/auth')



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.route('/')
@login_required
def hello_world():
    return render_template('home.html')


