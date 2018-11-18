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

table_map = {'users': USER_SQL}
