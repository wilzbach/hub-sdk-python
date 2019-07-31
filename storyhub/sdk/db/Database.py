# -*- coding: utf-8 -*-
from storyhub.sdk.db.BaseModel import BaseModel
from storyhub.sdk.db.Service import Service


class Database:
    def __init__(self, database_path: str):
        first_time = BaseModel.init(db_path=database_path)
        if first_time:
            BaseModel.create_tables([Service])

    def __enter__(self):
        return BaseModel.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        BaseModel.close()
