import sqlite3

con = sqlite3.connect('database/database.sqlite3')
cursor = sqlite3.Cursor(con)


class LoginNotFoundError(Exception):
    pass


class LoginInTableError(Exception):
    pass


def add_login(login):
    try:
        cursor.execute(f'''INSERT INTO users (login) VALUES ('{login}')''')
        con.commit()
    except sqlite3.IntegrityError as e:
        raise LoginInTableError


def add_data(password, notes, login):
    if login in map(lambda x: x[0], cursor.execute('SELECT login FROM users').fetchall()):
        loginID = cursor.execute(f'SELECT ID FROM users WHERE login = "{login}"').fetchone()[0]
        cursor.execute(f'''INSERT INTO data (password, notes, loginID) VALUES ('{password}', '{notes}', '{loginID}')''')
        con.commit()
    else:
        raise LoginNotFoundError


def delete_data(login):
    if login in map(lambda x: x[0], cursor.execute('SELECT login FROM users').fetchall()):
        loginID = cursor.execute(f'SELECT ID FROM users WHERE login = "{login}"').fetchone()[0]
        cursor.execute(f'DELETE FROM data WHERE loginID = {loginID}')
        con.commit()
    else:
        raise LoginNotFoundError


def delete_login(login):
    if login in map(lambda x: x[0], cursor.execute('SELECT login FROM users').fetchall()):
        delete_data(login)
        cursor.execute(f'DELETE FROM users WHERE login = "{login}"')
        con.commit()
    else:
        raise LoginNotFoundError


def show_data(login):
    loginID = cursor.execute(f'SELECT ID FROM users WHERE login = "{login}"').fetchone()[0]
    return (cursor.execute(f'SELECT login FROM users WHERE ID = "{loginID}"').fetchone()[0],
            cursor.execute(f'SELECT password, notes FROM data WHERE loginID = "{loginID}"').fetchall())


def show_all_data():
    logins = tuple(map(lambda x: x[0], cursor.execute(f'SELECT login FROM users').fetchall()))
    print(logins)
    return [show_data(el) for el in logins]


def delete_ALL():
    cursor.execute('DELETE FROM users')
    cursor.execute('DELETE FROM data')
    con.commit()

