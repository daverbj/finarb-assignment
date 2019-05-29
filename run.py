from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os 
import config
def create_app(config_filename):
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    """ app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True """
    app.config.from_object(config.DevelopmentConfig)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)