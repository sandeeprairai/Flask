from flask import Flask
from flask.templating import render_template,request

app=Flask("__main__")


@app.route("/")
def take_date():
    return render_template('take_data.html')

@app.route('/fetchData',methods=['POST'])
def fetch_data():
    print(request.form)
    return "Request form is Printed"
    



if __name__=='__main__':
    app.run(debug=True)