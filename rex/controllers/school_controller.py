__author__ = 'carlozamagni'

from bson.json_util import dumps
from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from rex import db, lm
from rex.models import school_model


__author__ = 'cazamagni'

student_ctrl = Blueprint('school', __name__, static_folder='static', template_folder='templates')

@student_ctrl.route('/')
def list_students():
    students_list = db.Student.find()
    return dumps(students_list)