from mongoengine import Document, StringField, DateField


class MemberDocument(Document):
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    gender = StringField(max_length=10, required=True)
    date_of_birth = DateField(required=True)
    email = StringField(max_length=100, required=True, unique=True)

    meta = {"collection": "Member"}
