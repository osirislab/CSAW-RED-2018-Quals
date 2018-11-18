#import sqlite3
from flag import flag
import pymysql.cursors


def get_db():
    return pymysql.connect(
        host='localhost',
        user='red_user',
        passwd='password',
        db='the_db_you_are_looking_for',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


def plant_flag(db):
    sql = "INSERT INTO its_in_here (entry) VALUES (?);"
    db.execute(sql, (flag,))
    db.commit()

def init_db(db):
    from sql_init import table_map
    with db.cursor() as cursor:
        for table in table_map:
            cursor.execute('TRUNCATE TABLE {}'.format(table))
            cursor.commit()
        cursor.close()
    with db.cursor() as cursor:
        for table, sql in table_map.items():
            cursor.execute(sql)
            cursor.commit()
        plant_flag(cursor)
        cursor.close()
    return db


if __name__ == "__main__":
    import sys
    if '--init' in sys.argv:
        db = get_db()
        init_db(db)
