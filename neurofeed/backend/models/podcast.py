from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
import uuid
from datetime import datetime
from app import db

class Podcast(db.Model):
    __tablename__ = 'podcasts'
    podcast_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    publisher = db.Column(db.String(255))
    language = db.Column(db.String(50))
    release_date = db.Column(db.Date)
    total_episodes = db.Column(db.Integer)
    explicit = db.Column(db.Boolean)
    podcast_url = db.Column(db.Text)