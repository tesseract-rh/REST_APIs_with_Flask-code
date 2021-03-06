import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # primary_key > unique value
    username = db.Column(db.String(80)) # 80 char long max
    password = db.Column(db.String(80))

    def __init__(self, username, password):
    #   self.id       <---- auto-generated by SQLAlchemy & auto-incremental as well
        self.username = username  # must match the db.Columns to be saved in the db
        self.password = password  # must match the db.Columns to be saved in the db

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    # query builder ^^^ > object;  ^column name ^argument

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    #                              ^^ col. name, defined in line 7
