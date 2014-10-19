####whoop best blog evar
from flask import Flask, render_template, request, redirect, g, url_for, flash
import sqlite3

app = Flask(__name__) #Create flask object
app.config.from_object(__name__) #add configuration information

@app.route("/")
def index():
    pass



#Configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'dontputthisongithub' #hurr
USERNAME = 'admin'
PASSWORD = 'notongithub'

if __name__ == "__main__":
    app.debug=True
    app.run()
