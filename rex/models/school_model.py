__author__ = 'carlozamagni'

from mongokit import Document
from rex import app, db
import validators


class School(Document):
    __collection__ = 'schools'

