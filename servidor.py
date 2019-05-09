from flask import Flask, render_template, request

class Pessoa():
	def __init__(self, nome, endereco, cpf):
		self.nome = nome
		self.endereco = endereco
		self.cpf = cpf

pessoas = []

app = Flask(__name__)


@app.route("/")
def inicio():
	return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html")

@app.route("/form_inserir_pessoa")
def form_inserir_pessoa():
	return render_template("form_inserir_pessoa.html")

@app.route("/cadastrar_pessoa")
def cadastrar_pessoa():
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	cpf = request.args.get("cpf")
	pessoas.append(Pessoa(nome, endereco, cpf))
	return render_template("exibir_mensagem.html", mensagem="uhuuu deu certo", pessoa=(nome, endereco, cpf))

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
	return render_template("form_alterar_pessoa.html")

@app.route("/exibir_mensagem")
def exibir_mensagem():
	return render_template("exibir_mensagem.html")

app.run(debug=True, host="0.0.0.0")