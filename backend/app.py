from flask import Flask, request, jsonify      

app = Flask(__name__)    

# Some fake products
fake_products = [
    {
        'id': 0,
        'brand': 'Brand 1',
        'name': 'Superlong Product Title With Superpowers',
        'platform': 'Platform.com',
        'function': 'cleansing'
    },
    {
        'id': 1,
        'brand': 'Brand 2',
        'name': 'Product Title 2',
        'platform': 'Platform.com',
        'function': 'moisturizing'
    },
    {
        'id': 2,
        'brand': 'Brand 1',
        'name': 'Product Title 3',
        'platform': 'Platform.com',
        'function': 'cleansing',
    },
    {
        'id': 3,
        'brand': 'Longer Brand Name',
        'name': 'Product Title 4',
        'platform': 'Something.com',
        'function': 'moisturizing'
    },
    {
        'id': 4,
        'brand': 'Brand 2',
        'name': 'Product Title 5',
        'platform': 'Platform.com',
        'function': 'cleansing'
    },
    {
        'id': 5,
        'brand': 'Another Brand',
        'name': 'Product Title 6',
        'platform': 'Things.com',
        'function': 'moisturizing'
    },
    {
        'id': 6,
        'brand': 'Brand 1',
        'name': 'Superlong Product Title With Superpowers 2',
        'platform': 'Something.com',
        'function': 'cleansing'
    },
    {
        'id': 7,
        'brand': 'Brand X',
        'name': 'Product Title 7',
        'platform': 'Fake.com',
        'function': 'moisturizing'
    },
    {
        'id': 8,
        'brand': 'Brand X',
        'name': 'uperlong Product Title With Superpowers 3',
        'platform': 'Things.com',
        'function': 'cleansing'
    },
    {
        'id': 9,
        'brand': 'Longer Brand Name 2',
        'name': 'Product Title 8',
        'platform': 'Something.com',
        'function': 'moisturizing'
    },
    {
        'id': 10,
        'brand': 'Brandy Brand',
        'name': 'Product Title 9',
        'platform': 'Platform.com',
        'function': 'cleansing'
    },
    {
        'id': 11,
        'brand': 'Another Brand 2',
        'name': 'Product Title 10',
        'platform': 'Fake.com',
        'function': 'moisturizing'
    }
]

@app.route("/")                   

def welcome():                      
    return "Welcome to the phony products service"  

@app.route("/products")    

def products():

    return jsonify(fake_products)

@app.route("/products/moisturizers")    

def products_moisturizers():

    moisturizing_products = list(filter(lambda product: product['function'] == 'moisturizing', fake_products))
    return jsonify(moisturizing_products)

@app.route("/products/cleansers")    

def products_cleansers():

    cleansing_products = list(filter(lambda product: product['function'] == 'cleansing', fake_products))
    return jsonify(cleansing_products)

if __name__ == "__main__":        
    app.run()                            # run the flask app