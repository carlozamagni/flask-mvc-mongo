from bson.json_util import dumps
from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from rex import db, lm
from rex.models import user_model


__author__ = 'cazamagni'

teacher_ctrl = Blueprint('teacher', __name__, static_folder='static', template_folder='templates')

@teacher_ctrl.route('/')
def home():
    students_list = db.Student.find()
    return dumps(students_list)