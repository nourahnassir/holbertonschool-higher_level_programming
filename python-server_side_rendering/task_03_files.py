#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


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
                # Convert id and price to appropriate types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
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
    app.run(debug=True, port=5000)
