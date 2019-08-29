from flask import Flask, render_template, request
import sqlite3
app = Flask("my-app")

#
# @app.route("/")
# def index():
#     return render_template("main.html")
#
#
# @app.route("/login/<name>/<int:var>")
# def login_page(name, var):
#     return render_template("login.html", name=name, var=var)
#
#
# @app.route("/table/<int:cols>/<int:rows>")
# def table(cols, rows):
#     return render_template("table.html", rows=rows, cols=cols)


@app.route("/cool", methods=["GET", "POST"])
def cool():
    if request.method == 'GET':
        return render_template("cool.html")
    else:
        weight = float(request.form['w'])
        height = float(request.form['h'])
        bmi = weight / height ** 2
        return render_template("cool.html", bmi=bmi)

def creat_sql():
    conn = sqlite3.connect("my-db.sqlite")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS student (
      id INTEGER PRIMARY KEY AUTOINCREMENT ,
      first_name TEXT NOT NULL, 
      last_name TEXT NOT NULL,
      age INTEGER 
    );""")
    first_name = input("first name:")
    last_name = input("last name:")
    age = int(input("age:"))

    conn.execute(f"""
    INSERT INTO student 
      (first_name, last_name, age) VALUES 
      ({first_name}, {last_name}, {age});
    """)

    conn.commit()
creat_sql()


app.run()
