from app import create_app
from flask_mail import Mail
from flask import render_template,request,redirect,url_for, flash, session
from app.personal_informacion import details_portfolio
from app.email import send


app = create_app()
mail = Mail(app)

@app.errorhandler(404)
def page_not_found(error):
    session.clear()
    return render_template('error/error_404.html', error = error)

@app.errorhandler(500)
def internal_server_error(error):
    session.clear()
    return render_template('error/error_500.html', error = error)

@app.route('/email', methods = ['POST'])
def email():
    if request.method == 'POST':
        send(mail)
        return redirect(url_for('index'))

@app.route('/blog')
def blogs():
    return redirect(url_for('index'))
    return render_template('blog/index.html', json = details_portfolio())

@app.route('/')
def index():
    if session.get('user'):
        session.clear()
    return render_template('principal/index.html', json = details_portfolio())
