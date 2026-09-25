from processor import filtrar_ativas, processar_atividades
from scraper import coletar_dados
from output import gerar_arquivo

dados = coletar_dados()

dados = processar_atividades(dados)

atividades_ativas = filtrar_ativas(dados)

gerar_arquivo(atividades_ativas)