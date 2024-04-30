from flask import Flask, render_template

app = Flask(__name__)
""" instancia um objeto da classe Flask """

@app.route('/')  # rota raiz
def pagina_index():
    return render_template('index.html')

@app.route('/menu')
def pagina_menu():
    return render_template('FrontProjeto.html')

@app.route('/cadastro')
def pagina_cadastro():
    return render_template('CadastroProjeto.html')

@app.route('/listar')
def pagina_listagem_alunos():
    return render_template('listaAlunos.html')


app.run()
