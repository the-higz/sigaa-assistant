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
    "#avaliacao-portal tr"
)

for atividade in atividades:
    print(atividade.text)

input()

driver.quit()