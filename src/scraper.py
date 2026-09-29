from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()

usuario = os.getenv("SIGAA_USER")
senha = os.getenv("SIGAA_PASSWORD")

def fazer_login(driver):
    campo_usuario = driver.find_element(By.NAME, "user.login")
    campo_usuario.send_keys(usuario)

    campo_senha = driver.find_element(By.NAME, "user.senha")
    campo_senha.send_keys(senha)

    botao = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Entrar"]')

    botao.click()

def coletar_dados():
    driver = webdriver.Chrome()
    driver.get("https://sigaa.sistemas.ufcat.edu.br/sigaa/verTelaLogin.do")

    fazer_login(driver)

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
