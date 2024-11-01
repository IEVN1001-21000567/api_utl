from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

@app.route("/")
def index():
    titulo="IEVN-1001"
    list=['Dulce','Juan','Cristian']
    return render_template('uno.html', titulo=titulo, list=list)

@app.route("/user/<string:user>")
def user(user):
    return "El usuario es: {}".format(user)

@app.route("/numero/<int:n1>")
def numero(n1):
    return "El numero es: {}".format(n1)

@app.route("/datos/<string:nom>/<int:id>")
def datos(nom,id):
    return "<h1>ID:{} Nombre: {}</h1>".format(id,nom)

@app.route("/sumaa/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {}".format(n2+n1)

@app.route("/default")
@app.route("/default/<string:nom>")
def nom2(nom='Ali'):
    return "<h1> El nombre es: {}</h1>".format(nom)

if __name__=="__main__":
    app.run(debug=True)