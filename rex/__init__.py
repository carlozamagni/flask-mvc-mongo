from flask import Flask, send_from_directory
from flask.ext.mongokit import MongoKit
import os
import settings

__author__ = 'carlozamagni'

app = Flask(__name__)
app.config.from_object(settings)

db = MongoKit(app)

#setattr(sys.modules['settings'],'mongoDb', Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT']))
#setattr(sys.modules['settings'],'mongoDb', db)

from rex.controllers import user_controller
app.register_blueprint(blueprint=user_controller.user, url_prefix='/user')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.route('/')
def hello_world():
    return 'Hello World!'


