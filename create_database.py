import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('orders.db')
c = conn.cursor()

# Drop old table
c.execute('DROP TABLE IF EXISTS menu')

# Create new menu table
c.execute('''
    CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        subcategory TEXT,
        item_name TEXT NOT NULL,
        price INTEGER NOT NULL
    )
''')

# Define full menu
menu_items = [
    # --- Soda Section ---
    # Masala Masti (₹25)
    *[('Soda', 'Masala Masti', item, 25) for item in [
        'jeera', 'white', 'chatpata', 'mosambi', 'sprite', 'kashmiri masala',
        'tangy orange', 'lime lemon', 'kachi keri', '4 UP', 'double decker',
        'ganga jamuna', 'kala khatta', 'rim zim', 'mix match', 'ice-cream soda',
        'cock tail', '3 UP', 'orange', 'cola current', 'ora cola', 'black grapes',
        'blue berry', 'blue lagoon special', 'cola thunder', 'dil khush khush',
        'chocolate'
    ]],
    # Natural (₹25)
    *[('Soda', 'Natural', item, 25) for item in [
        'kairi panna', 'variyali (badisop)', 'imlee masala', 'litchi melon',
        'water melon punch', 'golden butter scotch', 'puply musk melon',
        'apple jack', 'pan mukhwas', 'rose', 'orange apricot', 'mango tango',
        'pink panther', 'pineapple crush', 'litchi crush', 'strawberry crush',
        'natural jamun', 'pink peru crush', 'white peru crush', 'kiwi crush',
        'king kong', 'rose melon', 'pina cola', 'sahi gulab'
    ]],
    # Ayurvedic (₹25)
    *[('Soda', 'Ayurvedic', item, 25) for item in [
        'kokam masala', 'ginger lemon', 'kairi pudina', 'ginger aawla', 'lemon pudina'
    ]],

 # Non-Alcoholic Drinks (₹20)
('Non-Alcoholic', 'Drinks', 'rum cola', 20),
('Non-Alcoholic', 'Drinks', 'vodka', 20),
('Non-Alcoholic', 'Drinks', 'whisky', 20),
('Non-Alcoholic', 'Drinks', 'coffee beer', 20),
('Non-Alcoholic', 'Drinks', 'golden rum', 20),
('Non-Alcoholic', 'Drinks', 'fruit beer', 20),
('Non-Alcoholic', 'Drinks', 'chocolate whisky', 20),


    # --- Samosa Pav Section ---
    *[('Samosa Pav', 'Regular', item, price) for item, price in [
        ('Single samosa', 12), ('samosa pav', 25), ('cheese wrap samosa', 30), ('cheese pav', 35),
        ('mayo cheese grill pav', 40), ('grill samosa pav', 35), ('grill lays pav', 35),
        ('grill cheese samosa pav', 45), ('grill mayo cheese samosa pav', 55), ('lays samosa pav', 45),
        ('cheese lays samosa pav', 55), ('grill mayo cheese lays pav', 55),
        ('grill mayo cheese lays samosa pav', 60)
    ]],
    *[('Samosa Pav', 'Jain', item, price) for item, price in [
        ('jain samosa', 20), ('jain samosa pav', 25), ('jain cheese wrap samosa', 30),
        ('jain cheese pav', 35), ('jain grill samosa pav', 35),
        ('jain grill cheese samosa pav', 45), ('jain grill mayo cheese pav', 40),
        ('jain grill mayo cheese samosa pav', 55)
    ]],

    # --- Buns ---
    ('Buns', '', 'Pizza buns', 60),
    ('Buns', '', 'Paneer buns', 60),

    # --- Chocolate Cold Cocoa ---
    *[('Cold Cocoa', '', item, price) for item, price in [
        ('Small', 50), ('Large', 100), ('Small (takeaway)', 70), ('Large (takeaway)', 120),
        ('Brownie shake (medium)', 100), ('Brownie shake (large)', 150)
    ]],

    # --- Brownies ---
    *[('Brownies', '', item, price) for item, price in [
        ('Without ice cream', 85), ('With ice cream', 120), ('Takeaway without ice cream', 85)
    ]]
]

# Insert all items
c.executemany('INSERT INTO menu (category, subcategory, item_name, price) VALUES (?, ?, ?, ?)', menu_items)

# Save and close
conn.commit()
conn.close()
print("✅ Database recreated and full menu inserted successfully.")
