from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
import uuid
from datetime import datetime
from app import db  # Assuming you have a Flask app instance in app.py

class MoodInput(db.Model):
    __tablename__ = 'mood_inputs'
    mood_input_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'))
    timestamp = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    mood_text = db.Column(db.String(255))
    mood_id = db.Column(UUID(as_uuid=True), db.ForeignKey('moods.mood_id'))