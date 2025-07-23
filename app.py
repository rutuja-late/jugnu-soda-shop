from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import sqlite3

app = Flask(__name__)

# --- Menu Definition ---
menu = {
    "Soda (₹25)": {
        "Masala Masti": ["jeera", "white", "chatpata", "mosambi", "sprite", "kashmiri masala", "tangy orange", "lime lemon", "kachi keri", "4 UP", "double decker", "ganga jamuna", "kala khatta", "rim zim", "mix match", "ice-cream soda", "cock tail", "3 UP", "orange", "cola current", "ora cola", "black grapes", "blue berry", "blue lagoon special", "cola thunder", "dil khush khush", "chocolate"],
        "Natural": ["kairi panna", "variyali (badisop)", "imlee masala", "litchi melon", "water melon punch", "golden butter scotch", "puply musk melon", "apple jack", "pan mukhwas", "rose", "orange apricot", "mango tango", "pink panther", "pineapple crush", "litchi crush", "strawberry crush", "natural jamun", "pink peru crush", "white peru crush", "kiwi crush", "king kong", "rose melon", "pina cola", "sahi gulab"],
        "Ayurvedic": ["kokam masala", "ginger lemon", "kairi pudina", "ginger aawla", "lemon pudina"]
    },
    "Non-Alcoholic (₹20)": {
        "Flavours": ["rum cola", "vodka", "whisky", "coffee beer", "golden rum", "fruit beer", "chocolate whisky"]
    },
    "Samosa Pav": {
        "Regular": ["Single samosa ₹12", "samosa pav ₹25", "cheese wrap samosa ₹30", "cheese pav ₹35", "mayo cheese grill pav ₹40", "grill samosa pav ₹35", "grill lays pav ₹35", "grill cheese samosa pav ₹45", "grill mayo cheese samosa pav ₹55", "lays samosa pav ₹45", "cheese lays samosa pav ₹55", "grill mayo cheese lays pav ₹55", "grill mayo cheese lays samosa pav ₹60"],
        "Jain": ["jain samosa ₹20", "jain samosa pav ₹25", "jain cheese wrap samosa ₹30", "jain cheese pav ₹35", "jain grill samosa pav ₹35", "jain grill cheese samosa pav ₹45", "jain grill mayo cheese pav ₹40", "jain grill mayo cheese samosa pav ₹55"]
    },
    "Buns (₹60)": {
        "Types": ["Pizza buns", "Paneer buns"]
    },
    "Cold Cocoa": {
        "Types": ["Small ₹50", "Large ₹100", "Small (takeaway) ₹70", "Large (takeaway) ₹120", "Brownie shake (medium) ₹100", "Brownie shake (large) ₹150"]
    },
    "Brownies": {
        "Options": ["Without ice cream ₹85", "With ice cream ₹120", "Takeaway without ice cream ₹85"]
    }
}

# --- Initialize SQLite ---
def init_db():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        items TEXT,
        total INTEGER,
        payment_mode TEXT,
        timestamp TEXT
    )''')
    conn.commit()
    conn.close()

# --- Save Order ---
def save_order(items, total, payment_mode):
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("INSERT INTO orders (items, total, payment_mode, timestamp) VALUES (?, ?, ?, ?)", (
        json.dumps(items),
        total,
        payment_mode,
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))
    conn.commit()
    conn.close()

# --- Load Orders for Dashboard ---
def load_orders():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT id, items, total, payment_mode, timestamp FROM orders ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    orders = []
    for row in rows:
        orders.append({
            "id": row[0],
            "items": json.loads(row[1]),
            "total": row[2],
            "payment_mode": row[3],
            "timestamp": datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S')
        })
    return orders

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/place_order', methods=['POST'])
def place_order():
    selected_items = request.form.getlist('item[]')
    quantities = request.form.getlist('quantity[]')
    payment_mode = request.form.get('payment_mode')

    items = {}
    total = 0
    for i in range(len(selected_items)):
        item = selected_items[i]
        qty = int(quantities[i])
        if qty > 0:
            items[item] = qty
            if '₹' in item:
                price = int(item.split('₹')[-1])
            elif "Non-Alcoholic" in item:
                price = 20
            elif "Soda" in item:
                price = 25
            else:
                price = 0
            total += price * qty

    save_order(items, total, payment_mode)

    if payment_mode == "UPI":
        return render_template('thankyou.html', payment_mode="UPI", total=total)
    else:
        return render_template('thankyou.html', payment_mode="Cash", total=total)

@app.route('/dashboard')
def dashboard():
    orders = load_orders()
    return render_template('dashboard.html', orders=orders)

# --- Main ---
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    init_db()
    app.run(host='0.0.0.0', port=port)
