from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
import uuid
from datetime import datetime
from app import db  # Assuming you have a Flask app instance in app.py

class ArticleInteraction(db.Model):
    __tablename__ = 'article_interactions'
    interaction_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'))
    article_id = db.Column(UUID(as_uuid=True), db.ForeignKey('articles.article_id'))
    action = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    read_duration = db.Column(db.Integer)
    scroll_depth = db.Column(db.Integer)