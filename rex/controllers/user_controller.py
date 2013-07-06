from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from rex import app, db


__author__ = 'cazamagni'

user = Blueprint('user', __name__, static_folder='static', template_folder='templates')

@user.route('/', methods=['GET', 'POST'])
#@app.route('/', methods=['GET', 'POST'])
def list():
    #db = app.db
    users_list = db.User.find()
    return jsonify(**dict(users_list))


@user.route('/new', methods=['GET', 'POST'])
#@app.route('/new', methods=['GET', 'POST'])
def new():

    if request.method == 'POST':
        #db = app.db
        user = db.User()
        user.name = request.form['name']
        user.email = request.form['email']
        user.save()
        return redirect(url_for('list'))

    return render_template('user/new.html')