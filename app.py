
import datetime
from errno import ENFILE
from ftplib import all_errors
from os import urandom
from random import random
import time
# from os import uname
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema,fields


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=False)    
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/basemedica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.debug = True

#settings

app.secret_key = 'mysecretkey'

class Medicina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(500),nullable=False)
    apellido =db.Column(db.String(500),nullable=False)
    direccion = db.Column(db.String(500),nullable=False)
    numeroTele = db.Column(db.Integer,nullable=False)
    edad = db.Column(db.String(500),nullable=False)
    peso = db.Column(db.String(500),nullable=False)
    altura = db.Column(db.String(500),nullable=False)
    enfermedades = db.Column(db.String(500),nullable=False)
    medicacion = db.Column(db.String(500),nullable=False)
    condiciones  = db.Column(db.String(500),nullable=False)
    fecha = db.Column(db.DateTime,nullable=False)

    def __init__(self,nombre,apellido,direccion,numeroTele,edad,peso,altura,enfermedades,medicacion,condiciones,fecha):
        self.nombre = nombre
        self.apellido =apellido
        self.direccion =direccion
        self.numeroTele = numeroTele
        self.edad =edad
        self.peso = peso
        self.altura = altura
        self.enfermedades = enfermedades
        self.medicacion = medicacion
        self.condiciones = condiciones
        self.fecha = fecha
        
class MedicinaSchema(ma.Schema):
    class Meta:
        fields = ("id","nombre","apellido","direccion","numeroTele","altura","edad","peso","enfermedades","medicacion","condiciones","fecha")
        
Medicina_schema = MedicinaSchema()
Medicina_schema = MedicinaSchema(many=True)


@app.route("/all")
def index():
    return render_template("index.html")

@app.route("/add_medicina", methods=["POST"])
def add_medicina():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['doreccion']
        numeroTele = request.form['numeroTele']
        edad = request.form['edad']
        peso = request.form['peso']
        altura = request.form['altura']
        enfermedades = request.form['enfermedades']
        medicacion = request.form['medicacion']
        condiciones = request.form['condicion']
        fecha = datetime.date.today()
        
        my_posts = Medicina(nombre,apellido,direccion,numeroTele,edad,peso,altura,enfermedades,medicacion,condiciones,fecha)
        db.session.add(my_posts)
        db.session.commit()
        
        
        print(nombre,apellido,direccion,numeroTele,peso,edad,altura, enfermedades,medicacion,condiciones,fecha)
        return redirect(url_for("index"))


# @app.route("/delete/<string:id>",methods=['DELETE'])
# def delete_pedido(id):
#     medicina = Medicina.query.get(id)
#     db.session.delete(medicina)
#     db.session.commit()
#     flash('Pedido Eliminado')
#     return redirect(url_for("index"))


@app.route("/medicina")
def index2():
    all_medicina = Medicina.query.all()
    result = Medicina_schema.dump(all_medicina)
    return render_template("medicina.html", medicinas = result)

@app.route("/medicina/<id>/")
def indexId(id):
    all_medicina = Medicina.query.get(id)
    return render_template("individual.html", medicinas = all_medicina)