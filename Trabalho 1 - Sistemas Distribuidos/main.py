import statistics

from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operator = request.form['operator']

    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide' and num2 != 0:
            result = num1 / num2
        elif operator == 'potencia':
            result = num1 ** num2

        else:
            result = '"Operação Invalida"'
    else:
        result = ' "Operação Invalida" '

    return render_template('index.html', result=result)

@app.route('/calculate_operacao', methods=['POST'])
def calculate_operacao():
    num3 = request.form['num3']
    operator2 = request.form['operator2']

    if num3.isdigit() and operator2 == 'raiz':
        num3 = int(num3)
        result = math.sqrt(num3)
    else:
        result = ' "Operação Invalida" '

    return render_template('index.html', result=result)

@app.route('/calculate_media', methods=['POST'])
def calculate_media():
    media = request.form['txt_media']
    media = media.split(',')
    y = 0
    for x in media:
        y += float(x)
    result = y / len(media)
    return render_template('index.html', result=result)

@app.route('/calculate_moda', methods=['POST'])
def calculate_moda():
    moda = request.form['txt_moda']
    result = statistics.mode(moda.split(','))
    return render_template('index.html', result=result)



if __name__ == '__main__':
    app.run()
