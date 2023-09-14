from flask import Flask,request

app=Flask(__name__)


@app.route('/requestdemo')
def request_demo():
    print(request.__dict__.items())
    return "This Page printed Request Object"
    print(request.method)
   



if __name__=="__main__":
    app.run(debug=True)
 