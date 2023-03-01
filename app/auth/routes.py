from . import auth
from . import route_login, route_register
from flask import render_template, redirect, url_for, request, session, flash, g
import functools

@auth.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        return route_register.post_register()
    return route_register.get_register()

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return route_login.post_login()
    return route_login.get_login()

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@auth.before_app_request
def load_logged_in_user():
    user = session.get('user')
    
    if user is None:
        g.user= None
    else:
        g.user = user
    
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Inicia sesion')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view