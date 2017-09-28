from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')
    # many-to-one relationship >> items is a list
    # lazy='dynamic':
    # do NOT go into the 'items' table and create an object for each item yet

    def __init__(self, name):
        self.name = name

    def json(self):
    #   return {'name': self.name, 'items': [item.json() for item in self.items]}
    #   self.items >> list of items

        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
    #   lazy='dynamic':                                                         ^^^^^
    #   self.items >> query builder; .all -- retrieve all of the items in that table
    #   until we call 'def json', we're not looking into the table!
    #   BUT everytime we call 'def json', we have to go into the table!!

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
