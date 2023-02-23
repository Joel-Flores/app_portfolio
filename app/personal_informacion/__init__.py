from . import descripcion as d
def details_portfolio():
    json = dict()
    
    json['descriptions'] = d.data()
    return json