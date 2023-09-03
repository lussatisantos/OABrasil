from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

numero_oab = 133864

# entrar no site https://pje-consulta-publica.tjmg.jus.br/pje/ConsultaPublica/listView.seam
driver = webdriver.Chrome()
driver.get('https://pje-consulta-publica.tjmg.jus.br/pje/ConsultaPublica/listView.seam')
sleep(30)

# digitar numero oab
campo_oab = driver.find_element(By.XPATH, "input[@id='fPP:Decoration:numeroOAB']")
campo_oab.send_keys(numero_oab)

#Selecionar estado
dropdown_estados = driver.find_element(By.XPAT, "//select[@id='fPP:Decoration:estadoComboOAB']")
opcoes_estados = Select(dropdown_estados)
opcoes_estados.select_by_visible_text('SP')

# clicar em pesquisar
botao_pesquisar = driver.find_element(By.XPATH, "//input[@id='fPP:searchProcessos']")
botao_pesquisar.click()
sleep(10)

# entrar em cada um do processo
#extrair o n* processo e data de distribuicao
# extrair e guardas todos os ultimos moviementos
# guardar tudo no excel, separados por processo

