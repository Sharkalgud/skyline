from app.models import Cash, Dish, Item, Order
from app import db


class DishCom():
	def get_all_dishes(self):
		return Dish.query.all()
	def add_dish(self, name, ingrd, price):
		items = ItemCom().get_all_items()
		d = Dish()
		d.name = name
		d.price = float(price)
		itm_list = ingrd.split(',')
		for i in itm_list:
			for it in items:
				if i == it.name:
					d.items.append(it)
		db.session.add(d)
		db.session.commit()

	def edit_dish(self, name, ingrd, price):
		items = ItemCom().get_all_items()
		d = Dish.query.filter_by(name = name)[0]
		d.name = name
		itm_list = ingrd.split(',')[:-1]
		d.items = []
		for i in itm_list:
			for it in items:
				if i == it.name:
					d.items.append(it)
		d.price = price
		db.session.commit()

	def remove_dish(self, name):
		d = Dish.query.filter_by(name = name)[0]
		db.session.delete(d)
		db.session.commit()
class ItemCom():
	def get_all_items(self):
		return Item.query.all()

	def reduce_item_count(self, item, amount):
		item.count -= amount
		db.session.commit()

	def add_item_count(self, item, amount):
		item.count += amount
		db.session.commit()

	def add_item(self, name, amount, price):
		i = Item()
		i.name = name
		i.count = int(amount)
		i.price = float(price)
		db.session.add(i)
		db.session.commit()

	def edit_item(self, name, amount, price):
		i = Item.query.filter_by(name = name)[0]
		i.name = name
		i.count = float(amount)
		i.price = float(price)
		db.session.commit()

	def remove_item(self, name):
		i = Item.query.filter_by(name = name)[0]
		db.session.delete(i)
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
	def reduce_cash(self, amount):
		c = Cash.query.all()[0]
		c.cash -= amount
		db.session.commit()
	def add_cash(self, amount):
		c = Cash.query.all()[0]
		c.cash += amount
		db.session.commit()