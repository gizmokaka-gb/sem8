import json

# BD = [12345,True, '17 марта', {'Миша': [8888888,7777777]}]
# def load():
#     fname = 'BD.json'
#     with open(fname, 'r', encoding = 'utf-8') as fh:
#         BD_local = json.load(fh)
#     print('БД успешно загружена')
#     return BD_local
#
# def save():
#      with open('BD.json', 'w', encoding = 'utf-8') as fh:
#         fh.write(json.dumps(BD,
#                             ensure_ascii=False))
#      print('БД успешно сохранена')
#
# save()
#
# BDnew = load()
# print(BDnew)

import json

db = 'phone_book.txt'
welcome = 'Enter command: 1 - read and show | 2 - add record | 3 - search | 4 - init DB | q - Quit\n'
phone_book = {
    'Миша': {'phone': ['55555', '66666'], 'birthday': '11-02-2001', 'e-mail': 'afdaf@asdf.ru'},
    'Паша': {'phone': ['111111', '44444'], 'birthday': '14-02-1998', 'e-mail': 'afsfsee@asdf.ru'}
}

def print_book(book):
    for k, v in book.items():
        print(k, ' - ', end=' | ')
        for i, j in v.items():
            print(i, j, end=' | ')
        print()

# def init_db(path, db):
#     with open(path,'w') as database:#
#       for i in db:
#             database.write(str(*i))#
#             print(type(i))
#     with open('BD.json', 'w', encoding='utf=8') as fh:#
#       fh.write(json.dumps(BD, ensure_ascii=False))
#     print('ss')

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)
    elif action == '2':
        print(action, '->', db)
    elif action == '3':
        print(action, '->', db)
    elif action == '4':
        init_db(db, phone_book)