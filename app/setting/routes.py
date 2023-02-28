from . import setting
from flask import render_template, url_for, redirect
from . import route_images, route_profesion, route_description

@setting.route('/')
def index():
    return render_template('setting/index.html')

@setting.route('/images', methods = ['POST'])
def images():
    route_images.function()
    return redirect(url_for('setting.index'))

@setting.route('/profesion', methods = ['POST'])
def profesion():
    route_profesion.function()
    return redirect(url_for('setting.index'))

@setting.route('/description', methods = ['POST'])
def description():
    route_description.function()
    return redirect(url_for('setting.index'))

@setting.route('/Proyecto', methods = ['POST'])
def Proyecto():
    return redirect(url_for('setting.index'))

@setting.route('/curse', methods = ['POST'])
def curse():
    return redirect(url_for('setting.index'))







''' @setting.route('/prueba', methods = ['GET', 'POST'])
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
    return render_template('formulario.html', json = data) '''