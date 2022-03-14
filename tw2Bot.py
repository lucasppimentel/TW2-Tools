from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time
from json import load


def atualizar_recursos(object_):
    madeira = object_.navegador.find_element_by_xpath(
        '//*[contains(@tooltip-before-show-args, "wood")]/div[2]/div')
    ferro = object_.navegador.find_element_by_xpath(
        '//*[contains(@tooltip-before-show-args, "iron")]/div[2]/div')
    argila = object_.navegador.find_element_by_xpath(
        '//*[contains(@tooltip-before-show-args, "clay")]/div[2]/div')
    return {"Madeira": madeira, "Ferro": ferro, "Argila": argila}

def atualizar_filas(object_):
    fila = object_.navegador.find_elements_by_xpath(
        '//div[contains(@tooltip-content, "Aprimorar p/")]')
    fila = list(map(lambda x: x.get_attribute("tooltip-content").split('-')[0].rstrip(), fila))
    return fila

# Coleta recompensa diaria
def coletar_recompensa(object_):
    try:
        object_.navegador.find_element_by_css_selector(
            '*[ng-click="claimReward()"]').click()  # Mudar  <------
    except NoSuchElementException:
        print("Recompensa diária não exibida!")
        pass

# Entra na visão da aldeia
def goto_aldeia(object_):
    tela_mundi = True
    while tela_mundi:
        try:
            WebDriverWait(object_.navegador, 2).until(
                EC.element_to_be_clickable((By.ID, 'village-zoom')))

        except TimeoutException:
            tela_mundi = False
            pass
        
        except ElementNotInteractableException:
            pass
        
        else:
            object_.navegador.find_element_by_id('village-zoom').click()
            time.sleep(1)

# Aprimora um edifício
def construir(object_, cons):
    goto_aldeia(object_)
    object_.navegador.find_element_by_xpath('//*[text()[contains(., "Edifício Principal")]]').click()
    object_.navegador.find_element_by_class_name('menu-highlight').click()
    object_.navegador.find_element_by_xpath(
        '//*[text()[contains(., "{}")]]/../../../../tr[4]/td/span'.format(cons)).click()
    object_.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()
    
def adicionar_unidade(object_, key, value):
    object_.navegador.find_element_by_xpath('//*[text()[contains(.,"{}")]]/../Input'.format(key)).send_keys(
        str(value))
    
def criar_predef(object_, nome, un_qnt):
    goto_aldeia(object_)
    object_.navegador.find_element_by_xpath('//*[text()[contains(., "Ponto de Encontro")]]').click()
    object_.navegador.find_element_by_class_name('menu-highlight').click()
    object_.navegador.find_element_by_css_selector('*[ng-click="createPreset();"]').click()
    object_.navegador.find_element_by_xpath('//input[@placeholder="Digite o nome da predefinição"]').send_keys(
        str(nome))
    object_.navegador.find_element_by_xpath('//*[text()[contains(.,"Salvar")]]/..').click()
    object_.navegador.find_element_by_xpath('//*[text()[contains(.,"Ok")]]/..').click()

    for unidade, quantidade in un_qnt.items():
        adicionar_unidade(object_, unidade, quantidade)

    object_.navegador.find_element_by_xpath('//*[text()[contains(.,"Salvar")]]/..').click()
    object_.navegador.find_element_by_css_selector('*[ng-click="closeWindow();"]').click()
    
    object_.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()

def deletar_predef(object_, nome):
    goto_aldeia(object_)
    object_.navegador.find_element_by_xpath('//*[text()[contains(., "Ponto de Encontro")]]').click()
    object_.navegador.find_element_by_class_name('menu-highlight').click()
    tmp = object_.navegador.find_element_by_xpath(
        "//span[contains(@class, 'preset-name text-normal ff-cell-fix') and text()='{}']".format(nome))
    tmp.find_element_by_xpath(".//ancestor::td/../td[10]/a").click()
    object_.navegador.find_element_by_css_selector('*[ng-click="submit($event)"]').click()
    object_.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]')

def desabilitar_dicas(object_):
    object_.navegador.find_element_by_class_name('icon-60x60-settings').click()
    object_.navegador.find_element_by_class_name('icon-44x44-settings-game').click()
    object_.navegador.find_element_by_id('settings-smart-tips').find_element_by_xpath('.//ancestor::label').click()
    object_.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()

