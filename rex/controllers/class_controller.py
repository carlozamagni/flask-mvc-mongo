from bson.json_util import dumps
from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from rex import db, lm
from rex.models import class_model

__author__ = 'carlozamagni'

class_ctrl = Blueprint('class', __name__, static_folder='static', template_folder='templates')

@class_ctrl.route('/')
def classes_list():
    classes = db.Class.find()
    return dumps(classes)

@class_ctrl.route('/new', methods=['GET', 'POST'])
def new_class():
    if request.method == 'POST':
        cls = db.Class()
        cls.name = request.form['name']
        cls.email = request.form['email']
        cls.save()
        return redirect(url_for('classes_list'))

    return render_template('class/new.html')