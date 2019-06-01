from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
import config
from models import db


def create_app():
    app = Flask(__name__, static_folder="static")

    @app.route('/public')
    def serve_page():
        return "hello"
    CORS(app)
    SWAGGER_URL = '/docs'  # URL for exposing Swagger UI (without trailing '/')
    # Our API url (can of course be a local resource)
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(
        # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        SWAGGER_URL,
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Test application"
        },
        # oauth_config={ # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        # 'clientId': "your-client-id",
        # 'clientSecret': "your-client-secret-if-required",
        # 'realm': "your-realms",
        # 'appName': "your-app-name",
        # 'scopeSeparator': " ",
        # 'additionalQueryStringParams': {'test': "hello"}
        # }
    )
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config.from_object(config.DevelopmentConfig)
    db.init_app(app)
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    jwt = JWTManager(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")
