from flask import Flask, render_template
import os

os.path.dirname(__file__)
DIR = os.path.dirname(__file__)
DIR += '/'
app = Flask(__name__)

@app.route("/") ##creating home page of web page
def hello_world():
    return render_template("home.html")

if __name__== "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
