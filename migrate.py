from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from run import create_app

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()
    manager.run()
        