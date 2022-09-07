from src.db import session
from src.models import UserContact, UserInfo, ContactInfo
from sqlalchemy import update


def create_users_contacts(n_name, n_phone=None):
    us_cont = UserContact(
        name=n_name,
        phone=n_phone
    )
    session.add(us_cont)
    session.commit()


def create_users_info(n_name, n_email=None, n_birthday=None, n_address=None):
    us_info = UserInfo(
        name=n_name,
        email=n_email,
        birthday=n_birthday,
        address=n_address
    )
    session.add(us_info)
    session.commit()


# def create_relationship():
#     contacts = session.query(UserContact).all()
#     inform = session.query(UserInfo).all()
#
#     for contact, info in contacts, inform:
#         rel = ContactInfo(info_id=contact.id, contact_id=contact.id)
#         session.add(rel)
#     session.commit()


def update_contacts(n_id, n_name, n_phone):
    session.execute(update(UserContact).where(UserContact.id == n_id).
                    values(name=n_name, phone=n_phone))
    session.commit()


def update_contact_phone(n_name, n_phone):
    session.execute(update(UserContact).where(UserContact.name == n_name).
                    values(phone=n_phone))
    session.commit()


def update_contact_name(n_name, n_phone):
    session.execute(update(UserContact).where(UserContact.phone == n_phone).
                    values(name=n_name))
    session.commit()


def update_name_id(n_id, n_name):
    session.execute(update(UserContact).where(UserContact.id == n_id).
                    values(name=n_name))
    session.commit()


def update_info(n_id, n_name, n_email, n_birthday, n_address):
    session.execute(update(UserInfo).where(UserInfo.id == n_id).
                    values(name=n_name, email=n_email, birthday=n_birthday, address=n_address))
    session.commit()


def update_email(n_name, n_email):
    session.execute(update(UserInfo).where(UserInfo.name == n_name).
                    values(email=n_email))
    session.commit()


def update_birthday(n_name, n_birthday):
    session.execute(update(UserInfo).where(UserInfo.name == n_name).
                    values(birthday=n_birthday))
    session.commit()


def update_address(n_name, n_address):
    session.execute(update(UserInfo).where(UserInfo.name == n_name).
                    values(address=n_address))
    session.commit()


def show_all(class_name):
    contacts = session.query(class_name).all()
    for c in contacts:
        print(vars(c))


def remove(ex, n_ex, class_name):
    session.query(class_name).filter(f'{class_name}.{ex}' == n_ex).delete()
    session.commit()


def remove_cont(n_name):
    session.query(UserContact).filter(UserContact.n_name == n_name).delete()
    session.commit()


# if __name__ == '__main__':
#     create_users_contacts('Ann', '+380967776655')
#     create_users_info(n_name, n_email, n_birthday, n_address)
    # create_relationship()
    # update_contacts(n_id, n_name, n_phone)
    # update_contact_phone(n_name, n_phone)
    # update_contact_name(n_name, n_phone)
    # update_name_id(n_id, n_name)
    # update_info(n_id, n_name, n_email, n_birthday, n_address)
    # update_email(n_name, n_email)
    # update_birthday(n_name, n_birthday)
    # update_address(n_name, n_address)
    # show_all(class_name)
    # remove(ex, n_ex, class_name)
    # remove_cont(n_name)








