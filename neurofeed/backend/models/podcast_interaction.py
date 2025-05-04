from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
import uuid
from datetime import datetime
from app import db

class PodcastInteraction(db.Model):
    __tablename__ = 'podcast_interactions'
    interaction_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'))
    episode_id = db.Column(UUID(as_uuid=True), db.ForeignKey('episodes.episode_id'))
    action = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    listen_duration = db.Column(db.Integer)
    completed = db.Column(db.Boolean, default=False)