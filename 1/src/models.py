from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db import Base


class UserContact(Base):
    __tablename__ = "users_contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column('phone', String(25), nullable=True)
    users_info = relationship('UserInfo', secondary='contacts_to_info', back_populates='users_contacts')


class UserInfo(Base):
    __tablename__ = "users_info"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column('email', String(50), nullable=True)
    birthday = Column('birthday', String(50), nullable=True)
    address = Column('address', String(250), nullable=True)
    users_contacts = relationship('UserContact', secondary='contacts_to_info', back_populates='users_info')


class ContactInfo(Base):
    __tablename__ = 'contacts_to_info'
    id = Column(Integer, primary_key=True)
    contacts_id = Column('contacts_id', ForeignKey("users_contacts.id", ondelete='CASCADE'))
    info_id = Column('info_id', ForeignKey("users_info.id", ondelete='CASCADE'))



