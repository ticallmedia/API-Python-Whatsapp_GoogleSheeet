from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

#________________________________________________________________________________________________________

app = Flask(__name__)

#________________________________________________________________________________________________________
#Base de datos SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Tabla Log
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_y_hora = db.Column(db.DateTime, default = datetime.utcnow)
    texto = db.Column(db.TEXT)

#Crear tabla si no existe
with app.app_context():
    db.create_all()

    prueba1 = Log(texto = 'Mensaje de prueba 1')
    prueba2 = Log(texto = 'Mensaje de prueba 2')

    db.session.add(prueba1)
    db.session.add(prueba2)
    db.session.commit()
#________________________________________________________________________________________________________
#funcion para ordendar los registro por fecha y hora

def ordenar_fecha_hora(registros):
    return sorted(registros, key=lambda x: x.fecha_y_hora, reverse=True)


@app.route('/')

def index():
    #obtener todos los registros de la base de  datos
    registros = Log.query.all()
    return render_template('index.html', registros = registros )

#agregar información de la base de datos
mensajes_log = []

#Agregar informacion a la base de datos
def agregar_mensajes_log(texto):
    mensajes_log.append(texto)

    #guardar mensajes en la de datos
    nuevo_registro = Log(texto = texto)
    db.session.add(nuevo_registro)
    db.session.commit()
#________________________________________________________________________________________________________
#Agregar  mensajes de ejemplo

#agregar_mensajes_log(json.dumps('Prueba de base de datos test1'))


#________________________________________________________________________________________________________

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)