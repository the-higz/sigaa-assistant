from processor import processar_atividades
from scraper import coletar_dados
from output import gerar_arquivo

dados = coletar_dados()

dados = processar_atividades(dados)

atividades_ativas = []

for atividade in dados:

    if atividade["ativa"]:
        atividades_ativas.append(atividade)

gerar_arquivo(atividades_ativas)