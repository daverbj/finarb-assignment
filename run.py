from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os 
import config
from models import db
def create_app():
    app = Flask(__name__)
    CORS(app)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config.from_object(config.DevelopmentConfig)
    db.init_app(app)
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    jwt = JWTManager(app)
    return app
if __name__ == "__main__":
    app = create_app()
    app.run()