from flask import redirect, url_for, render_template, flash
from .post_register_logic import register_user
def get_register():
    flash('estas por registrar un usuario, para administrar la pagina')
    return render_template('auth/register.html')
    

def post_register():
    error = register_user()
    if error is None:
        flash('usuario registrado exitosamente, ya pudes iniciar sesion')
        return redirect(url_for('auth.login'))
    flash(error)
    return render_template('auth/register.html')