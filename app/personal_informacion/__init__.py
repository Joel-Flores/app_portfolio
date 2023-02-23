from . import services as s
def details_portfolio():
    json = dict()
    json['courses'] = s.data()
    return json