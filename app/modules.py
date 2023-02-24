from . import personal_information as p
from app.personal_informacion import details_portfolio as d
def details_portfolio():
    json = d()
    json['works'] = p.works
    json['journals'] = p.journals
    return json