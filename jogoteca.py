from flask import Flask
from flask import render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)


@app.route('/inicio')
def ola():
    tetris = Jogo('Tetris', 'Puzzle', 'Atari')
    gow = Jogo('God of War', 'Rack n Slash', 'PS2')
    mk = Jogo('Mortal Kombat', 'Luta', 'PS2')
    lista = [tetris, gow, mk]
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run()
