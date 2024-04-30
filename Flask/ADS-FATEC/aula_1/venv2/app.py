from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_home():
    return render_template('index.html')

@app.route('/contato')
def pagina_contato():
    return render_template('contato.html')

@app.route('/servicos')
def pagina_services():
    return render_template('servicos.html')

@app.route('/about')
def pagina_about_us():
    return render_template('sobre.html', var_titulo= "Minha página about")


app.run()
