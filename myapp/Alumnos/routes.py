from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
from models import db
from models import Alumnos
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from db import get_connection
import forms

alumnos=Blueprint("alumnos",__name__)
csrf = CSRFProtect()

@alumnos.route("/getalum",methods=["GET","POST"])
def getalum():

    creat_form=forms.UserForm(request.form)
    alumno=Alumnos.query.all()

    return render_template("ABCompletoA.html", form=creat_form, alumno=alumno)



@alumnos.route("/insertAlum", methods=["GET","POST"])
def index():
    create_form=forms.UserForm(request.form)
    if request.method=="POST":

        nombre=create_form.nombre.data,
        apellidos=create_form.apellidos.data,
        email=create_form.email.data

        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call agregar_alumno(%s, %s, %s)',(nombre,apellidos,email))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
        
        return redirect(url_for("ABCompletoA"))
    return render_template("agregarAlumno.html",form=create_form)

@alumnos.route("/modificar",methods=["GET","POST"])
def modificar():
    create_form=forms.UserForm(request.form)
    if request.method=="GET":
        id=request.args.get("id")
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get("id")
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email
    if request.method=="POST":
        id=create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre=create_form.nombre.data
        alum.apellidos=create_form.apellidos.data
        alum.email=create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("ABCompleto"))
    return render_template("modificar.html",form=create_form)

@alumnos.route("/eliminar",methods=["GET","POST"])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=="GET":
        id=request.args.get("id")
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get("id")
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email
    if request.method=="POST":
        id=create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre=create_form.nombre.data
        alum.apellidos=create_form.apellidos.data
        alum.email=create_form.email.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("ABCompleto"))
    return render_template("eliminar.html",form=create_form)