from flask import Flask, render_template, request, jsonify, redirect
import mysql.connector


app = Flask(__name__)

def conexao_com_db():
    try:
        return mysql.connector.connect(host='201.23.3.86',
                                        port=5000,
                                        user='usr_aluno',
                                        password='E$tud@_m@1$',
                                        database='aula_fatec')  # faz a conexão com o banco na variável db
    except mysql.connector.Error as err:
        print(f'Erro de conexão com banco de dados: {err}')
        return None


@app.route('/')
def raiz():
    return render_template('form_cadastro.html')


@app.route('/cadastrar_usuario', methods=['POST'])
def inserir_usuario():
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    email = request.form['txt_email']
    senha = request.form['txt_senha']
    db = conexao_com_db()
    mycursor = db.cursor()
    query = "INSERT INTO gomes_tbusuario(nome, cpf, email, senha) VALUES(%s, %s, %s, %s)"
    values = (nome, cpf, email, senha)
    try:
        mycursor.execute(query, values)
        db.commit()
        return jsonify({"sucess": True})
    except Exception as e:
        db.rollback()  # Desfaz qualquer alteração no banco de dados em caso de erro
        return jsonify({"sucess": False, "error": str(e)})

@app.route('/list_user')
def lista_user():
    db = conexao_com_db()
    mycursor = db.cursor()  # para fazer alterações no banco é preciso criar o cursor
    query = "select nome, cpf, email, id from gomes_tbusuario"  # cria a query de seleção no banco
    mycursor.execute(query)  # executa a query
    resultado = mycursor.fetchall()  # recupera toda a pesquisa executada na query
    return render_template('lista_user.html', opcao= 'listar', usuarios=resultado)


@app.route('/alterar_usuario/<user>')  # carregar página de cadastro
def alterar_usuario(user):
    db = conexao_com_db()
    mycursor = db.cursor() 
    query = "select nome, cpf, email, id from gomes_tbusuario where id = " + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('alterar_user.html', opcao='alterar', usuarios=resultado)


@app.route('/atualizar_cad', methods=['POST'])
def atualizar_cadastro():
    id_do_usuario = request.form['id_do_usuario']
    novo_nome = request.form['txt_nome']
    novo_cpf = request.form['txt_cpf']
    novo_email = request.form['txt_email']
    nova_senha = request.form['txt_senha']
    db = conexao_com_db()
    if db:
        mycursor = db.cursor()
        query = "UPDATE gomes_tbusuario SET nome=%s, CPF=%s, email=%s, senha=%s WHERE id=%s"
        values = (novo_nome, novo_cpf, novo_email, nova_senha, id_do_usuario)
        mycursor.execute(query, values)
        db.commit()  # ou utilizar o rollback para fechar a transação
        return 'Cadastro atualizado com sucesso'
    else:
        return 'Erro de conexão com o banco de dados'

@app.route('/excluir_usuario/<user>')
def excluir_usuario(user):
    db = conexao_com_db()
    if db:
        mycursor = db.cursor()
        query = "DELETE FROM gomes_tbusuario WHERE id = " + user
        mycursor.execute(query)
        db.commit()
        return redirect('/list_user')


app.run()
