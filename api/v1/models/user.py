"""
Model to represent a user.
"""
from uuid import uuid4

from models.extensions import db


class User(db.Model):
    """
    User model
    """
    __tablename__ = "users"
    id = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    address = db.Column(db.String(60))
    phone1 = db.Column(db.String(30))
    phone2 = db.Column(db.String(60), nullable=True)

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.__dict__.update(kwargs)

    def as_dict(self):
        """Returns a dict with all the attributtes of a User instance
        """
        return {
            col.name: getattr(self, col.name)
            for col in self.__table__.columns
        }

    def save(self):
        """Save an user object to Database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete a user object from Database.
        """
        db.session.delete(self)
        db.session.commit()
