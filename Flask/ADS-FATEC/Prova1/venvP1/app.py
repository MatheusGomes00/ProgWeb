from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calculo2grau')
def equacao_2grau():
    return render_template('calculo2grau.html')

@app.route('/calc_2grau', methods=['POST'])
def eq_2grau():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    delta = ((b**2) -4 * a * c)
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    return render_template('calculo2grau_apos.html', X1=f'{x1:.2f}', X2=f'{x2:.2f}')

@app.route('/fahrenheit')
def fahrenheit():
    return render_template('fahrenheit.html')

@app.route('/calc_fahrenheit', methods=['GET'])
def calc_fahrenheit():
    args = request.args
    C = float(args.get('celsius'))
    result = C * 1.8 + 32
    return render_template('fahrenheit_apos.html', CELSIUS=F'{C:.2f}', RESULT=f'{result:.2f}')


app.run()
