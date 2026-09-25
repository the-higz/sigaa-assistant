from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

def coletar_dados():
    driver = webdriver.Chrome()
    driver.get("https://sigaa.sistemas.ufcat.edu.br/sigaa/verTelaLogin.do")


    wait = WebDriverWait(driver, 100)
    wait.until(EC.url_to_be("https://sigaa.sistemas.ufcat.edu.br/sigaa/portais/discente/discente.jsf"))

    atividades = driver.find_elements(By.CSS_SELECTOR,"#avaliacao-portal tbody tr")

    dados = []

    for atividade in atividades:
        colunas = atividade.find_elements(By.TAG_NAME, "td")

        informacoes = colunas[2].text.split("\n")

        disciplina = informacoes[0]

        tipo_nome = informacoes[1].split(":")
        tipo = tipo_nome[0]
        nome = tipo_nome[1].lstrip()

        data_dias = colunas[1].text.split(" ")

        if tipo == "Avaliação":
            data = data_dias[0] + " 23:59"
        else:
            data = data_dias[0] + " " + data_dias[1]

        dados.append({
            "data": data,
            "disciplina": disciplina,
            "tipo": tipo,
            "nome": nome
        }   )

    driver.quit()
    return dados
