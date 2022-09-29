class Chamado:
    def __init__(self,id,categoria,data,descricao,local,status,nome_responsavel, id_responsavel, prioridade, sms, email, arquivos):
        self.id = id
        self.data = data
        self.categoria = categoria
        self.descricao = descricao
        self.local = local
        self.status = status
        self.nome_responsavel = nome_responsavel
        self.id_responsavel = id_responsavel
        self.prioridade = prioridade
        self.sms = sms
        self.email = email
        self.arquivos = arquivos