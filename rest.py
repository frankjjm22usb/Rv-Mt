from flask import Flask,jsonify
# from flask import request
from Evaluador import Evaluador
from MetodoDeBiseccion import metodoBiseccion
#from Graficador import graficador

app = Flask(__name__)
evaluador=Evaluador()
biseccion=metodoBiseccion()
# graficas=graficador()
@app.route('/')

def index():
    return 'Alexandra'

@app.route('/Evaluador/<string:ecuation>/<float:num>',methods=['GET'])
def params(ecuation='name por default', num=0):
    return 'El parametro es {},'.format(evaluador.evaluar(num,ecuation))


@app.route('/metodos/biseccion/<string:ecuation>/<a>/<b>/<float:errorTolerable>',methods=['GET'])
def bisecc(ecuation='name por default',a=0,b=0,errorTolerable=0):
    a=float(a)
    b=float(b)
    errorTolerable=float(errorTolerable)
    return jsonify(biseccion.comprobacion(a,b,ecuation,errorTolerable), biseccion.grafica(ecuation))



""""
@app.route('/Grafica/<string:ecuation>',methods=['GET'])
def grafica(ecuation='name por default'):
    return 'El parametro es {},'.format(graficador.grafica(ecuation))
"""
if __name__ == '__main__':
    app.run(debug=True)