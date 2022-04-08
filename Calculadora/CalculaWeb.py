import os
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/calculaform', methods=['POST', 'GET'])
def calcular():
    valor1 = request.form['v1']
    valor2 = request.form['v2']
    operacao = request.form['operacao']
    v1 = int(valor1)
    v2 = int(valor2)

    if operacao == '+':
        return str(v1+v2)
    elif operacao == '-':
        return str(v1-v2)
    elif operacao == '*':
        return str(v1 * v2)
    elif operacao == '/':
        return str(v1 / v2)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
