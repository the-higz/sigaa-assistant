from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://sigaa.sistemas.ufcat.edu.br/sigaa/verTelaLogin.do")


wait = WebDriverWait(driver, 100)

wait.until(EC.url_to_be("https://sigaa.sistemas.ufcat.edu.br/sigaa/portais/discente/discente.jsf"))

atividades = driver.find_elements(
    By.CSS_SELECTOR,
    "#avaliacao-portal tbody tr"
)
    
lista_atividades = []
atividades_ativas = []

for atividade in atividades:
    colunas = atividade.find_elements(By.TAG_NAME, "td")

    informaçoes = colunas[2].text.split("\n")
    disciplina = informaçoes[0]
    tipo_nome = informaçoes[1].split(":")
    nome = tipo_nome[1].lstrip()
    tipo = tipo_nome[0]

    data_dias = colunas[1].text.split(" ")
    
    if(tipo == "Avaliação"):
        data = data_dias[0]
        data_convertida = datetime.strptime(data, "%d/%m/%Y")
    else:
        data = data_dias[0] + " " + data_dias[1]
        data_convertida = datetime.strptime(data, "%d/%m/%Y %H:%M")
        
    agora = datetime.now()

    situacao = data_convertida > agora


    lista_atividades.append({'data': data, 'disciplina': disciplina, "tipo": tipo, "nome": nome, 'ativa': situacao})


for atividade in lista_atividades:
    if atividade["ativa"]:
        atividades_ativas.append(atividade)

for atividade in atividades_ativas:
    print(atividade)
    print()

driver.quit()