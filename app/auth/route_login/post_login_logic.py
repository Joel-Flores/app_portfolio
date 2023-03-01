from flask import request, session
from werkzeug.security import check_password_hash

from app.db import get_db


def init_session():
    db, c = get_db()    
    username = request.form['username']
    password = request.form['password']
    error = None
    
    query = '''SELECT nick_name, password, register_active
	FROM user
    WHERE nick_name = %s'''
    values = [username]
    c.execute(query, values)
    user = c.fetchone()
    
    if user is None:
        error = 'Usuario y/o Contraseña invalida'
    elif not check_password_hash(user['password'],password):
        error = 'Usuario y/o Contraseña invalida' 
    elif user['register_active'] is False:
        error = 'Permiso Denegado'

    if error is None:
        session.clear()
        session['user'] = user
    
    return error