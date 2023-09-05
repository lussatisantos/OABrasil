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
campo_oab = driver.find_element(By.XPATH, "//input[@id='fPP:Decoration:numeroOAB']")
campo_oab.send_keys(numero_oab)

#Selecionar estado
dropdown_estados = driver.find_element(By.XPATH, "//select[@id='fPP:Decoration:estadoComboOAB']")
opcoes_estados = Select(dropdown_estados)
opcoes_estados.select_by_visible_text('SP')

# clicar em pesquisar
botao_pesquisar = driver.find_element(By.XPATH, "//input[@id='fPP:searchProcessos']")
botao_pesquisar.click()
sleep(10)

# entrar em cada um do processo
processos = driver.find_elements(By.XPATH, "//b[@class='btn-block']")
for precesso in processos:
    precesso.click()
    sleep(10)
    janelas = driver.windows_handles
    driver.switch_to.windows(janelas[-1])
    driver.set_window_size(1920, 1080)
    numero_processo = driver.find_elements(By.XPATH, "//div[@class='col-sm-12 ']")
    numero_processo = numero_processo[0]
    numero_processo = numero_processo.text

    data_distribuicao = driver.find_elements(By.XPATH, "//div[@class='value col-sm-12 ']")
    data_distribuicao = data_distribuicao[1]
    data_distribuicao = data_distribuicao.text

#extrair o n* processo e data de distribuicao
# extrair e guardas todos os ultimos moviementos
# guardar tudo no excel, separados por processo

