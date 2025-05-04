from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
import uuid
from datetime import datetime
from app import db  # Assuming you have a Flask app instance in app.py

class Mood(db.Model):
    __tablename__ = 'moods'
    mood_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    mood_name = db.Column(db.String(50))
    description = db.Column(db.Text)
    category = db.Column(db.String(50))
    score = db.Column(db.Numeric(3, 2))