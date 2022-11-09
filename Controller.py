from flask import Flask, request, jsonify, make_response
from Model import Model


app = Flask(__name__)

@app.route('/produtos/', methods=["GET"])
def consultar():
    return Model.jsonReturn()


@app.route('/soma', methods=["GET"])
def consultarCliente():
    return Model.soma()

if __name__ == '__main__':
    app.run(debug=True,port= 5000)