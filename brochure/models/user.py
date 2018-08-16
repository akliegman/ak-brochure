from sqlalchemy import exc
from sqlalchemy.sql import func

from brochure import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, server_default=func.now(),
                           nullable=False)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email = db.Column(db.String(64))
    phone = db.Column(db.String(16), nullable=True)

    def __init__(self, **user):
        super(User, self).__init__(**user)

    def __repr__(self):
        return u'<User {}>'.format(self.email)

    def to_dict(self):
        """Return a dictionary representation of this model.
        """
        columns = self.__table__.columns.keys()
        return {key: getattr(self, key) for key in columns}

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            db.session.rollback()
            raise err

    @classmethod
    def get_by_id(cls, user_id):
        return db.session.query(User).filter(
            User.id == user_id
        ).first()
