import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Server
from brochure import app, db

MIGRATION_DIR = os.path.join('brochure', 'migrations')
DEBUG = os.getenv('DEBUG') == 'True'

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=5000))
manager.add_command("shell", Shell())

migrate = Migrate(app, db, directory=MIGRATION_DIR)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
