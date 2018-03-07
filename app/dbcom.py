from app.models import Cash, Dish, Item, Order
from app import db


class DishCom():
	def get_all_dishes(self):
		return Dish.query.all()
class ItemCom():
	def get_all_items(self):
		return Item.query.all()
	def reduce_item_count(self, item, amount):
		item.count -= amount
		db.session.commit()
class OrderCom():
	def get_all_orders(self):
		return Order.query.all()
	def add_order(self, dish_name):
		d = Dish.query.filter_by(name = dish_name).first()
		o = Order(dish = d)
		db.session.add(o)
		db.session.commit()
class CashCom():
	def get_cash(self):
		return Cash.query.all()[0].cash
	def reduced_cash(self, amount):
		c = Cash.query.all()[0]
		c.cash -= amount
		db.session.commit()
	def add_cash(self, amount):
		c = Cash.query.all()[0]
		c.cash += amount
		db.session.commit()