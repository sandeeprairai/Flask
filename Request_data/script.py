from flask import Flask,request,render_template
import requests


app=Flask(__name__)

@app.route('/makejson')
def make_json():
    person={
        "name":"Rupal",
        "language":"Python",
        "framework":"[Flask,Dkango,Bootle]"
    }

    res=requests.post("http://127.0.0.1:5000/processJson",json=person)
    return res.text


@app.route('/processJson',methods=['post'])
def process_json():
    if requests.is_json():
        return "It has a json data"
    else:
        return "It has not json data"



if __name__=='__main__':
    app.run(debug=True)