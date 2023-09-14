from flask import Flask,request,render_template

app=Flask(__name__)


@app.route("/")
def take_data():
    return render_template('take_data.html')

@app.route('/fetchData',methods=['POST'])
def fetch_data():
    print(request.form)
    return "Request Form is Printed"


if __name__=='__main__':
    app.run(debug=True)
