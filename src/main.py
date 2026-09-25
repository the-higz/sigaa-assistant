from datetime import datetime
from scraper import coletar_dados
from output import gerar_arquivo

dados = coletar_dados()
atividades_ativas = []

agora = datetime.now()

for atividade in dados:

    data_convertida = datetime.strptime(
        atividade["data"],
        "%d/%m/%Y %H:%M"
    )

    situacao = data_convertida > agora

    atividade["ativa"] = situacao

    if atividade["ativa"]:
        atividades_ativas.append(atividade)

gerar_arquivo(atividades_ativas)