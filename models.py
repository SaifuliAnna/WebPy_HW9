from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table


Base = declarative_base()

# таблиця для зв'язку many-to-many між таблицями names_contacts і phones_contacts
name_m2m_phone = Table(
    "names_contacts_m2m_phones_contacts",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("name_contact", Integer, ForeignKey("names_contacts.id")),
    Column("phone_contact", Integer, ForeignKey("phones_contacts.id"))
)


# таблиця для зв'язку many-to-many між таблицями names_contacts і emails_contacts
name_m2m_email = Table(
    "names_contacts_m2m_emails_contacts",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("name_contact", Integer, ForeignKey("names_contacts.id")),
    Column("email_contact", Integer, ForeignKey("emails_contacts.id"))
)


# Таблиця names_contacts
class NameContact(Base):
    __tablename__ = "names_contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    second_name = Column(String(50), nullable=True)
    birthday = Column(String(50), nullable=True)
    address = Column(String(250), nullable=True)
    records = relationship("Record", cascade="all, delete", backref="name_contact")
    phones_contacts = relationship("PhoneContact", secondary=name_m2m_phone, backref="names_contacts")
    emails_contacts = relationship("EmailContact", secondary=name_m2m_email, backref="names_contacts")


# Таблиця phones_contacts
class PhoneContact(Base):
    __tablename__ = "phones_contacts"
    id = Column(Integer, primary_key=True)
    phone = Column(String(25), nullable=False, unique=True)


# Таблиця phones_contacts
class EmailContact(Base):
    __tablename__ = "emails_contacts"
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=True, unique=True)


# Таблиця records, де зберігатимуться записи для конкретної справи з таблиці notes - зв'язок one-to-one, поле note_id
class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    description = Column(String(150), nullable=False)
    names_contacts_id = Column(Integer, ForeignKey(NameContact.id, ondelete="CASCADE"))


