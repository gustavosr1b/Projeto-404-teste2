import sqlite3

# cursor.execute("CREATE TABLE chamados (categoria text,data date,descricao text,local text,status text,nome_responsavel text, id_responsavel text, prioridade integer, sms boolean, email boolean, arquivos text)")

# cursor.execute("INSERT INTO chamados VALUES('Windows','29/08/2022','Meu Windows não está carregando','10º Andar - SP','Em andamento','Gustavo Ribeiro',50394017870,2,True,False,'test')")

# banco.commit()

#cursor.execute("SELECT * FROM chamados3")
#print(cursor.fetchall())

def listar_chamados(cliente_ativo):
    banco = sqlite3.connect('dados/gotech_suporte.db')
    c = banco.cursor()
    c.execute("SELECT * from chamados where id_responsavel = " + cliente_ativo)
    lista_chamados = c.fetchall()
    banco.commit()
    return lista_chamados


def criar_chamado(dados_chamado):
    banco = sqlite3.connect('dados/gotech_suporte.db')
    c = banco.cursor()
    c.execute("INSERT INTO chamados (categoria, data, descricao, local, status, nome_responsavel, id_responsavel, prioridade, sms, email, arquivos) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(dados_chamado.categoria,dados_chamado.data,dados_chamado.descricao,dados_chamado.local,dados_chamado.status,dados_chamado.nome_responsavel,dados_chamado.id_responsavel,dados_chamado.prioridade,dados_chamado.sms,dados_chamado.email,dados_chamado.arquivos))
    c.execute("SELECT max(id) from chamados where id_responsavel = " + str(dados_chamado.id_responsavel))
    auto_id = c.fetchall()[0][0]
    banco.commit()
    return str(auto_id)

def deletar_chamado(id_chamado, cliente_ativo):
    banco = sqlite3.connect('dados/gotech_suporte.db')
    c = banco.cursor()
    c.execute("DELETE FROM chamados where id = " + str(id_chamado) + " and id_responsavel = " + str(cliente_ativo))
    banco.commit()


