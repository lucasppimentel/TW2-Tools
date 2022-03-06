from PyQt5 import QtCore, QtWidgets


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
from selenium.webdriver.common.keys import Keys
import json


def load_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


class Ui_MainWindow(object):
    # =========================PYQT Designer===================================
    def setupUi(self, MainWindow, path):
        
        self.navegador = webdriver.Chrome(path)
        self.navegador.implicitly_wait(2)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Fila = QtWidgets.QListWidget(self.centralwidget)
        self.Fila.setGeometry(QtCore.QRect(270, 30, 201, 251))
        self.Fila.setObjectName("Fila")
        self.C_Edificio = QtWidgets.QComboBox(self.centralwidget)
        self.C_Edificio.setGeometry(QtCore.QRect(270, 290, 121, 22))
        self.C_Edificio.setObjectName("C_Edificio")
        self.C_Edificio.addItem("")
        self.C_Edificio.addItem("")
        self.C_Edificio.addItem("")
        self.C_Edificio.addItem("")
        self.C_Edificio.addItem("")
        self.C_Edificio.addItem("")
        self.C_Edificio.addItem("")
        self.C_Edificio.addItem("")
        self.C_Edificio.addItem("")
        self.B_Construir = QtWidgets.QPushButton(self.centralwidget)
        self.B_Construir.setGeometry(QtCore.QRect(400, 290, 75, 23))
        self.B_Construir.setObjectName("B_Construir")
        self.B_Farmar = QtWidgets.QPushButton(self.centralwidget)
        self.B_Farmar.setGeometry(QtCore.QRect(20, 290, 81, 31))
        self.B_Farmar.setObjectName("B_Farmar")
        self.B_Escanear = QtWidgets.QPushButton(self.centralwidget)
        self.B_Escanear.setGeometry(QtCore.QRect(110, 290, 121, 31))
        self.B_Escanear.setObjectName("B_Escanear")
        self.Lista_Farm = QtWidgets.QListWidget(self.centralwidget)
        self.Lista_Farm.setGeometry(QtCore.QRect(20, 30, 211, 251))
        self.Lista_Farm.setObjectName("Lista_Farm")
        self.I_Coord_X = QtWidgets.QLineEdit(self.centralwidget)
        self.I_Coord_X.setGeometry(QtCore.QRect(20, 340, 81, 21))
        self.I_Coord_X.setObjectName("I_Coord_X")
        self.I_Coord_Y = QtWidgets.QLineEdit(self.centralwidget)
        self.I_Coord_Y.setGeometry(QtCore.QRect(110, 340, 81, 21))
        self.I_Coord_Y.setObjectName("I_Coord_Y")
        self.B_Add_Coords = QtWidgets.QPushButton(self.centralwidget)
        self.B_Add_Coords.setGeometry(QtCore.QRect(200, 340, 31, 23))
        self.B_Add_Coords.setObjectName("B_Add_Coords")
        self.Console = QtWidgets.QTextBrowser(self.centralwidget)
        self.Console.setGeometry(QtCore.QRect(20, 380, 751, 171))
        self.Console.setObjectName("Console")
        self.CB_Auto_farm = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_Auto_farm.setGeometry(QtCore.QRect(680, 30, 70, 17))
        self.CB_Auto_farm.setObjectName("CB_Auto_farm")
        self.CB_Auto_Build = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_Auto_Build.setGeometry(QtCore.QRect(680, 50, 70, 17))
        self.CB_Auto_Build.setObjectName("CB_Auto_Build")
        self.B_Atualizar_Rec = QtWidgets.QPushButton(self.centralwidget)
        self.B_Atualizar_Rec.setGeometry(QtCore.QRect(500, 20, 131, 41))
        self.B_Atualizar_Rec.setObjectName("B_Atualizar_Rec")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(680, 70, 101, 17))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 330, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 330, 47, 13))
        self.label_4.setObjectName("label_4")
        
        
        self.B_setup = QtWidgets.QPushButton(self.centralwidget)
        self.B_setup.setGeometry(QtCore.QRect(680, 260, 101, 41))
        self.B_setup.setObjectName("B_setup")
        self.B_tests = QtWidgets.QPushButton(self.centralwidget)
        self.B_tests.setGeometry(QtCore.QRect(500, 80, 75, 23))
        self.B_tests.setObjectName("B_tests")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.B_Farmar.clicked.connect(self.F_farm_click)
        self.B_Add_Coords.clicked.connect(self.F_add_coords)
        self.B_Atualizar_Rec.clicked.connect(self.F_atualizar_recursos)
        self.B_Construir.clicked.connect(self.F_Build)
        self.B_Escanear.clicked.connect(self.F_Scan)
        self.B_setup.clicked.connect(self.F_Setup)
        self.B_tests.clicked.connect(self.F_Tester)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.C_Edificio.setItemText(0, _translate("MainWindow", "Edifício Principal"))
        self.C_Edificio.setItemText(1, _translate("MainWindow", "Fazenda"))
        self.C_Edificio.setItemText(2, _translate("MainWindow", "Mercado"))
        self.C_Edificio.setItemText(3, _translate("MainWindow", "Quartel"))
        self.C_Edificio.setItemText(4, _translate("MainWindow", "Bosque"))
        self.C_Edificio.setItemText(5, _translate("MainWindow", "Mina de Ferro"))
        self.C_Edificio.setItemText(6, _translate("MainWindow", "Poço de Argila"))
        self.C_Edificio.setItemText(7, _translate("MainWindow", "Muralha"))
        self.C_Edificio.setItemText(8, _translate("MainWindow", "Armazém"))
        self.B_Construir.setText(_translate("MainWindow", "Construir"))
        self.B_Farmar.setText(_translate("MainWindow", "Farmar"))
        self.B_Escanear.setText(_translate("MainWindow", "Escanear Província"))
        self.B_Add_Coords.setText(_translate("MainWindow", "+"))
        self.CB_Auto_farm.setText(_translate("MainWindow", "Auto-Farm"))
        self.CB_Auto_Build.setText(_translate("MainWindow", "Auto-Build"))
        self.B_Atualizar_Rec.setText(_translate("MainWindow", "Atualizar Recursos"))
        self.checkBox.setText(_translate("MainWindow", "Auto-Rewards"))
        self.label.setText(_translate("MainWindow", "Alvos de Farm"))
        self.label_2.setText(_translate("MainWindow", "Fila de Construção"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        
        
        self.B_setup.setText(_translate("MainWindow", "Setup Predef"))
        self.B_tests.setText(_translate("MainWindow", "ForDev"))
        
        # Acordar worker2
        self.worker2 = First_Init()
        self.worker2.chrome = self.navegador
        self.worker2.start()
        self.worker2.finished.connect(self.F_after_init)
        
    
    def F_Tester(self):
        print("Test")
    
    def F_Setup(self):
        nome = "farm_pred"
        un_qnt = {"Lanceiro":1}

        self.criar_predef(nome, un_qnt)
    
    def F_after_init(self):
        self.navegador.implicitly_wait(2)
        self.coletar_recompensa()
        self.desabilitar_dicas()
        self.navegador.implicitly_wait(5)
        
        self.worker2.quit()
    
    def F_farm_click(self):
        print("Farm")
        for i in range(self.Lista_Farm.count()):
            alvo = self.Lista_Farm.item(i).text()
            self.atacar(alvo, "farm_pred")
            
    def F_add_coords(self):
        coord_x = self.I_Coord_X.text()
        coord_y = self.I_Coord_Y.text()
        
        coord = f"{coord_x} | {coord_y}"
        self.Lista_Farm.addItem(coord)
        
    def F_atualizar_recursos(self):
        self.worker = Resources_Worker()
        self.worker.chrome = self.navegador
        self.worker.start()
        
        self.worker.finished.connect(self.worker2.quit())
    
    def F_Build(self):
        print("Build")
        cons = self.C_Edificio.currentText()
        self.Fila.addItem(cons)
        
        # Acordar Builder
        print("Acordar")
        self.Builder = Builder_worker()
        self.Builder.navegador = self.navegador
        self.Builder.isQueueEmpty = self.isQueueEmpty
        self.Builder.construir = self.construir
        self.fila_cons =  [str(self.Fila.item(i).text()) for i in range(self.Fila.count())]
        self.Builder.fila_bot = self.fila_cons
        self.Builder.start()
        
        self.Builder.cons_built.connect(self.cons_built)
        self.Builder.finished.connect(self.Builder.quit())
    
    def F_Scan(self):
        print("Scan")
        alvos = self.escanear_provincia()
        self.Lista_Farm.addItems(alvos)
    
    def cons_built(self, val):
        self.Fila.takeItem(val)
    
    # ================================TWB======================================
    def atualizar_recursos(self):
        madeira = self.navegador.find_element_by_xpath(
            '//*[contains(@tooltip-before-show-args, "wood")]/div[2]/div').text
        ferro = self.navegador.find_element_by_xpath(
            '//*[contains(@tooltip-before-show-args, "iron")]/div[2]/div').text
        argila = self.navegador.find_element_by_xpath(
            '//*[contains(@tooltip-before-show-args, "clay")]/div[2]/div').text
        return {"Madeira": madeira, "Ferro": ferro, "Argila": argila}

    def atualizar_filas(self):
        fila = self.navegador.find_elements_by_xpath(
            '//div[contains(@tooltip-content, "Aprimorar p/")]')
        fila = list(map(lambda x: x.get_attribute("tooltip-content").split('-')[0].rstrip(), fila))
        return fila

    # Coleta recompensa diaria
    def coletar_recompensa(self):
        try:
            self.navegador.find_element_by_css_selector(
                '*[ng-click="claimReward()"]').click()  # Mudar  <------
        except NoSuchElementException:
            print("Recompensa diária não exibida!")
            pass

    # Entra na visão da aldeia
    def goto_aldeia(self):
        tela_mundi = True
        while tela_mundi:
            try:
                WebDriverWait(self.navegador, 2).until(
                    EC.element_to_be_clickable((By.ID, 'village-zoom')))

            except TimeoutException:
                tela_mundi = False
                pass
            
            except ElementNotInteractableException:
                pass
            
            else:
                self.navegador.find_element_by_id('village-zoom').click()
                time.sleep(1)

    # Aprimora um edifício
    def construir(self, cons):
        self.goto_aldeia()
        self.navegador.find_element_by_xpath('//*[text()[contains(., "Edifício Principal")]]').click()
        self.navegador.find_element_by_class_name('menu-highlight').click()
        self.navegador.find_element_by_xpath(
            '//*[text()[contains(., "{}")]]/../../../../tr[4]/td/span'.format(cons)).click()
        self.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()
        
    def adicionar_unidade(self, key, value):
        self.navegador.find_element_by_xpath('//*[text()[contains(.,"{}")]]/../Input'.format(key)).send_keys(
            str(value))
        
    def criar_predef(self, nome, un_qnt):
        self.goto_aldeia()
        self.navegador.find_element_by_xpath('//*[text()[contains(., "Ponto de Encontro")]]').click()
        self.navegador.find_element_by_class_name('menu-highlight').click()
        self.navegador.find_element_by_css_selector('*[ng-click="createPreset();"]').click()
        self.navegador.find_element_by_xpath('//input[@placeholder="Digite o nome da predefinição"]').send_keys(
            str(nome))
        self.navegador.find_element_by_xpath('//*[text()[contains(.,"Salvar")]]/..').click()
        self.navegador.find_element_by_xpath('//*[text()[contains(.,"Ok")]]/..').click()

        for unidade, quantidade in un_qnt.items():
            self.adicionar_unidade(unidade, quantidade)

        self.navegador.find_element_by_xpath('//*[text()[contains(.,"Salvar")]]/..').click()
        self.navegador.find_element_by_css_selector('*[ng-click="closeWindow();"]').click()
        
        self.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()

    def deletar_predef(self, nome):
        self.goto_aldeia()
        self.navegador.find_element_by_xpath('//*[text()[contains(., "Ponto de Encontro")]]').click()
        self.navegador.find_element_by_class_name('menu-highlight').click()
        tmp = self.navegador.find_element_by_xpath(
            "//span[contains(@class, 'preset-name text-normal ff-cell-fix') and text()='{}']".format(nome))
        tmp.find_element_by_xpath(".//ancestor::td/../td[10]/a").click()
        self.navegador.find_element_by_css_selector('*[ng-click="submit($event)"]').click()
        self.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]')

    def desabilitar_dicas(self):
        self.navegador.find_element_by_class_name('icon-60x60-settings').click()
        self.navegador.find_element_by_class_name('icon-44x44-settings-game').click()
        self.navegador.find_element_by_id('settings-smart-tips').find_element_by_xpath('.//ancestor::label').click()
        self.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()

    # Recruta unidades
    def recrutar(self, un_id, qnt):
        self.goto_aldeia()
        self.navegador.find_element_by_xpath('//*[text()[contains(., "Quartel")]]').click()
        self.navegador.find_element_by_class_name('menu-highlight').click()
        self.navegador.find_element_by_xpath('//*[text()[contains(.,"{}")]]/../../../..'.format(un_id)).click()
        self.navegador.find_element_by_xpath(
            '//*[text()[contains(.,"{}")]]/../../tr[3]/td/input'.format(un_id)).send_keys(qnt)
        self.navegador.find_element_by_xpath(
            '//*[text()[contains(.,"{}")]]/../../tr[3]/td/input'.format(un_id)).send_keys(
            Keys.ENTER)
        self.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()

    # Salva as coordenadas das aldeias bárbaras DA LISTA DA PROVINCIA ABERTA NA HORA
    def escanear_provincia(self):
        lista = []
        occur = self.navegador.find_elements_by_xpath('//td[text()[contains(., "Aldeia Bárbara")]]')
        for i in range(0, int(len(occur) / 2)):
            u = occur[i]
            coord = u.find_element_by_xpath(".//ancestor::tr/td[3]")
            lista.append(coord.get_attribute("innerHTML"))
        
        self.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()

        return lista

    def atacar(self, coord, predef):
        self.navegador.find_element_by_id('world-map').click()
        self.navegador.find_element_by_css_selector('*[ng-model="coordinates.x"]').clear()
        self.navegador.find_element_by_css_selector('*[ng-model="coordinates.x"]').send_keys(coord[:3])
        self.navegador.find_element_by_css_selector('*[ng-model="coordinates.y"]').clear()
        self.navegador.find_element_by_css_selector('*[ng-model="coordinates.y"]').send_keys(coord[6:])
        self.navegador.find_element_by_css_selector('*[ng-model="coordinates.y"]').send_keys(Keys.ENTER)

        self.navegador.find_element_by_xpath(
            '//div[contains(@tooltip-content, "Predefinições") and contains(@class, "border")]').click()
        
        B_desbug = self.navegador.find_element_by_css_selector(
            '*[ng-click="editPreset(preset);"]')
        B_desbug.click()
        
        self.navegador.find_element_by_css_selector(
            '*[ng-click="closeWindow();"]').click()
        
        tmp = self.navegador.find_element_by_xpath(
            '//span[contains(@class, "preset-name text-normal ff-cell-fix") \
                and text()="{}"]'.format(predef))
        tmp.find_element_by_xpath('.//ancestor::td/../../tr[2]/td[3]/a').click()
        
        self.navegador.find_element_by_css_selector(
            '*[ng-click="closeWindow();"]').click()
        
    # Refaz essa merda ne
    def coletar_missoes(self, recursos):
        

        capacidade = load_json('C:/Users/Pichau/Desktop/projs/tw2bot/alpha/CapacidadeNivel.json')

        quests = self.navegador.find_elements_by_css_selector('*[ng-click="openQuestLineModal(questLineModel);"]')
        for missao in quests:
            missao.click()
            subq = self.navegador.find_elements_by_xpath(
                '//*[contains(@class, "text-overflow") and contains(text(), "Parte")]/..')
            for submiss in subq:
                submiss.click()

                try:
                    botao = self.navegador.find_element_by_css_selector('*[ng-click="finishQuest();"]')
                except NoSuchElementException:
                    print("Concluida")
                    pass
                else:
                    if 'green' in botao.get_attribute('class'):
                        reward = self.navegador.find_elements_by_xpath(
                            '//span[contains(@ng-init, "itemTitle = getDisplayedName(reward)")]')
                        reward = list(map(lambda x: x.text, reward))
                        caso = []

                        for rec in recursos:
                            reward_recursos = [(int(recursos[rec].replace('.', '')) +
                                                int(rew[:3]))
                                               for i, rew in enumerate(reward) if rec in rew]
                            caso.append(reward_recursos[0])

                        a = True
                        nivel_armazem = self.navegador.find_element_by_xpath(
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
            self.navegador.find_element_by_css_selector('*[ng-click="closeWindow()"]').click()
        return 0
    
    def isQueueEmpty(self):
        try:
            self.navegador.find_element_by_xpath(
                "//div[contains(@ng-if, '!queue[key]') and \
                contains(@tooltip-content, 'Abre a Janela do Edifício Principal')]")
        except NoSuchElementException:
            return False
        else:
            return True
    
    # =========================================================================

class Resources_Worker(QtCore.QThread):
    def run(self):
        print(self.atualizar_recursos())

class First_Init(QtCore.QThread):
    def run(self):
        self.chrome.get('https://br.tribalwars2.com/page#/')
        
        waiting = True
        while waiting:
            try:
                WebDriverWait(self.chrome, 5).until(
                    EC.title_contains("Tribal Wars 2 (")
                )
            except TimeoutException:
                print("Faça login e selecione um mundo")
                pass
            except WebDriverException:
                print("Exceção: chrome nr")
            else:
                waiting = False
        
        # Espera fim do loading
        waiting = True
        while waiting:
            try:
                WebDriverWait(self.chrome, 5).until(
                    EC.invisibility_of_element_located((By.ID, 'screen-loading'))
                )
            except TimeoutException:
                print("Carregando...")
                pass
            else:
                waiting = False

class Builder_worker(QtCore.QThread):
    cons_built = QtCore.pyqtSignal(int)
    
    def run(self):
        print("Builder working...")
        
        if len(self.fila_bot) == 0:
            print("Sem fila")
            
        elif self.isQueueEmpty():
            cons = self.fila_bot[0]
            print(cons)
            
            # Signal que a construção foi feita
            self.cons_built.emit(0)
            
            self.construir(cons)
            print("Feito")
            
        else:
            print("Fila cheia")



if __name__ == "__main__":
    print("Not main")
