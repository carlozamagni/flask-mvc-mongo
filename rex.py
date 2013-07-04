import os
import sys
from flask import Flask, send_from_directory
from controllers import user_controller
from mongokit import Connection
import settings

app = Flask(__name__)

app.config.from_object(settings)

error = None

try:
    setattr(sys.modules['settings'],'mongoDb', Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT']))
except:
    error = 'database init'

app.register_blueprint(blueprint=user_controller.user, url_prefix='/user')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.route('/')
def hello_world():
    if error is None:
        return 'Hello World!'

    return error


if __name__ == '__main__':
    app.run(debug=True)
