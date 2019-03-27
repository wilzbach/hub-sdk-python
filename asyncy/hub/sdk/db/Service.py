# -*- coding: utf-8 -*-
from peewee import UUIDField, TextField, BooleanField
from playhouse.sqlite_ext import JSONField

from asyncy.hub.sdk.db.BaseModel import BaseModel


class Service(BaseModel):
    service_uuid = UUIDField(primary_key=True)
    name = TextField(index=True)
    alias = TextField(index=True, null=True)
    username = TextField()
    description = TextField(null=True)
    certified = BooleanField()
    public = BooleanField()
    topics = JSONField(null=True)
    state = TextField()
    configuration = JSONField()
    readme = TextField(null=True)



