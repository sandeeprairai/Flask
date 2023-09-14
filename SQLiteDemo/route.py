from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("mycollege.db")
cur = conn.cursor()

cur.execute("select count(*) from sqlite_master where type='table' and name='student'")
count_table = cur.fetchone()[0]
print(count_table)
if count_table == 1:
    print("Table Already Exists")
else:
    conn.execute("CREATE TABLE student (name TEXT,addr TEXT, city TEXT, pin TEXT)")
    print("Table Created")
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deleteInput')
def delete_input():
    return render_template('delete_input.html')

@app.route('/deleteStudent', methods=['POST'])
def delete_student():
    stud_name = request.form.get('txtname')
    try:
        with sqlite3.connect('mycollege.db') as conn:
            my_query = "DELETE FROM student WHERE name='" + stud_name + "';"
            conn.execute(my_query)
            conn.commit()
            msg = "Total Rows Deleted are: " + str(conn.total_changes)
    except:
        conn.rollback()
        msg = "Sorry..Could not Delete Any Records"
    finally:
        conn.close()
    return render_template('success.html', msg=msg)




@app.route('/updateInput')
def update_input():
    return render_template('update_input.html')

@app.route('/updateStudent',methods=['POST'])
def update_student():
    stud_name = request.form.get('txtname')
    stud_city = request.form.get('txtcity')

    try:
        with sqlite3.connect('mycollege.db') as conn:
            my_query = "update student set city='" + stud_city + "' where name='" + stud_name + "';"
            conn.execute(my_query)
            conn.commit()
            msg = "Total Rows Affected are: " + str(conn.total_changes)
    except:
        conn.rollback()
        msg = 'Could not Update Record'
    finally:
        conn.close()
    return render_template('success.html',msg=msg)

@app.route('/addStudent')
def add_student():
    return render_template('add_student.html')

@app.route('/saveStudent', methods=['GET','POST'])
def save_student():
    msg = ''
    if request.method == 'POST':
        try:
            name = request.form.get('studname')
            addr = request.form.get('studaddr')
            city = request.form.get('studcity')
            pin = request.form.get('studpin')

            with sqlite3.connect('mycollege.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO student (name,addr, city, pin) values (?,?,?,?)", (name,addr,city,pin))
                conn.commit()
                msg = "Data Inserted Successfully"
        except:
            conn.rollback()
            msg = "Could Not Insert Data"
        finally:
            conn.close()
    return render_template('success.html', msg=msg)

@app.route('/listStudent')
def list_student():
    conn = sqlite3.connect('mycollege.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('select * from student')
    rows = cur.fetchall()

    return render_template('view.html',rows=rows)


if __name__ == '__main__':
    app.run(debug=True)