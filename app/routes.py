from app import app
from app.models import Item, Dish, Order
from app.dbcom import DishCom, ItemCom, CashCom
from flask import render_template

cash = 50000

dishcom = DishCom()
itemcom = ItemCom()
cashcom = CashCom()

@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/menu')
def get_menu():
	dishes =  dishcom.get_all_dishes()
	out = ''
	for d in dishes:
		out += d.name + ' ' + str(d.price) + '/n'
	return render_template('menu.html', dishes = dishes)
@app.route('/inventory')
def get_inventory():
	items = itemcom.get_all_items()
	cash = cashcom.get_cash()
	out = ''
	for i in items:
		out += i.name + ' ' + str(i.count) + ' ' + str(i.price) + '/n'
	return render_template('inventory.html', items = items, cash = cash)