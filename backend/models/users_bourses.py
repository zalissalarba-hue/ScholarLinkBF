from models import db
from datetime import datetime



class UsersBourses(db.Model):
    __tablename__ = "users_bourses"

    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), primary_key=True)
    bourse_id = db.Column(db.String(36), db.ForeignKey("bourses.id"), primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<UsersBourses user_id={self.user_id} bourse_id={self.bourse_id} datetime={self.datetime}>"
