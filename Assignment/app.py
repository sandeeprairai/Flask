#Create a Route and send the greeting message of Goodmorning/Good Afternoon/Good Evening based on current time

from flask import Flask
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def greeting():
    now=datetime.now()
    current_time=now.time()

    if current_time.hour<12:
        greeting_message="Good morning!"
    elif current_time.hour<17:
        greeting_message="Good afternoon!"
    else:
        greeting_message="Good evening!"
    
    return  greeting_message

if __name__=='__main__':
      app.run(debug=True)
      