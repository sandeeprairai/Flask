from flask import Flask,render_template,request


app=Flask(__name__)

@app.route('/querydemo')
def query_demo():
    return render_template('query_demo.html')

    print(request.args)
    return "<h1>Request Arguments Printed </h1>"

if __name__=="__main__":
    app.run(debug=True)
