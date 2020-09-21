from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User,Role,Comment,Pitch

app=create_app('development')

manager=Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

#use the manager shell decorator to access the shell on the command line
@manager.shell 
def make_shell_context():
    return dict(app=app, db=db,User = User, Role = Role,Comment=Comment,Pitch=Pitch)

@manager.command
def test():
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
if __name__=='__main__':
    manager.run()