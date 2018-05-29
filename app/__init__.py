<<<<<<< HEAD
from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)
#@app.route('/')
"""
def index():
    return render_template('index.html')
"""
@app.route("/")
def main():
    return render_template('index.html')



@app.route('/lights/')
def luces():
    return render_template('lights.html')

@app.route('/temperature/')
def temperature():
    return render_template('temperature.html')

=======
from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
>>>>>>> 93ee85140ab44f0451becaf1a0037b2f5764488e
