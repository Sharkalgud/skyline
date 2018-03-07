from app import app
from app.models import Item, Dish, Order
from app.dbcom import DishCom, ItemCom, CashCom
from app.forms import LoginForm
from flask import render_template, flash, redirect, session

cash = 50000

dishcom = DishCom()
itemcom = ItemCom()
cashcom = CashCom()

@app.route('/', methods = ['GET', 'POST'])
def home_page():
	form = LoginForm()
	if form.validate_on_submit():
		flash('{}'.format(form.email.data[:form.email.data.index('@')]))
		session['username'] = form.email.data[:form.email.data.index('@')]
		return redirect('/menu')
	return render_template('index.html', form = form)

@app.route('/index')
def index_page():
	return render_template('inner.html')

@app.route('/menu')
def get_menu():
	dishes =  dishcom.get_all_dishes()
	out = ''
	for d in dishes:
		out += d.name + ' ' + str(d.price) + '/n'
	return render_template('menu.html', dishes = dishes, user = session['username'])
@app.route('/inventory')
def get_inventory():
	items = itemcom.get_all_items()
	cash = cashcom.get_cash()
	out = ''
	for i in items:
		out += i.name + ' ' + str(i.count) + ' ' + str(i.price) + '/n'
	return render_template('inventory.html', items = items, cash = cash, user = session['username'])