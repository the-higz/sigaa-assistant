import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://sigaa.sistemas.ufcat.edu.br/sigaa/verTelaLogin.do")

time.sleep(10)

driver.quit()