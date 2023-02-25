from . import full_name, profesiones, descripcion, services, social_media, portfolio, subir_a_profolio as s
def details_portfolio():
    json = dict()
    json['name'] = full_name.data()
    json['profesiones'] = profesiones.data()
    json['social_media'] = social_media.data()
    json['descriptions'] = descripcion.data()
    json['courses'] = services.data()
    json['type_works'] = portfolio.type_works()
    json['works'] = portfolio.data()
    
    return json