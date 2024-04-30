from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('/imc_calc.html')

@app.route('/calcular_imc_post', methods=['POST'])
def calcular_imc_post():
    altura = float (request.form['txt_altura'])
    peso = float (request.form['txt_peso'])
    if 'Calcular' in request.form:
        calculo = peso / altura ** 2
        if(calculo < 18.5):
            classificacao = 'MAGREZA'
        elif(calculo >=18.5 and calculo <= 24.9):  # 18.5 <= calculo <= 24.9
            classificacao = 'NORMAL'
        elif(calculo >= 25 and calculo <= 29.9):  # 25 <= calculo <= 29.9
            classificacao = 'SOBREPESO'
        elif(calculo >= 30 and calculo <= 39.9):  # 30 <= calculo <= 39.9 
            classificacao = 'OBESIDADE'
        elif(calculo >= 40):
            classificacao = 'OBESIDADE GRAVE'
        return render_template('imc_calc.html', IMC=f'{calculo:.2f}', classificado = classificacao)

@app.route('/calcular_imc_get', methods=['GET'])
def calcular_imc_get():
    args = request.args
    altura = float (args.get['txt_altura'])
    peso = float (args.get['txt_peso'])
    if 'Calcular' in request.form:
        calculo = peso / altura ** 2
        if(calculo < 18.5):
            classificacao = 'MAGREZA'
        elif(calculo >=18.5 and calculo <= 24.9):  # 18.5 <= calculo <= 24.9
            classificacao = 'NORMAL'
        elif(calculo >= 25 and calculo <= 29.9):  # 25 <= calculo <= 29.9
            classificacao = 'SOBREPESO'
        elif(calculo >= 30 and calculo <= 39.9):  # 30 <= calculo <= 39.9 
            classificacao = 'OBESIDADE'
        elif(calculo >= 40):
            classificacao = 'OBESIDADE GRAVE'
        return render_template('imc_calc.html', IMC=f'{calculo:.2f}', classificado = classificacao)


if __name__ == "__main__":
    app.run(debug=True)
