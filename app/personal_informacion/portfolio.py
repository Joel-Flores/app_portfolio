from app.db import get_db
import os
def type_works():
    db, c = get_db()
    sql = 'SELECT tipo FROM tipo_trabajo'
    c.execute(sql)
    return c.fetchall()

def _traer_imagenes(datos):
    for dato in datos:
        ruta = os.path.join(os.getcwd(), 'app', 'static', 'images', 'portfolio', dato['titulo'])
        archivos = os.listdir(ruta)
        ruta = list()
        for archivo in archivos:
            ruta.append(f'images/portfolio/{dato["titulo"]}/{archivo}')
            dato['archivos'] = ruta
    return datos

def data():
    db, c = get_db()
    sql = '''
    SELECT titutlo as titulo, descripcion, url_proyecto, tt.tipo 
    FROM trabajos as t
    inner join tipo_trabajo as tt
    on tt.id = t.type;'''
    c.execute(sql)
    json = _traer_imagenes(c.fetchall())
    return json