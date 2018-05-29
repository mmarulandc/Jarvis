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

