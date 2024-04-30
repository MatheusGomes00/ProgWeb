from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)

@app.route('/')
def raiz():
    return render_template('form_cadastro.html')

@app.route('/cadastrar_usuario', methods=['POST'])
def inserir_usuario():
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    email = request.form['txt_email']
    senha = request.form['txt_senha']
    if 'sub_salvar' in request.form:
        db = mysql.connector.connect(host='201.23.3.86',
                                    port=5000,
                                    user='usr_aluno',
                                    password='E$tud@_m@1$',
                                    database='aula_fatec')
        mycursor = db.cursor()
        query = "INSERT INTO gomes_tbusuario(nome, cpf, email, senha) VALUES(%s, %s, %s, %s)"
        values = (nome, cpf, email, senha)
        mycursor.execute(query, values)
        db.commit()
        return 'gravou'

@app.route('/caduser')
def lista_user():
    db = mysql.connector.connect(host='201.23.3.86',
                                    port=5000,
                                    user='usr_aluno',
                                    password='E$tud@_m@1$',
                                    database='aula_fatec')  # faz a conexão com o banco na variável db
    mycursor = db.cursor()  # para fazer alterações no banco é preciso criar o cursor
    query = 'select nome, cpf, email, from gomes_tbusuario'  # cria a query de seleção no banco
    mycursor.execute(query)  # executa a query
    resultado = mycursor.fetchall()  # recupera toda a pesquisa executada na query
    return render_template('cadusuario.html', usuarios=resultado)


app.run()
