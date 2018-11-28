# wsgi.py
from flask import Flask, jsonify, abort

app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'test'}
]

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def list_products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>')
def show_product(id):
    PDT = [item for item in PRODUCTS if item['id'] == id]
    try:
        return jsonify( PDT[0])
    except IndexError:
        abort(404)

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def del_product(id):
    PDT = [item for item in PRODUCTS if item['id'] != id]
    return jsonify(PDT, status.HTTP_204)
