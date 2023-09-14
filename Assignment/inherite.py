from flask import Flask
from flask.templating import render_template

app=Flask("__main__")

@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product')
def product():
    return render_template('product.html')


if __name__=='__main__':
    app.run(debug=True)
