# Jugnu Soda's & More – QR-based Takeaway Website

## Features:
- Scan QR, open ordering page
- View categories: Soda, Samosa Pav, Non-Alcoholic, Cold Cocoa, etc.
- Select items, choose payment mode (Cash/UPI)
- View order success page
- Admin dashboard to see order history

## How to Run:
1. Install Flask:
   pip install -r requirements.txt

2. Create database:
   python create_database.py

3. Start the server:
   python app.py

4. Access site at:
   http://127.0.0.1:5000

## Folder Structure:
- app.py
- create_database.py
- requirements.txt
- README.txt
- static/
    - css/style.css
    - js/main.js
- templates/
    - index.html
    - thankyou.html
    - dashboard.html
