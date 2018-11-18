import sqlite3
from flag import flag


def init_admin(db):
    db.execute(
        "INSERT INTO users (username, password) "\
        "VALUES ('admin', '558ed230f85bafba20663dabd23d400d9181d5734735ab68eed193f7870bf1dd');"
    )
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
    init_admin(db)
    return db


def get_db():
    conn = sqlite3.connect('database.db')
    return init_db(conn)


if __name__ == "__main__":
    import sys
    if '--init' in sys.argv:
        db = get_db()
        init_db(db)
