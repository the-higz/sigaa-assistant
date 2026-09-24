
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://sigaa.sistemas.ufcat.edu.br/sigaa/verTelaLogin.do")

print("Faça login e pressione ENTER quando terminar")

input()

driver.quit()