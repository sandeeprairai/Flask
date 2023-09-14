from flask import Flask
from flask.templating import render_template


app=Flask("__main__")


@app.route('/demo')
def var_demo():
    username='Sandeep'
    password='san123'
    return render_template('var.html',context={
        'username':username,'password':password
    })

@app.route('/filter')
def filter():
    names=['Sita','Gita','Rita','Nita']
    numbers=[12,35,56,79]
    return render_template('filter.html',context=
                           {"names":names,"numbers":numbers})
    

if __name__=='__main__':
    app.run(debug=True)