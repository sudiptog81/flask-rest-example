# Flask REST API

- Simple REST API with CRUD functionality.
- Built on top of SQLAlchemy and Marshmallow
- Requires Python 3.x (doesn't work with 2.x)

## Quick Setup

### Clone this Repository

Run the following command in a shell:

```bash
git clone https://git.ghosh.pro/sudipto/flask-rest-example.git
```

Change to the directory cloned into:

```bash
cd flask-rest-example
```

### Install Dependencies

Run the following command in the shell:

```bash
# prepend sudo if required
pip install -r requirements.txt # use pip3 on Linux/Mac
```

### Run Database Migrations

Run the following command in the shell:

```bash
python migrate.py # use python3 on Linux/Mac
```

### Run the Server

Run the following command in the shell:

```bash
python app.py # use python3 on Linux/Mac
# OR
FLASK_APP=app.py flask run
```

Application, by default, listens on port 5000.

## API Structure

### GET `/api/product`

Returns all Products.

#### Example Response

```json
[
    {
        "description": "Boring description",
        "id": 1,
        "name": "Product Boring",
        "price": 1.2,
        "qty": 12
    },
    {
        "description": "Awesome description",
        "id": 2,
        "name": "Product Awesome",
        "price": 1.5,
        "qty": 10
    }
]
```

### GET `/api/product/<id>`

Returns a single Product whose `id` matches the `id` passed in the request URL.

#### Example Response

```json
{
    "description": "Boring description",
    "id": 1,
    "name": "Product Boring",
    "price": 1.2,
    "qty": 12
}
```

### POST `/api/product`

Adds a new Product to the DB

#### Example Request

```http
Request: POST http://localhost:5000/api/product
Content-Type: application/json
```

```json
{
    "name": "Product Boring",
    "description": "Boring description",
    "price": 1.20,
    "qty": 12
}
```

#### Example Response

```json
{
    "description": "Boring description",
    "id": 1,
    "name": "Product Boring",
    "price": 1.2,
    "qty": 12
}
```

### PUT `/api/product/<id>`

Update a Product's fields whose `id` matches the `id` in the request URL.

#### Example Request

```http
Request: PUT http://localhost:5000/api/product/1
Content-Type: application/json
```

```json
{
    "description": "Boring description NEW",
    "name": "Updated Product Boring",
    "price": 1.5,
    "qty": 3
}
```

#### Example Response

```json
{
    "description": "Boring description NEW",
    "id": 1,
    "name": "Updated Product Boring",
    "price": 1.5,
    "qty": 3
}
```

### DELETE `/api/product/<id>`

Delete a Product whose `id` matches the `id` in the request URL.

#### Example Request

```http
Request: DELETE http://localhost:5000/api/product/1
```

#### Example Response

```json
{
    "description": "Boring description NEW",
    "id": 1,
    "name": "Updated Product Boring",
    "price": 1.5,
    "qty": 3
}
```

#### Confirming Deletion

##### Example Request

```http
Request: GET http://localhost:5000/api/product
```

##### Example Response

```json
[]
```

## Author

[Sudipto Ghosh](https://sudipto.ghosh.pro) sudipto(at)ghosh(dot)pro

## License

Source code distributed under the MIT License.