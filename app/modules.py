from . import personal_information as p
def details_portfolio():
    json = dict()
    json['name'] = p.name
    json['profesiones'] = p.profesiones
    json['social_media'] = p.social_media
    json['descriptions'] = p.descriptions
    json['courses'] = p.courses
    json['works'] = p.works
    json['journals'] = p.journals
    return json