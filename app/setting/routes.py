from . import setting
from flask import render_template, url_for, redirect, request, flash
from . import route_images, route_profesion, route_description, route_curse, route_proyecto, route_icon, route_social, route_personal_informacion

@setting.route('/')
def index():
    flash('cualquier ajuste se reflajera directamente en la pagina principal')
    return render_template('setting/index.html')

@setting.route('/icon', methods = ['GET', 'POST'])
def icon():
    if request.method == 'POST':
        route_icon.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_icon.html')

@setting.route('/personal', methods = ['GET', 'POST'])
def personal():
    if request.method == 'POST':
        route_personal_informacion.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_personal_informacion.html')

@setting.route('/description', methods = ['GET', 'POST'])
def description():
    if request.method == 'POST':
        route_description.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_description_perfil.html')

@setting.route('/images', methods = ['GET', 'POST'])
def images():
    if request.method == 'POST':
        route_images.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_image.html')

@setting.route('/profesion', methods = ['GET', 'POST'])
def profesion():
    if request.method == 'POST':
        route_profesion.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_profesion.html')

@setting.route('/social', methods = ['GET', 'POST'])
def social():
    if request.method == 'POST':
        route_social.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_social_media.html')

@setting.route('/curse', methods = ['GET', 'POST'])
def curse():
    if request.method == 'POST':
        route_curse.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_course.html')

@setting.route('/proyecto', methods = ['GET', 'POST'])
def Proyecto():
    if request.method == 'POST':
        route_proyecto.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_works.html')