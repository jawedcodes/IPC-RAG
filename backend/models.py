# models.py
from backend.database import db
from datetime import datetime

class QueryLog(db.Model):
    __tablename__ = "query_logs"

    id = db.Column(db.Integer, primary_key=True)
    query_text = db.Column(db.Text, nullable=False)
    final_answer = db.Column(db.Text, nullable=False)
    retrieved_sections = db.Column(db.Text, nullable=True)
    confidence_score = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, query_text, final_answer):
        self.query_text = query_text
        self.final_answer = final_answer
    
