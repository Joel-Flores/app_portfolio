from . import personal_information as p
from app.personal_informacion import services as s
def details_portfolio():
    json = dict()
    json['name'] = p.name
    json['profesiones'] = p.profesiones
    json['social_media'] = p.social_media
    json['descriptions'] = p.descriptions
    json['courses'] = s.data()
    json['works'] = p.works
    json['journals'] = p.journals
    return json