from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
@app.route("/")
def home():
    return render_template("CreateAlgo.html")



if __name__=='__main__':
    app.run(debug=True)
