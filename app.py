import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialise app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'db.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise db
db = SQLAlchemy(app)

# Initialise marshmallow
ma = Marshmallow(app)


class Product(db.Model):
    """
    Model of a Product for SQLAlchemy
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

class ProductSchema(ma.Schema):
    """
    Schema for a Product for Marshmallow
    """
    class Meta:
        """
        Fields to be exposed by Marshmallow
        """
        fields = ('id', 'name', 'description', 'price', 'qty')


productSchema = ProductSchema(strict=True)
productsSchema = ProductSchema(many=True, strict=True)

@app.route('/api/product', methods=['POST'])
def addProduct():
    """
    POST Endpoint for adding a Product
    """
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    newProduct = Product(name, description, price, qty)

    db.session.add(newProduct)
    db.session.commit()

    return productSchema.jsonify(newProduct)

@app.route('/api/product', methods=['GET'])
def getProducts():
    """
    GET Endpoint for getting all Products
    """
    allProducts = Product.query.all()
    result = productsSchema.dump(allProducts)
    return jsonify(result.data)

@app.route('/api/product/<id>', methods=['GET'])
def getProduct(id):
    """
    GET Endpoint for getting a Product by it's `id`
    """
    product = Product.query.get(id)
    return productSchema.jsonify(product)


@app.route('/api/product/<id>', methods=['PUT'])
def updateProduct(id):
    """
    PUT Endpoint for updating a Product by it's `id`
    """
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return productSchema.jsonify(product)

@app.route('/api/product/<id>', methods=['DELETE'])
def deleteProduct(id):
    """
    DELETE Endpoint for deleting a Product
    """
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return productSchema.jsonify(product)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
