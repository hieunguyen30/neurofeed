from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
import uuid
from datetime import datetime
from app import db  # Assuming you have a Flask app instance in app.py

class Episode(db.Model):
    __tablename__ = 'episodes'
    episode_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    podcast_id = db.Column(UUID(as_uuid=True), db.ForeignKey('podcasts.podcast_id'))
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    duration = db.Column(db.Integer)
    release_date = db.Column(db.Date)
    explicit = db.Column(db.Boolean)
    audio_url = db.Column(db.Text)
    transcript = db.Column(db.Text)
    episode_href = db.Column(db.Text)
    episode_uri = db.Column(db.Text)