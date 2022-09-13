from sqlalchemy.exc import SQLAlchemyError
from src.db import session
from src.models import User


def add_user(*args):
    name = input('name: ')
    phone = input('phone : ')
    try:
        new_user = User(name=name, phone=phone)
        session.add(new_user)
        session.commit()
    except SQLAlchemyError as err:
        print(err)


if __name__ == '__main__':
    add_user()
