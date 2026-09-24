from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://sigaa.sistemas.ufcat.edu.br/sigaa/verTelaLogin.do")


wait = WebDriverWait(driver, 100)

wait.until(EC.url_to_be("https://sigaa.sistemas.ufcat.edu.br/sigaa/portais/discente/discente.jsf"))

atividades = driver.find_elements(
    By.CSS_SELECTOR,
    "#avaliacao-portal tbody tr"
)
    
lista_atividades = []

for atividade in atividades:
    colunas = atividade.find_elements(By.TAG_NAME, "td")

    data = colunas[1].text
    informaçoes = colunas[2].text.split("\n")
    disciplina = informaçoes[0]
    tipo_nome = informaçoes[1].split(":")
    tipo = tipo_nome[0]
    nome = tipo_nome[1].lstrip()

    lista_atividades.append({'data': data, 'disciplina': disciplina, "tipo": tipo, "nome": nome})

for element in lista_atividades:
    print(element)
    print()

driver.quit()