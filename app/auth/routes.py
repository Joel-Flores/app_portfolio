from . import auth
from flask import redirect, url_for

@auth.route('/login')
def login():
    
    return redirect(url_for('setting.index'))