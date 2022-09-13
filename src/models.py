from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    phone = Column(String(25), nullable=False, unique=True)


class Info(Base):
    __tablename__ = 'information'
    id = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=True, unique=True, index=True)
    birthday = Column(String(20), nullable=True)
    address = Column(String(200), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)


Base.metadata.create_all(engine)
Base.metadata.bind = engine