from jogoteca import app
from flask import render_template, request, redirect
from flask import session, flash
from flask import url_for
from models import Usuarios
from helpers import FormularioLogin
from flask_bcrypt import check_password_hash


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioLogin()
    return render_template('login.html', proxima=proxima, form=form)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioLogin(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(f'Usuário {usuario.nickname} logado com sucesso.')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    flash('Usuário não logado.')
    return redirect(url_for('login', proxima=url_for('novo')))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect(url_for('index'))
