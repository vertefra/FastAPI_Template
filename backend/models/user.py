from tortoise.models import Model
from tortoise import fields


class User(Model):
    name = fields.TextField()
    username = fields.TextField(unique=True)
    password = fields.TextField()
    email = fields.TextField(unique=True)
