Jugnu Soda's & More - QR Code Ordering Website
---------------------------------------------

📌 DESCRIPTION:
A complete QR-based takeaway ordering system with UPI/Cash payment support, real-time menu, and a shopkeeper dashboard.

🌟 FEATURES:
- Card-style interactive menu with quantity buttons
- Mobile-friendly layout
- Total bill calculator
- UPI & Cash payment mode support
- UPI QR shows only when selected
- Order history saved in SQLite
- Shopkeeper dashboard at /dashboard
- No login or signup

📂 FOLDER STRUCTURE:
JugnuSodaShop/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── qr/
│   │   └── site_qr.png
├── templates/
│   ├── index.html
│   ├── thankyou.html
│   └── dashboard.html
├── app.py
├── create_database.py
├── orders.db  ← Auto-generated
├── requirements.txt
└── README.txt

⚙️ SETUP INSTRUCTIONS:

1. Install dependencies:
   pip install -r requirements.txt

2. Create database:
   python create_database.py

3. Run the Flask app:
   python app.py

4. Visit on mobile/desktop:
   http://127.0.0.1:5000/

📱 SCAN QR CODE:
Place site_qr.png at your shop. Customers scan it to open the site.

💳 UPI PAYMENT:
Customer selects "UPI", scans the QR and confirms payment.

🧾 ORDER RECORD:
All orders saved in `orders.db` and shown on /dashboard.

📤 DEPLOYMENT:
Use [Render](https://render.com) or PythonAnywhere for free hosting.

   (Recommended for Render):
   - Push your folder to GitHub
   - Create new Web Service on Render
   - Set Build Command: `pip install -r requirements.txt`
   - Set Start Command: `python app.py`
   - Add `orders.db` and `static/qr/site_qr.png` to your repo

✅ DONE!
Your QR ordering website is now live. Happy serving! 🎉
