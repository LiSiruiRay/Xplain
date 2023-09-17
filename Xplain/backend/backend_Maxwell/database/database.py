from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Transcripts(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    full_text = db.Column(db.Text(), nullable=False)
    summary = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

class TranscriptDetails(db.Model):
    __tablename__ = 'TranscriptionDetails'
    id = db.Column(db.Integer, primary_key = True)
    transcript_id = db.Column(db.Integer, db.ForeignKey('transcripts.id'))
    start = db.Column(db.Float, nullable=False)
    text = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    end = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"ID: {id}, Start: {self.start}, End: {self.end}"
