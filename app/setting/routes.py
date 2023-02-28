from . import setting
from flask import render_template, url_for, redirect
from . import route_images, route_profesion, route_description, route_curse, route_proyecto

@setting.route('/')
def index():
    return render_template('setting/index.html')

@setting.route('/images', methods = ['POST'])
def images():
    route_images.function()
    return redirect(url_for('setting.index'))

@setting.route('/profesion', methods = ['POST'])
def profesion():
    route_profesion.function()
    return redirect(url_for('setting.index'))

@setting.route('/description', methods = ['POST'])
def description():
    route_description.function()
    return redirect(url_for('setting.index'))

@setting.route('/proyecto', methods = ['POST'])
def Proyecto():
    route_proyecto.function()
    return redirect(url_for('setting.index'))

@setting.route('/curse', methods = ['POST'])
def curse():
    route_curse.function()
    return redirect(url_for('setting.index'))