from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_menu():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT category, subcategory, item_name, price FROM menu")
    data = c.fetchall()
    conn.close()

    menu = {}
    for category, subcategory, item, price in data:
        if category not in menu:
            menu[category] = {}
        if subcategory not in menu[category]:
            menu[category][subcategory] = []
        menu[category][subcategory].append({'item_name': item, 'price': price})
    return menu

@app.route('/')
def index():
    menu = get_menu()
    return render_template('index.html', menu=menu)

@app.route('/place_order', methods=['POST'])
def place_order():
    items = request.form.getlist('items[]')
    total_price = request.form['total_price']
    payment_mode = request.form['payment_mode']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    for item in items:
        c.execute("INSERT INTO orders (item_name, price, payment_mode, timestamp) VALUES (?, ?, ?, ?)",
                  (item.split('|')[0], float(item.split('|')[1]), payment_mode, timestamp))
    conn.commit()
    conn.close()
    return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

# ✅ Add the dashboard route at the end
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT * FROM orders ORDER BY timestamp DESC")
    orders = c.fetchall()
    conn.close()
    return render_template('dashboard.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
