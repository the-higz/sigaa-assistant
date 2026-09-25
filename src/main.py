from datetime import datetime
from selenium.webdriver.common.by import By
from scraper import coletar_dados

dados = coletar_dados()
atividades_ativas = []

agora = datetime.now()

for atividade in dados:

    data = atividade["data"]

    data_convertida = datetime.strptime(
        atividade["data"],
        "%d/%m/%Y %H:%M"
    )

    situacao = data_convertida > agora

    atividade["ativa"] = situacao

    if atividade["ativa"]:
        atividades_ativas.append(atividade)

with open("atividades.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("=== SIGAA ASSISTANT ===\n")

    for atividade in atividades_ativas:
        arquivo.write(f"📅 {atividade['data']}\n")
        arquivo.write(f"📚 {atividade['disciplina']}\n")
        arquivo.write(f"📝 {atividade['tipo']}: {atividade['nome']}\n\n")