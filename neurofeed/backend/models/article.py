from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
import uuid
from datetime import datetime
from app import db  # Assuming you have a Flask app instance in app.py


class Article(db.Model):
    __tablename__ = 'articles'
    article_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    content = db.Column(db.Text)
    source = db.Column(db.String(255))
    language = db.Column(db.String(50))
    published_at = db.Column(db.DateTime)
    category = db.Column(db.String(100))
    article_url = db.Column(db.Text)
    summary = db.Column(db.Text)
    keywords = db.Column(ARRAY(db.Text))