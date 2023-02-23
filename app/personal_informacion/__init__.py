from . import full_name as f
def details_portfolio():
    json = dict()
    json['name'] = f.data()
    print(json)
    return json