from flask import Flask, url_for



app=Flask("__main__")


@app.route("/")
def index():
    return "This is index"
@app.route('/myhome')
@app.route("/myhome/<username>")
def  home(username="Guest1"):
    return "Welcome to home:" + username

@app.route("/home/")
def home1():
    return "Home"

@app.route('/check_odd_even/<int:number>')
def check_odd_even(number):
    if number % 2==0:
        return "Number is <b> Even </b>"
    
    return "Number is <b> ODD </b>"


def  blog():
    msg = "These are all blog"
    return msg

@app.route('/blog/<int:blog_no>')
def get_blog(blog_no):
    return "This is Blog Number:" + str(blog_no)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('home',username='Sandeep'))
    print(url_for,username="sandeep",password="1234")




# app.add_url_rule('/get_blogs','blog',blog)

if __name__=='__main__':
    app.run(debug=True)