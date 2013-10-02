from bson.json_util import dumps
from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from rex import db, lm
from rex.models import user_model


__author__ = 'cazamagni'

user_ctrl = Blueprint('user', __name__, static_folder='static', template_folder='templates')


@user_ctrl.route('/', methods=['GET', 'POST'])
def home():
    users_list = db.User.find()
    return dumps(users_list)


@user_ctrl.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    #else must return something as login-process result
    return


@user_ctrl.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        user = db.User()
        user.name = request.form['name']
        user.email = request.form['email']
        user.save()
        return redirect(url_for('home'))

    return render_template('user/new.html')


@lm.user_loader
def load_user(id):
    return db.User.find_one({'_id': int(id)})
