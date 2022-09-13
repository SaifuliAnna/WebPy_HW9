from sqlalchemy import and_
from src.db import session
from src.models import User, Info


def get_user(name) -> User:
    user = session.query(User).filter(User.name == name).one()
    return user


def create_info(email, birthday, address, user):
    info = Info(email=email, address=address, birthday=birthday, user=user)
    session.add(info)
    session.commit()
    session.close()


def get_all_info(user) -> list[Info]:
    inform = session.query(Info).join(User).filter(Info.user == user).all()
    return inform


def update_info(_id, email, birthday, address, user) -> Info:
    info = session.query(Info).filter(and_(Info.user == user, Info.id == _id))
    info.update({'email': email, 'birthday': birthday, 'address': address})
    session.commit()
    session.close()
    return info.one()


def remove_info(_id, user) -> int:
    r = session.query(Info).filter(and_(Info.user == user, Info.id == _id)).delete()
    session.commit()
    session.close()
    return r


def remove_contact(_id, name):
    r = session.query(User).filter(and_(User.name == name, User.id == _id)).delete()
    session.commit()
    session.close()
    return r
