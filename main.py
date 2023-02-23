from app import create_app
from flask import render_template,request,redirect,url_for, flash, jsonify
from app.modules import details_portfolio
import os

app = create_app()

@app.route('/email', methods = ['POST'])
def blog():
    if request.method == 'POST':
        flash('Mensaje Enviado')
        return redirect(url_for('index'))

@app.route('/blog')
def blogs():
    data = details_portfolio()
    return render_template('blog/index.html', json = data)

@app.route('/')
def index():
    data = details_portfolio()
    return render_template('principal/index.html', json = data)
    

@app.route('/prueba', methods = ['GET', 'POST'])
def prueba():
    if request.method == 'POST':
        #obtener todos los datos del formulario
        titulo = request.form['titulo']
        enlace = request.form['enlace']
        description = request.form['description']
        images = request.files.getlist('images')
        #creamos la carpeta para el proyecto realizado
        ruta = os.path.join(os.getcwd(), 'app', 'static', 'images', 'portfolio', titulo)
        os.makedirs(ruta, exist_ok=True)
        #contamos la cantidad de archivos
        archivos = len(os.listdir(ruta))
        #guardamos los archivos en la ruta especificada
        for image in images:
            archivos += 1
            file_name = f'{titulo}_{archivos}.jpg'
            image.save(os.path.join(ruta, file_name))
        return 'recibido'
        #return redirect(url_for('index'))
    data = details_portfolio()
    return render_template('formulario.html', json = data)