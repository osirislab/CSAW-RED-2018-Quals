import sqlite3
from flag import flag


def plant_flag(db):
    sql = "INSERT INTO flag_is_in_here (entry) VALUES (?);"
    s="this is garbage"
    for i in s.split():
        db.execute(sql, (i,))
    db.execute(sql, (flag,))
    db.commit()

def init_db(db):
    from sql_init import table_map
    current_tables = list(map(
        lambda x: x[0],
        db.execute('SELECT tbl_name FROM sqlite_master;').fetchall()
    ))
    for table, container in table_map.items():
        if table not in current_tables:
            db.execute(container.sql)
    db.commit()
    plant_flag(db)
    return db


def get_db():
    conn = sqlite3.connect('database.db')
    return init_db(conn)
