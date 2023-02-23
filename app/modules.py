from . import personal_information as p
from app.personal_informacion import descripcion as d
def details_portfolio():
    json = dict()
    json['name'] = p.name
    json['profesiones'] = p.profesiones
    json['social_media'] = p.social_media
    json['descriptions'] = d.data()
    json['courses'] = p.courses
    json['works'] = p.works
    json['journals'] = p.journals
    return json