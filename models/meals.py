from mongoengine import Document, StringField, FloatField


class Meals(Document):
    name = StringField(required=True)
    description = StringField()
    price = FloatField()
    image_url = StringField()