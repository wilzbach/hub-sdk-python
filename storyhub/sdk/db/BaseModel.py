# -*- coding: utf-8 -*-
import os

from peewee import Model, SqliteDatabase

_db = SqliteDatabase(None)
_initialised = False


class BaseModel(Model):
    class Meta:
        database = _db

    @classmethod
    def connect(cls):
        _db.connect(reuse_if_open=True)
        return _db

    @classmethod
    def init(cls, db_path: str):
        """
        Initialises the SQLite database as "hub_cache.sqlite" under db_path.

        :return: True if initialised for the first time, false otherwise
        """
        global _initialised

        if not _initialised:
            _db.init(os.path.join(db_path, "hub_cache.sqlite"))
            _initialised = True
            return True

        return False

    @classmethod
    def create_tables(cls, models: [Model]):
        _db.create_tables(models)

    @classmethod
    def close(cls):
        _db.close()
