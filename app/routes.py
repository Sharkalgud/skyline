from app import app
from app.models import Item, Dish, Order
from app.dbcom import DishCom, ItemCom, CashCom, OrderCom
from app.forms import LoginForm, AddDishForm
from flask import render_template, flash, redirect, session, request

cash = 50000

dishcom = DishCom()
itemcom = ItemCom()
cashcom = CashCom()
ordercom = OrderCom()

def out_of_stock(d):
	for i in d.items:
		if int(i.count) <= 0 :
			return True
	return False

@app.route('/', methods = ['GET', 'POST'])
def home_page():
	form = LoginForm()
	if form.validate_on_submit():
		session['username'] = form.email.data[:form.email.data.index('@')]
		return redirect('/menu')
	return render_template('index.html', form = form)

@app.route('/financial')
def get_cash():
	cash = cashcom.get_cash()
	orders = ordercom.get_all_orders()
	return render_template('financial.html', cash = cash, orders = orders, user = session['username'])

@app.route('/menu')
def get_menu():
	dishes =  dishcom.get_all_dishes()
	return render_template('menu.html', dishes = dishes, user = session['username'])

@app.route('/menu', methods = ['POST'])
def get_menu_post():
	dishes = dishcom.get_all_dishes()
	price = 0.0
	for d in dishes:
		amount = int(request.form[d.name])
		for i in range(amount):
			if out_of_stock(d):
				flash('{} is out of stock'.format(d.name))
			else:
				price += d.price
				for i in d.items:
					itemcom.reduce_item_count(i, 1)
				ordercom.add_order(d.name)
	cashcom.add_cash(price)
	return render_template('menu.html', dishes = dishes, user = session['username'])
@app.route('/inventory')
def get_inventory():
	items = itemcom.get_all_items()
	legend = 'Inventory'
	count = [i.count for i in items]
	labels = [i.name for i in items]
	return render_template('inventory.html', items = items, user = session['username'], values = count, labels = labels, legend = legend)

@app.route('/inventory', methods = ['POST'])
def get_inventory_post():
	items = itemcom.get_all_items()
	price = 0.0
	for i in items:
		amount = int(request.form[i.name])
		itemcom.add_item_count(i, amount)
		price += amount * i.price
	cashcom.reduce_cash(price)
	return redirect('/inventory')
@app.route('/adddish', methods = ['POST'])
def add_dish():
	dishcom.add_dish(request.form['name'], request.form['items'], request.form['price'])
	return redirect('/setting')

@app.route('/remdish', methods = ['POST'])
def rem_dish():
	dishcom.remove_dish(request.form['name'])
	return redirect('/setting')

@app.route('/editdish', methods = ['POST'])
def edit_dish():
	dishcom.edit_dish(request.form['name'], request.form['items'], request.form['price'])
	return redirect('/setting')

@app.route('/additem', methods = ['POST'])
def add_item():
	itemcom.add_item(request.form['name'], request.form['count'], request.form['price'])
	return redirect('/setting')

@app.route('/remitem', methods = ['POST'])
def rem_item():
	itemcom.remove_item(request.form['name'])
	return redirect('/setting')

@app.route('/edititem', methods = ['POST'])
def edit_item():
	itemcom.edit_item(request.form['name'], request.form['amount'], request.form['price'])
	return redirect('/setting')

@app.route('/setting')
def get_setting():
	dishes =  dishcom.get_all_dishes()
	items = itemcom.get_all_items()
	return render_template('settings.html', dishes = dishes, items = items, user = session['username'])