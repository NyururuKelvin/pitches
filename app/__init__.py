from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES

bootstrap=Bootstrap()
db=SQLAlchemy()
photos = UploadSet('photos',IMAGES)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):

    app=Flask(__name__)
    #initialize app extentions
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app,photos)

    #regster your blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    #register your configuration files
    app.config.from_object(config_options[config_name])
    
    return app
