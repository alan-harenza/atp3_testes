# instalacao bibliotecas

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# garantia de ter o ultima versao webdriver manager instalado
servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)

# buscando pagina do correio no google chrome
site = "https://buscacepinter.correios.com.br/app/endereco/index.php"
browser.get(site)
# tempo de espera para garantia de tudo carregar
time.sleep(3)
# setando uma variavel com o cep a ser buscado
cep = "02911120"
# encontrando o campo de busca
browser.find_element(By.NAME, 'endereco').send_keys(cep)
# tempo de espera para garantia de tudo carregar
time.sleep(3)
# clicando no botao "Buscar"
browser.find_element(By.NAME, 'btn_pesquisar').click()
# tempo de espera para garantia de tudo carregar
time.sleep(4)
# retirando a informacao deo enderco
endereco = browser.find_element(By.XPATH, "/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]").text
bairro = browser.find_element(By.XPATH, "/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[2]").text
cidade = browser.find_element(By.XPATH, "/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[3]").text
# tempo de espera para garantia de tudo carregar
time.sleep(2)
# encerrando instancia browser
browser.quit()
# mostrando resultados
resultado_final = endereco + '\n' + bairro + '\n' + cidade
print(resultado_final)
