from sqlalchemy.sql import func

from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", back_populates="posts")

    def to_dict(self):
        return {
            'id': self.id,
            'author_id': self.user_id,
            'text': self.text,
            'created_at': self.created_at
        }

    def __repr__(self):
        return f"{self.id}: {self.text}"
