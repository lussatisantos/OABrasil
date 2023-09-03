from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# entrar no site https://pje-consulta-publica.tjmg.jus.br/pje/ConsultaPublica/listView.seam
driver = webdriver.Chrome()
driver.get('https://pje-consulta-publica.tjmg.jus.br/pje/ConsultaPublica/listView.seam')
print()
sleep(30)
# digitar numero oab e selecionar estado
# clicar em pesquisar
# entrar em cada um do processo
#extrair o n* processo e data de distribuicao
# extrair e guardas todos os ultimos moviementos
# guardar tudo no excel, separados por processo

