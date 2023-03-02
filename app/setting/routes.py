from . import setting
from flask import render_template, url_for, redirect, request, flash
from . import route_images, route_profesion, route_description, route_curse, route_proyecto, route_icon, route_social, route_personal_informacion
from app.auth.routes import login_required
@setting.route('/')
@login_required
def index():
    flash('cualquier ajuste se reflajera directamente en la pagina principal')
    return render_template('setting/index.html')

@setting.route('/icon', methods = ['GET', 'POST'])
@login_required
def icon():
    if request.method == 'POST':
        route_icon.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_icon.html')

@setting.route('/personal', methods = ['GET', 'POST'])
@login_required
def personal():
    if request.method == 'POST':
        route_personal_informacion.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_personal_informacion.html')

@setting.route('/description', methods = ['GET', 'POST'])
@login_required
def description():
    if request.method == 'POST':
        route_description.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_description_perfil.html')

@setting.route('/images', methods = ['GET', 'POST'])
@login_required
def images():
    if request.method == 'POST':
        route_images.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_image.html')

@setting.route('/profesion', methods = ['GET', 'POST'])
@login_required
def profesion():
    if request.method == 'POST':
        route_profesion.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_profesion.html')

@setting.route('/social', methods = ['GET', 'POST'])
@login_required
def social():
    if request.method == 'POST':
        route_social.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_social_media.html')

@setting.route('/curse', methods = ['GET', 'POST'])
@login_required
def curse():
    if request.method == 'POST':
        route_curse.function()
        return redirect(url_for('setting.index'))
    return render_template('setting/form_course.html')

@setting.route('/proyecto', methods = ['GET', 'POST'])
@login_required
def Proyecto():
    if request.method == 'POST':
        error = route_proyecto.function()
        if error is None:
            return redirect(url_for('setting.index'))
        flash(error)
        return redirect(url_for('setting.index'))
    return render_template('setting/form_works.html')