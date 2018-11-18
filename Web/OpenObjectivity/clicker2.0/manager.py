from eventlet import wsgi
import eventlet

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from clicker import blueprint
from clicker.app import create_app, db, uuid_rand
from clicker.model import auth
from clicker.model import user
from clicker.model import blacklist
from clicker.model import user_click
from clicker.service import user as user_service

app = create_app('prod')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


def sync_rand():
    for _ in range(db.session.query(auth.Auth).count()):
        uuid_rand.getrandbits(128)


@manager.command
def run():
    sync_rand()
    wsgi.server(eventlet.listen(('', 80)), app, log_output=False)


@manager.command
def seed():
    "Add seed data to the database."
    user_service.new_admin()


if __name__ == '__main__':
    manager.run()
