from ..db import db
from ceos.auth.models import User

class Bucketlist(db.Model):

    __tablename__ = 'bucketlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )
    # created_by = db.relationship(User, backref=db.backref('bucket', lazy='joined'), lazy='select')
    created_by = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return "<Bucketlist: {}".format(self.name)

    def __init__(self, name, created_by):
        self.name = name
        self.created_by = created_by

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Bucketlist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
