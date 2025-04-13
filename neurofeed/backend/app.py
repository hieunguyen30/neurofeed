from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config.settings import Config
import os


load_dotenv()

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)

    # --- Load Configuration from Environment Variables ---
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    if not app.config['SECRET_KEY']:
        raise ValueError("No SECRET_KEY set for Flask application")

    app.config['GOOGLE_CLIENT_ID'] = os.environ.get('GOOGLE_CLIENT_ID')
    app.config['GOOGLE_CLIENT_SECRET'] = os.environ.get('GOOGLE_CLIENT_SECRET')
    app.config['GOOGLE_REDIRECT_URI'] = os.environ.get('GOOGLE_REDIRECT_URI')
    app.config['SCOPES'] = ['https://www.googleapis.com/auth/calendar.readonly']
    # Validate essential Google Config
    if not app.config['GOOGLE_CLIENT_ID'] or not app.config['GOOGLE_CLIENT_SECRET'] or not app.config['GOOGLE_REDIRECT_URI']:
         raise ValueError("Missing required Google OAuth configuration in environment variables.")

    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Register blueprints from controllers
    from controllers.auth_controller import auth_bp
    from controllers.music_controller import music_bp
    from controllers.recommendation_controller import recommendations_bp
    from controllers.user_controller import user_profile_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(music_bp, url_prefix='/api/v1/music')
    app.register_blueprint(recommendations_bp, url_prefix='/api/v1/recommendations')
    app.register_blueprint(user_profile_bp, url_prefix='/api/v1/profile')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 