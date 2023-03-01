from flask import redirect, url_for, render_template, flash
from .post_login_logic import init_session
from .get_login_logic import user_exist

def get_login():
    error = user_exist()
    if error is None:
        return render_template('auth/login.html')
    flash(error)
    return redirect(url_for('auth.register'))
    
    

def post_login():
    error = init_session()
    if error is None:
        flash('Bienvenido!')
        return redirect(url_for('setting.index'))
    
    flash(error)
    return redirect(url_for('auth.login'))