# Recruta unidades
def recrutar(object_, un_id, qnt):
    goto_aldeia(object_)
    object_.navegador.find_element_by_xpath('//*[text()[contains(., "Quartel")]]').click()
    object_.navegador.find_element_by_class_name('menu-highlight').click()
    object_.navegador.find_element_by_xpath('//*[text()[contains(.,"{}")]]/../../../..'.format(un_id)).click()
    object_.navegador.find_element_by_xpath(
        '//*[text()[contains(.,"{}")]]/../../tr[3]/td/input'.format(un_id)).send_keys(qnt)
    object_.navegador.find_element_by_xpath(
        '//*[text()[contains(.,"{}")]]/../../tr[3]/td/input'.format(un_id)).send_keys(
        Keys.ENTER)
    object_.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()

# Salva as coordenadas das aldeias bárbaras DA LISTA DA PROVINCIA ABERTA NA HORA
def escanear_provincia(object_):
    lista = []
    occur = object_.navegador.find_elements_by_xpath('//td[text()[contains(., "Aldeia Bárbara")]]')
    for i in range(0, int(len(occur) / 2)):
        u = occur[i]
        coord = u.find_element_by_xpath(".//ancestor::tr/td[3]")
        lista.append(coord.get_attribute("innerHTML"))
    
    object_.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()

    return lista

def atacar(object_, coord, predef):
    object_.navegador.find_element_by_id('world-map').click()
    object_.navegador.find_element_by_css_selector('*[ng-model="coordinates.x"]').clear()
    object_.navegador.find_element_by_css_selector('*[ng-model="coordinates.x"]').send_keys(coord[:3])
    object_.navegador.find_element_by_css_selector('*[ng-model="coordinates.y"]').clear()
    object_.navegador.find_element_by_css_selector('*[ng-model="coordinates.y"]').send_keys(coord[6:])
    object_.navegador.find_element_by_css_selector('*[ng-model="coordinates.y"]').send_keys(Keys.ENTER)

    object_.navegador.find_element_by_xpath(
        '//div[contains(@tooltip-content, "Predefinições") and contains(@class, "border")]').click()
    
    B_desbug = object_.navegador.find_element_by_css_selector(
        '*[ng-click="editPreset(preset);"]')
    B_desbug.click()
    
    object_.navegador.find_element_by_css_selector(
        '*[ng-click="closeWindow();"]').click()
    
    tmp = object_.navegador.find_element_by_xpath(
        '//span[contains(@class, "preset-name text-normal ff-cell-fix") \
            and text()="{}"]'.format(predef))
    tmp.find_element_by_xpath('.//ancestor::td/../../tr[2]/td[3]/a').click()
    
    object_.navegador.find_element_by_css_selector(
        '*[ng-click="closeWindow();"]').click()


def load_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return load(f)

# A recursive function should make this acceptable
def coletar_missoes(object_, recursos):
    capacidade = load_json('C:/Users/Pichau/Desktop/projs/tw2bot/alpha/CapacidadeNivel.json')

    quests = object_.navegador.find_elements_by_css_selector('*[ng-click="openQuestLineModal(questLineModel);"]')
    for missao in quests:
        missao.click()
        subq = object_.navegador.find_elements_by_xpath(
            '//*[contains(@class, "text-overflow") and contains(text(), "Parte")]/..')
        for submiss in subq:
            submiss.click()

            try:
                botao = object_.navegador.find_element_by_css_selector('*[ng-click="finishQuest();"]')
            except NoSuchElementException:
                print("Concluida")
                pass
            else:
                if 'green' in botao.get_attribute('class'):
                    reward = object_.navegador.find_elements_by_xpath(
                        '//span[contains(@ng-init, "itemTitle = getDisplayedName(reward)")]')
                    reward = list(map(lambda x: x.text, reward))
                    caso = []

                    for rec in recursos:
                        reward_recursos = [(int(recursos[rec].replace('.', '')) +
                                            int(rew[:3]))
                                            for i, rew in enumerate(reward) if rec in rew]
                        caso.append(reward_recursos[0])

                    a = True
                    nivel_armazem = object_.navegador.find_element_by_xpath(
                        '//*[text()[contains(., " Armazém ")]]/../span[2]/span').text
                    for rew in caso:
                        if rew >= capacidade[nivel_armazem]:
                            a = False
                            break
                        else:
                            pass
                    if a:
                        botao.click()
                else:
                    pass
        object_.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()
    return 0

def isQueueEmpty(object_):
    try:
        object_.navegador.find_element_by_xpath(
            "//div[contains(@ng-if, '!queue[key]') and \
            contains(@tooltip-content, 'Abre a Janela do Edifício Principal')]")
    except NoSuchElementException:
        return False
    else:
        return True

def isRewardAvailable(object_):
    try:
        object_.navegador.find_element_by_xpath("//li[contains(@class, 'finishable') and \
            contains(@ng-click, 'openQuestLineModal(questLineModel);')]")
    except NoSuchElementException:
        print("No finishable quests found")
        return False
    else:
        print("Finishable quests found")
        return True

    print("Fim")