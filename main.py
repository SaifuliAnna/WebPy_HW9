import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError
from src.repository import get_user, create_info, get_all_info, update_info, remove_info, remove_contact


parser = argparse.ArgumentParser(description='AddressBook APP')
parser.add_argument('--action', help='Command: create, update, list, remove, remove_user')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--phone')
parser.add_argument('--email')
parser.add_argument('--birthday')
parser.add_argument('--address')
parser.add_argument('--user')

arguments = parser.parse_args()
my_arg = vars(arguments)


action = my_arg.get('action')
_id = my_arg.get('id')
name = my_arg.get('name')
phone = my_arg.get('phone')
email = my_arg.get('email')
birthday = my_arg.get('birthday')
address = my_arg.get('address')
user = my_arg.get('user')


def main(user):
    match action:
        case 'create':
            create_info(email=email, birthday=birthday, address=address, user=user)
        case 'list':
            info = get_all_info(user)
            for i in info:
                print(i.id, i.email, i.birthday, i.address, i.user.phone)
        case 'update':
            i = update_info(_id=_id, email=email, birthday=birthday, address=address, user=user)
            print(i.id, i.email, i.birthday, i.address, i.user.phone)
        case 'remove':
            r = remove_info(_id=_id, user=user)
            print(f'Result: {bool(r)}')
        case 'remove_user':
            r = remove_contact(_id=_id, name=name)
            print(f'Result: {bool( r )}')


if __name__ == "__main__":
    user = get_user(name)
    name_n = input('name: ')
    main(user)