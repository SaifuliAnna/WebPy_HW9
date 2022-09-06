from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db import Base


class NameContact(Base):
    __tablename__ = "names_contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    birthday = Column('birthday', String(50), nullable=True)
    address = Column('address', String(250), nullable=True)
    phones_contacts = relationship("PhoneContact", secondary="names_to_phones", back_populates="names_contacts")
    emails_contacts = relationship("EmailContact", secondary="names_to_emails", back_populates="names_contacts")


# Таблиця phones_contacts
class PhoneContact(Base):
    __tablename__ = "phones_contacts"
    id = Column(Integer, primary_key=True)
    phone = Column('phone', String(25), nullable=False, unique=True)
    names_contacts = relationship("NameContact", secondary="names_to_phones", back_populates="phones_contacts")


class EmailContact(Base):
    __tablename__ = "emails_contacts"
    id = Column(Integer, primary_key=True)
    email = Column('email', String(50), nullable=True, unique=True)
    names_contacts = relationship("NameContact", secondary="names_to_emails", back_populates="emails_contacts")


class NameContactPhone(Base):
    __tablename__ = "names_to_phones"
    id = Column(Integer, primary_key=True)
    names_contacts_id = Column('names_contacts_id', ForeignKey('names_contacts.id', ondelete='CASCADE'))
    phones_contacts_id = Column('phones_contacts_id', ForeignKey('phones_contacts.id', ondelete='CASCADE'))


class NameContactEmail(Base):
    __tablename__ = "names_to_emails"
    id = Column(Integer, primary_key=True)
    names_contacts_id = Column('names_contacts_id', ForeignKey('names_contacts.id', ondelete='CASCADE'))
    emails_contacts_id = Column('emails_contacts_id', ForeignKey('emails_contacts.id', ondelete='CASCADE'))