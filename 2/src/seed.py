from src.db import session
from src.models import NameContact, PhoneContact, EmailContact, NameContactPhone, NameContactEmail
from sqlalchemy import update


def create_names_contacts(n_name, n_birthday=None, n_address=None):
    contacts_for_table = NameContact(
        first_name=n_name,
        birthday=n_birthday,
        address=n_address
    )
    session.add(contacts_for_table)
    session.commit()


def create_phones_contacts(n_phone):
    phones_for_table = PhoneContact(
        phone=n_phone
    )
    session.add(phones_for_table)
    session.commit()


def create_emails_contacts(n_email):
    emails_for_table = EmailContact(
        email=n_email
    )
    session.add(emails_for_table)
    session.commit()


def update_contact(n_id, n_name, n_birthday, n_address):
    session.execute(update(NameContact).
                    where(NameContact.id == n_id).
                    values(name=n_name, birthday=n_birthday, address=n_address))
    session.commit()


def update_name(n_id, n_name):
    session.execute(update(NameContact).
                    where(NameContact.id == n_id).
                    values(name=n_name))
    session.commit()


def update_birthday(n_id, n_birthday):
    session.execute(update(NameContact).
                    where(NameContact.id == n_id).
                    values(birthday=n_birthday))
    session.commit()


def update_address(n_id, n_address):
    session.execute(update(NameContact).
                    where(NameContact.id == n_id).
                    values(address=n_address))
    session.commit()


def update_phone(p_id, n_phone):
    session.execute(update(PhoneContact).where(PhoneContact.id == p_id).
                    values(phone=n_phone))
    session.commit()


def update_email(e_id, n_email):
    session.execute(update(EmailContact).where(EmailContact.id == e_id).
                    values(email=n_email))
    session.commit()


def show_all(class_name):
    contacts = session.query(class_name).all()
    for c in contacts:
        print(vars(c))


def remove(n_id, class_name):
    session.query(class_name).filter(class_name.id == n_id).delete()
    session.commit()


# if __name__ == '__main__':
    # create_names_contacts('Ann')
    # create_phones_contacts('+38096503****')
    # create_emails_contacts('ann@gmail.com')
    # remove(1, PhoneContact)
    # show_all(NameContact)
    # update_email(2, 'ann1@gmail.com')
    # update_birthday(1, '18.10.1990')
