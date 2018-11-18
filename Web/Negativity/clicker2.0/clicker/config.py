import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    SEED = os.getenv('RANDOM_SEED', 'lol_im_so_random')
    CLICKERS = {
        "base": {
            "value": 1,
            "price": 5
        },
        "momo": {
            "value": 5,
            "price": 10
        },
        "mgb": {
            "value": 10,
            "price": 1000
        },
        "profk": {
            "value": 100,
            "price": 10000
        },
        "bigj": {
            "value": 100,
            "price": 50000
        },
        "passion": {
            "value": 500,
            "price": 2000000
        },
        "hyper": {
            "value": 10000,
            "price": 2000000
        },
        "ghost": {
            "value": 100000,
            "price": 120000000
        },
        "tnek": {
            "value": 1000000,
            "price": 4000000000
        },
        "captiosus": {
            "value": 10000000,
            "price": 50000000000
        }
    }


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'DEVELOPMENT'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
admin_password = os.getenv('ADMIN_PASS', 'super_secret_admin_pass')
