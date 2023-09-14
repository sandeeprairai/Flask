from flask import Flask
from flask.templating import render_template

app=Flask("__main__")


@app.route('/staticdemo')
def static_demo():
    return render_template("static_demo.html")
    



if __name__=='__main__':
    app.run(debug=True)