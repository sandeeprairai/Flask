from flask import Flask, abort
from flask.templating import render_template,request
from http import HTTPStatus

app=Flask(__name__)

@app.route('/printstatus')
def print_status():
    print(list(HTTPStatus))
    username=request.args.get('uname')
    if username=='admin':

        return render_template('print_status.html',statuses=(list(HTTPStatus)))
    
    else:
        abort(403)










if __name__=='__main__':
    app.run(debug=True)