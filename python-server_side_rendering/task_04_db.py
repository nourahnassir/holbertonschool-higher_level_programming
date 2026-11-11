#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


def create_database():
    db_path = os.path.join(os.path.dirname(__file__), 'products.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Check if table is empty before inserting
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []


def read_csv_file(file_path):
    products = []
    try:
        with open(file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        return []
    return products


def read_sqlite_db(db_path):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
        return []
    return products


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    item_list = []
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            data = json.load(f)
            item_list = data.get('items', [])
    return render_template('items.html', items=item_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    data = []
    error_message = None

    if source == 'json':
        file_path = os.path.join(os.path.dirname(__file__), 'products.json')
        data = read_json_file(file_path)
    elif source == 'csv':
        file_path = os.path.join(os.path.dirname(__file__), 'products.csv')
        data = read_csv_file(file_path)
    elif source == 'sql':
        db_path = os.path.join(os.path.dirname(__file__), 'products.db')
        data = read_sqlite_db(db_path)
    else:
        error_message = "Wrong source"

    if not error_message and product_id is not None:
        filtered_data = [p for p in data if p.get('id') == product_id]
        if not filtered_data:
            error_message = "Product not found"
        else:
            data = filtered_data

    return render_template('product_display.html', products=data, error=error_message)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
