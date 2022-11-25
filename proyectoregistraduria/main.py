import pymongo
import certifi
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

import pymongo
import certifi

from Controladores.ControladorCandidatos import ControladorCandidatos

app=Flask(__name__)
cors = CORS(app)
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://orlandoizq0707:1234@registraduriaciclo4.sgs4ktl.mongodb.net/registraduriaciclo4?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)
basedatos = client ["registraduriaciclo4"]
print(basedatos.list_collection_names())


miControladorCandidato= ControladorCandidatos()





@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])



@app.route("/Candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidatos():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/Candidatos/<string:id>",methods=['GET'])
def getCandidatos(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/estudiante/<string:id>",methods=['PUT'])
def modoficarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def elemininarCandidatos(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)




