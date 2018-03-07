from app import db
from app.models import Item, Dish, Order, Cash

#clear out all databases
items = Item.query.all()
dishes = Dish.query.all()
orders = Order.query.all()
cash = Cash.query.all()

for i in items: db.session.delete(i)
for d in dishes: db.session.delete(d)
for o in orders: db.session.delete(o)
for c in cash: db.session.delete(c)

db.session.commit()

#add dummy data
ingredients = [['Beef', 10, 15],
			   ['Bacon', 10, 10],
			   ['Sausage', 10, 5],
			   ['Lettuce', 10, 3],
			   ['Tomato', 10, 4],
			   ['Potato', 10, 2],
			   ['Pepper', 10, 3],
			   ['Onion', 10, 4],
			   ['Garlic', 10, 25],
			   ['Plantain', 10, 50],
			   ['Bread', 10, 10],
			   ['Cheese', 10, 25],
			   ['Mustard', 10, 20],
			   ['Relish', 10, 15]]
dishes = [['Cheeseburger w/ Fries', 18.20, ['Beef', 'Lettuce', 'Tomato', 'Bread', 'Bacon', 'Cheese', 'Potato']],
		  ['Hot Dog w/ Fries', 3.56, ['Sausage', 'Relish', 'Bread', 'Pepper', 'Onion', 'Mustard', 'Potato']],
		  ['Pizza Pot Pie', 25.50, ['Sausage', 'Pepper', 'Tomato', 'Bread', 'Garlic']],
		  ['Italian Beef w/ Fries', 11.85, ['Beef', 'Onion', 'Pepper', 'Bread', 'Potato']],
		  ['Jibarito', 5.95, ['Beef', 'Lettuce', 'Tomato', 'Plantain', 'Onion', 'Garlic']]]

ingred_obj = {}
dish_obj = []

for i in ingredients:
	ingred_obj[i[0]] = Item(name = i[0], count = i[1], price = 15.00)

for d in dishes:
	dish = Dish(name = d[0], price = d[1])
	for i in d[2]: dish.items.append(ingred_obj[i])
	dish_obj.append(dish)

for i in ingred_obj.values():
	db.session.add(i)

for d in dish_obj:
	db.session.add(d)

c = Cash(cash = 50000)
db.session.add(c)

db.session.commit()