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

SUBMISSION_SQL = Struct(
    name='user_submissions',
    sql="""
    CREATE TABLE user_submissions (
    id INTEGER PRIMARY KEY,
    content TEXT,
    discription TEXT,
    assignment_name TEXT,
    class_name TEXT
    );"""
)



table_map = {'users':USER_SQL,'user_submissions':SUBMISSION_SQL}
