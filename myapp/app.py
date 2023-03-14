from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import flask


from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect


from Alumnos.routes import alumnos
from Directivos.routes import directivos
from Maestros.routes import maestros

app = flask.Flask(__name__)
app.config["DEBUG"]=True
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.route("/", methods=["GET"])
def home():

    return render_template("index.html")

app.register_blueprint(alumnos)
app.register_blueprint(directivos)
app.register_blueprint(maestros)

if __name__ =="__main__":
    app.run()