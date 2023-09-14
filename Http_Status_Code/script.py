from flask import Flask,request,redirect,url_for

from flask.templating import render_template

app=Flask(__name__)

@app.route('/redirectPage')
def redirected_page():
    print("Request Argument from redirect Page",request.args)
    return "This is redirected page"

@app.route('/redirect')
def redirect_demo():
    print("request Argument form demo",request.args)
    return redirect(url_for('redirected_page'))


if __name__=='__main__':
    app.run(debug=True)