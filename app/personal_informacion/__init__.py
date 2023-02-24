from . import full_name, profesiones, descripcion, services, social_media
def details_portfolio():
    json = dict()
    json['name'] = full_name.data()
    json['profesiones'] = profesiones.data()
    json['social_media'] = social_media.data()
    json['descriptions'] = descripcion.data()
    json['courses'] = services.data()
    
    return json