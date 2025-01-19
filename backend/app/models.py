from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    
    def __repr__(self):
        return f"Video('{self.title}', '{self.url}')"
