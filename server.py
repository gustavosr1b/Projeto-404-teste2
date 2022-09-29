from flask import Flask, render_template, request, redirect, url_for
from datetime import date

from classes import Chamado
import banco_dados

app = Flask(__name__)

chamados = []

usuario_ativo = ['50394017870', 'gustavosr1b', 'gustavo@gmail.com','Gustavo RIbeiro'] #Usuário ativo no momento

def atualizar_lista_chamados(): #Função para atualizar a lista de chamados do Dashboard
    chamados_lista = banco_dados.listar_chamados(usuario_ativo[0])

    chamados.clear()
    for i in chamados_lista:
        chamados.append(Chamado(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], [8], i[9], i[10], i[11]))


@app.route('/')
def login():
    if(usuario_ativo is None):
        return render_template('login.html')
    else:
        return redirect(url_for('index'))

@app.route('/index')
def index():
    atualizar_lista_chamados()

    if request.args.get('idchamados') is None:
        return render_template('index.html', chamados=chamados, idchamados=-1)
    else:
        return render_template('index.html', chamados=chamados, idchamados=int(request.args.get('idchamados')))


@app.route('/admin')
def admin():
    return render_template('dashboard-admin.html')

@app.route('/perfil')
def perfil():
    return render_template('profile.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/abrir-chamado')
def abrirchamado():
    return render_template('criar-chamado.html')


@app.route('/atualizar-chamado')
def atualizarchamado():
    return render_template('atualizar-chamado.html')

@app.route('/ver_chamado/<int:idchamado>')
def ver_chamado(idchamado):
    atualizar_lista_chamados()

    for i in range(0, len(chamados)): #For para identificar em qual linha está o chamado na lista
        if chamados[i].id == idchamado:
            idchamado = i
            break

    return render_template('modal-ver-chamado.html', chamados=chamados, idchamado=idchamado)

@app.route('/excluir_chamado/<int:idchamado>')
def excluir_chamado(idchamado):
    return render_template('modal-excluir-chamado.html', chamados=chamados, idchamado=idchamado)

@app.route('/excluir_chamado/<int:idchamado>/excluir')
def excluir_chamado_confirmar(idchamado): #Função para deletar um chamado
    banco_dados.deletar_chamado(idchamado, usuario_ativo[0])

    return redirect(url_for('index'))


@app.route('/abrir-chamado/criar', methods=['POST'])
def criarchamado(): #Função para criar chamado
    if request.method == 'POST':
        criar_chamado_titulo = request.form.get('titulo')
        criar_chamado_descricao = request.form.get('descricao')
        criar_chamado_local = request.form.get('local')
        criar_chamado_prioridade = request.form.get('prioridade-chamado')
        criar_chamado_email = request.form.get('email')
        criar_chamado_sms = request.form.get('sms')
        criar_chamado_data = date.today().strftime("%d/%m/%Y")

        if (criar_chamado_email == 'on'):
            criar_chamado_email = True
        else:
            criar_chamado_email = False

        if (criar_chamado_sms == 'on'):
            criar_chamado_sms = True
        else:
            criar_chamado_sms = False

        criar_chamado_dados = Chamado('',criar_chamado_titulo, #Monta o chamado
                        criar_chamado_data,
                        criar_chamado_descricao,
                        criar_chamado_local,
                        'Aguardando atendimento',
                        usuario_ativo[3],
                        usuario_ativo[0],
                        criar_chamado_prioridade,
                        criar_chamado_email,
                        criar_chamado_sms,
                        '')

        novo_id = banco_dados.criar_chamado(criar_chamado_dados)

        return redirect(url_for('ver_chamado', idchamado=novo_id))
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
