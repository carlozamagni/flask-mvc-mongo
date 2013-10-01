from flask import Blueprint, request, session, redirect, url_for, render_template
from rex import app, db
from rex.models import user_model

__author__ = 'carlozamagni'

auth_ctrl = Blueprint('auth', __name__, static_folder='static', template_folder='templates')

@auth_ctrl.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = db.User.find({'username':username})

        if user is None or user['password'] != password:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            session['user_id'] = user['id']

            return redirect(url_for('main_page'))
    return render_template('login.html', error=error)


@auth_ctrl.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('main_page'))