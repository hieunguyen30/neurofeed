from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
import uuid
from datetime import datetime
from app import db  # Assuming you have a Flask app instance in app.py

db = SQLAlchemy()

class WeatherCondition(db.Model):
    __tablename__ = 'weather_conditions'
    weather_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'))
    timestamp = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    condition = db.Column(db.String(50))
    location = db.Column(db.String(100))
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    
    