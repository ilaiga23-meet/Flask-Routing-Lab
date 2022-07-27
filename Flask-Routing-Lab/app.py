from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')
def home_page():
    return render_template("home.html")
@app.route('/product1')
def airphones():
    return render_template("airphones.html")
@app.route('/product2')
def iphone():
    return render_template("product.html")
@app.route('/product3')
def barcelona_shirt():
    return render_template("barcelona_shirt.html")
@app.route('/product4')
def macbook():
    return render_template("macbook.html")

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
