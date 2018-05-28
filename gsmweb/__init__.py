import os
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for
)
app = Flask(__name__,instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route("/")
def hello():
    return render_template('index.html')
