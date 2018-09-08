import sqlite3
from flag import flag


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
    return db


def get_db():
    conn = sqlite3.connect('database.db')
    return init_db(conn)


if __name__ == "__main__":
    print(1)
    import os
    if os.path.isfile('./database.db'):
        os.remove('./database.db')
    db = get_db()
    init_db(db)
    db.execute(
        f"""
        INSERT INTO users (username, password)
        VALUES ('admin', '{flag}');
        """
    )
    db.commit()
