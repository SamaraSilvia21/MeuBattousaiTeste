from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
import os

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == "__main__":

    #port = int(os.getenv('PORT'), '5000')
    #app.run(host='0.0.0.0', port=port)
    app.run(debug=True)