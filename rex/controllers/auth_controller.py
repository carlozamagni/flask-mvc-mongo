from flask import Blueprint, request, session, redirect, url_for, render_template
from rex import app, db

__author__ = 'carlozamagni'

auth_ctrl = Blueprint('auth', __name__, static_folder='static', template_folder='templates')

@auth_ctrl.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('main_page'))
    return render_template('login.html', error=error)


@auth_ctrl.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('main_page'))