#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by Lipson on 19-11-29.
# email to LipsonChan@yahoo.com
#
import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, UniqueConstraint, Index
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_test.config import Config

engine = create_engine(Config.DB_URI, convert_unicode=True)
db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))
Base = declarative_base()
Base.query = db.query_property()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(256))
    email = Column(String(120))
    created = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
    # update_time = Column(DateTime, server_default=func.current_timestamp(), server_onupdate=func.current_timestamp())
    # update_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.email = email
        self.password = password

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

    def __repr__(self):
        return '<User %r>' % (self.name)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    body = Column(String(4096))
    author_id = Column(Integer, ForeignKey('users.id'))
    created = Column(DateTime, server_default=func.now())
    # update_time = Column(DateTime, server_default=func.now(), onupdate=True)
    update_time = Column(DateTime, server_default=func.now(), server_onupdate=func.now())

    def __init__(self, title=None, body=None, author_id=None):
        self.title = title
        self.body = body
        self.author_id = author_id

    def __repr__(self):
        return '<Post %r>' % (self.title)


def init_db():
    # import flask_test.orms
    # user = flask_test.orms.User()
    Base.metadata.create_all(bind=engine)


__all__ = [
    'User',
    'Post',
    'db',
    'Base',
    'init_db',
]