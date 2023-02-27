from . import setting
from flask import render_template
from .data_json import data
@setting.route('/')
def index():
    json = data()
    return render_template('setting/index.html', json = json)