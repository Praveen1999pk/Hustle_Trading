from flask import Flask
import mysql.connector
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=='__main__':
    #mydb=mysql.connector.connect(host="localhost",user="",passwd="")
    mydb=sqlite3.connect("database1.db")
    query=mydb.cursor()
    res=query.execute("SELECT * FROM bucket")
    print(res.fetchall())
    app.run(debug=True)

