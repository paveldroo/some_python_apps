from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product/')
def product():
    return render_template('product.html')

@app.route('/products/')
def products():
    return render_template('products.html')

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)