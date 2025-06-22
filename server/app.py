from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from server.controllers.auth_controller import auth_bp
    from server.controllers.appearance_controller import appearance_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.guest_controller import guest_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(appearance_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(guest_bp)
    
    from server.models import user, guest, episode, appearance  
    return app
