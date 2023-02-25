from app.db import get_db
import os

def _crear_carpeta(titulo):
    ruta = os.path.join(os.getcwd(), 'app', 'static', 'images', 'portfolio', titulo)
    os.makedirs(ruta, exist_ok=True)
    with open("i.jpg", "rb") as image_file:
        file_name = f'{titulo}.jpg'
        with open(os.path.join(ruta, file_name), 'wb') as new_file:
            new_file.write(image_file.read())
        image_file.close()
        
def data():
    db, c = get_db()
    sql = 'INSERT INTO trabajos(titutlo, descripcion, url_proyecto, type) VALUES(%s, %s, %s, %s)'
    for i in range(4):
        if i != 0:
            titulo = f'proyecto{i}'
            _crear_carpeta(titulo)
            values = (titulo, f'describe el proyecto {i}', 'www.algo.es', i)
            c.execute(sql, values)
    db.commit()
    return True