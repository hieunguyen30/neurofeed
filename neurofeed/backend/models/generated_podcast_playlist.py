from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
import uuid
from datetime import datetime
from app import db  # Assuming you have a Flask app instance in app.py

class GeneratedPodcastPlaylist(db.Model):
    __tablename__ = 'generated_podcast_playlists'
    playlist_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'))
    mood_id = db.Column(UUID(as_uuid=True), db.ForeignKey('moods.mood_id'))
    weather_id = db.Column(UUID(as_uuid=True), db.ForeignKey('weather_conditions.weather_id'))
    calendar_event_id = db.Column(UUID(as_uuid=True), db.ForeignKey('calendar_events.event_id'))
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())