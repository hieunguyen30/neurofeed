from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # <-- load it into Flask

db = SQLAlchemy()
db.init_app(app)

from models import *  # or import individual models if separated

@app.route('/check_db')
def check_db():
    try:
        # Use the `text()` function to explicitly declare the SQL expression
        result = db.session.execute(text('SELECT 1'))
        return "Database is connected successfully!"
    except Exception as e:
        return f"Error connecting to the database: {e}"
