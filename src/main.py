from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://sigaa.sistemas.ufcat.edu.br/sigaa/verTelaLogin.do")

wait = WebDriverWait(driver, 10)
wait.until(EC.url_to_be("https://sigaa.sistemas.ufcat.edu.br/sigaa/portais/discente/discente.jsf"))

driver.quit()