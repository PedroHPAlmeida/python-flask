from flask import Flask
from flask import render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


tetris = Jogo('Tetris', 'Puzzle', 'Atari')
gow = Jogo('God of War', 'Rack n Slash', 'PS2')
mk = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [tetris, gow, mk]


app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['senha'] == 'pass':
        session['usuario_logado'] = request.form['usuario']
        flash(f'Usuário {session["usuario_logado"]} logado com sucesso.')
        return redirect('/')
    flash('Usuário não logado.')
    return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect('/')


app.run(debug=True)
