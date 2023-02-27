from app import create_app
from flask import render_template,request,redirect,url_for, flash
from app.personal_informacion import details_portfolio
import os

app = create_app()

@app.route('/email', methods = ['POST'])
def blog():
    if request.method == 'POST':
        flash('Mensaje Enviado')
        return redirect(url_for('index'))

@app.route('/blog')
def blogs():
    return render_template('blog/index.html', json = details_portfolio())

@app.route('/')
def index():
    return render_template('principal/index.html', json = details_portfolio())
