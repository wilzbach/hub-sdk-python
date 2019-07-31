# -*- coding: utf-8 -*-
from storyhub.sdk.db.BaseModel import BaseModel

from peewee import BooleanField, TextField, UUIDField


class Service(BaseModel):
    service_uuid = UUIDField(primary_key=True)
    name = TextField(index=True)
    alias = TextField(index=True, null=True)
    username = TextField()
    description = TextField(null=True)
    certified = BooleanField()
    public = BooleanField()
    topics = TextField(null=True)
    state = TextField()
    configuration = TextField()
    readme = TextField(null=True)
    raw_data = TextField(index=False, null=False)
