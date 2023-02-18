from flask import Flask
from flask import render_template, request, redirect
from flask import session, flash
from flask import url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


tetris = Jogo('Tetris', 'Puzzle', 'Atari')
gow = Jogo('God of War', 'Rack n Slash', 'PS2')
mk = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [tetris, gow, mk]


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


pedro = Usuario('Pedro', 'pedro', 'pass')
jose = Usuario('José', 'jose', 'pass')
maria = Usuario('Maria', 'maria', 'pass')
usuarios = {pedro.nickname: pedro,
            jose.nickname: jose,
            maria.nickname: maria}


app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(f'Usuário {usuario.nickname} logado com sucesso.')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuário não logado.')
            return redirect(url_for('login', proxima=url_for('novo')))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect(url_for('index'))


app.run(debug=True)
