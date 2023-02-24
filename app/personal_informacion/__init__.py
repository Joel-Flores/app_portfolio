from . import full_name as f, descripcion as d, services as s
def details_portfolio():
    json = dict()
    json['name'] = f.data()
    json['descriptions'] = d.data()
    json['courses'] = s.data()
    return json