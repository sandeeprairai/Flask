from flask import Flask

app=Flask(__name__)

@app.route('/hello')
def helloWorld():
    msg="hello world"
    return msg

if __name__=='__main__':
    app.run(debug=True)
