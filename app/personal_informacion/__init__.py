from . import full_name as f, descripcion as d
def details_portfolio():
    json = dict()
    json['name'] = f.data()
    json['descriptions'] = d.data()
    return json