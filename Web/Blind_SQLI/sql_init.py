class Struct:
    def __init__(self, **kwargs):
        for item, value in kwargs.items():
            self.__setattr__(item, value)  # self.$item = $value


USER_SQL = Struct(
    name='users',
    sql="""
    CREATE TABLE users (
    id INTEGER PRIMARY KEY, 
    username TEXT, 
    password TEXT
    );
    """
)

FLAG_TABLE = Struct(
    name='flag_is_in_here',
    sql="""
    CREATE TABLE flag_is_in_here (
    id INTEGER PRIMARY KEY,
    entry TEXT
    );
    """
)

table_map = {
    'users': USER_SQL,
    'user_submissions': SUBMISSION_SQL,
    'flag_is_in_here': FLAG_TABLE
}
