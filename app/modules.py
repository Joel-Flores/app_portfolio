from . import personal_information as p
from app.personal_informacion import full_name as f, profesiones as pr, social_media as s, descripcion as d
def details_portfolio():
    json = dict()
    json['name'] = f.data()
    json['profesiones'] = pr.data()
    json['social_media'] = s.data()
    json['descriptions'] = d.data()
    json['courses'] = p.courses
    json['works'] = p.works
    json['journals'] = p.journals
    return json