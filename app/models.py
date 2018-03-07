from app import db
from datetime import datetime

items = db.Table('items',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('dish_id', db.Integer, db.ForeignKey('dish.id'), primary_key=True)
)


class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index = True, unique = True)
	count = db.Column(db.Integer)
	price = db.Column(db.Float(precision = 3))

	def __repr__(self):
		return '<Item {} {} {}>'.format(self.name, self.count, self.price)

class Dish(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index = True, unique = True)
	price = db.Column(db.Float(precision = 3))
	items = db.relationship('Item', secondary=items, lazy='subquery', backref=db.backref('dishes', lazy=True))
	orders = db.relationship('Order', backref='dish', lazy='dynamic')

	def __repr__(self):
		return '<Dish {} {}>'.format(self.name, self.price)

class Order(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	def __repr__(self):
		return '<Order {} {}>'.format(self.dish_id, self.timestamp)

class Cash(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	cash = db.Column(db.Float(precision = 3))

	def __repr__(self):
		return '<Cash {}>'.format(self.cash)