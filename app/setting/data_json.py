from app.personal_informacion import social_media

def data():
    json = dict()
    json['social_media'] = social_media.data()
    return json