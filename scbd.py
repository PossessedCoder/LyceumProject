import sqlite3

con = sqlite3.connect('database/database.sqlite3')
cursor = sqlite3.Cursor(con)

print(cursor.execute('''SELECT login, password, notes
FROM users
JOIN data ON ID = loginID''').fetchall())


def add_login(login):
    pass


def add_data(password, notes, login):
    pass


def delete_data(password, notes, login):
    pass


def delete_login(login):
    pass


def show_data(login):
    return cursor.execute('SELECT login, password, notes FROM users JOIN data ON ID = loginID').fetchall()
