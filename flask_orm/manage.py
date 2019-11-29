from flask_migrate import MigrateCommand
from flask_script import Manager

from flask_orm.app import create_app

manager = Manager(create_app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
