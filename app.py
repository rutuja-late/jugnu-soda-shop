from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import os
import qrcode

app = Flask(__name__)

menu = {
    "soda_masala_masti": {
        "jeera": 25, "white": 25, "chatpata": 25, "mosambi": 25, "sprite": 25, "kashmiri masala": 25,
        "tangy orange": 25, "lime lemon": 25, "kachi keri": 25, "4 UP": 25, "double decker": 25,
        "ganga jamuna": 25, "kala khatta": 25, "rim zim": 25, "mix match": 25, "ice-cream soda": 25,
        "cock tail": 25, "3 UP": 25, "orange": 25, "cola current": 25, "ora cola": 25,
        "black grapes": 25, "blue berry": 25, "blue lagoon special": 25, "cola thunder": 25,
        "dil khush khush": 25, "chocolate": 25
    },
    "soda_natural": {
        "kairi panna": 25, "variyali (badisop)": 25, "imlee masala": 25, "litchi melon": 25,
        "water melon punch": 25, "golden butter scotch": 25, "puply musk melon": 25,
        "apple jack": 25, "pan mukhwas": 25, "rose": 25, "orange apricot": 25, "mango tango": 25,
        "pink panther": 25, "pineapple crush": 25, "litchi crush": 25, "strawberry crush": 25,
        "natural jamun": 25, "pink peru crush": 25, "white peru crush": 25, "kiwi crush": 25,
        "king kong": 25, "rose melon": 25, "pina cola": 25, "sahi gulab": 25
    },
    "soda_ayurvedic": {
        "kokam masala": 25, "ginger lemon": 25, "kairi pudina": 25, "ginger aawla": 25, "lemon pudina": 25
    },
    "non_alcoholic": {
        "rum cola": 20, "vodka": 20, "whisky": 20, "coffee beer": 20, "golden rum": 20,
        "fruit beer": 20, "chocolate whisky": 20
    },
    "samosa_pav": {
        "samosa": 12, "samosa pav": 25, "cheese wrap samosa": 30, "cheese pav": 35,
        "mayo cheese grill pav": 40, "grill samosa pav": 35, "grill lays pav": 35,
        "grill cheese samosa pav": 45, "grill mayo cheese samosa pav": 55, "lays samosa pav": 45,
        "cheese lays samosa pav": 55, "grill mayo cheese lays pav": 55,
        "grill mayo cheese lays samosa pav": 60
    },
    "samosa_pav_jain": {
        "jain samosa": 20, "jain samosa pav": 25, "jain cheese wrap samosa": 30,
        "jain cheese pav": 35, "jain grill samosa pav": 35, "jain grill cheese samosa pav": 45,
        "jain grill mayo cheese pav": 40, "jain grill mayo cheese samosa pav": 55
    },
    "buns": {
        "pizza buns": 60, "paneer buns": 60
    },
    "cold_cocoa": {
        "small": 50, "large": 100, "small (takeaway)": 70, "large (takeaway)": 120,
        "brownie shake (medium)": 100, "brownie shake (large)": 150
    },
    "brownies": {
        "without ice cream": 85, "with ice cream": 120, "takeaway without ice cream": 85
    }
}

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/place_order', methods=['POST'])
def place_order():
    selected_items = request.form.getlist('items[]')
    quantities = request.form.getlist('quantities[]')
    total_price = 0
    order_summary = []

    for item, qty in zip(selected_items, quantities):
        qty = int(qty)
        for category in menu.values():
            if item in category:
                price = category[item]
                total_price += price * qty
                order_summary.append(f"{item} x {qty} = ₹{price * qty}")
                break

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS orders (timestamp TEXT, items TEXT, total_price INTEGER)")
    c.execute("INSERT INTO orders (timestamp, items, total_price) VALUES (?, ?, ?)",
              (timestamp, "\n".join(order_summary), total_price))
    conn.commit()
    conn.close()

    return render_template('thankyou.html', total_price=total_price, order_summary=order_summary)

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
