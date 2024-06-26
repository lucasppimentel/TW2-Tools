from PyQt5 import QtCore, QtWidgets
import tw2Bot as twb

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
#import time
#from selenium.webdriver.common.keys import Keys
import json
import time


def load_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


class Ui_MainWindow(object):
    # =========================PYQT Designer===================================
    def setupUi(self, MainWindow, path):

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
        #self.B_Atualizar_Rec = QtWidgets.QPushButton(self.centralwidget)
        #self.B_Atualizar_Rec.setGeometry(QtCore.QRect(500, 20, 131, 41))
        #self.B_Atualizar_Rec.setObjectName("B_Atualizar_Rec")
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
        
        self.B_Farmar.clicked.connect(self.Button_farm_click)
        self.B_Add_Coords.clicked.connect(self.Button_add_coords_click)
        self.B_Construir.clicked.connect(self.Button_build_click)
        self.B_Escanear.clicked.connect(self.Button_scan_click)
        self.B_setup.clicked.connect(self.Button_setup_army_click)
        self.B_tests.clicked.connect(self.Button_test_click)
        self.CB_Auto_farm.stateChanged.connect(self.AutoFarm_checked)

        # Setup manager thread
        self.Manager = Manager_worker()

        self.Manager.reward_available_signal.connect(self.collect_rewards)
        self.Manager.farm_signal.connect(self.Button_farm_click)
        self.Manager.cons_built_signal.connect(self.cons_built)
        
        

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
        #self.B_Atualizar_Rec.setText(_translate("MainWindow", "Atualizar Recursos"))
        self.checkBox.setText(_translate("MainWindow", "Auto-Rewards"))
        self.label.setText(_translate("MainWindow", "Alvos de Farm"))
        self.label_2.setText(_translate("MainWindow", "Fila de Construção"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        
        
        self.B_setup.setText(_translate("MainWindow", "Setup Predef"))
        self.B_tests.setText(_translate("MainWindow", "ForDev"))
        
    def setupBrowser(self, browser_path):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.navegador = webdriver.Chrome(browser_path, options=options)
        self.navegador.implicitly_wait(2)

        # Setup browser on all threads
        self.Manager.navegador = self.navegador

        # Acordar worker2
        self.worker2 = First_Init()
        self.worker2.chrome = self.navegador
        self.worker2.start()
        self.worker2.finished.connect(self.F_after_init)


    def AutoFarm_checked(self):
        if self.CB_Auto_farm.isChecked:
            self.Manager.auto_attack = True
        else:
            self.Manager.auto_attack = False

    def Button_test_click(self):
        self.Manager.awaken = False
    
    def Button_setup_army_click(self):
        nome = "farm_pred"
        un_qnt = {"Lanceiro":1}

        twb.criar_predef(self, nome, un_qnt)
    
    def F_after_init(self):
        self.navegador.implicitly_wait(2)
        twb.coletar_recompensa(self)
        twb.desabilitar_dicas(self)
        self.navegador.implicitly_wait(5)
        self.resources = twb.atualizar_recursos(self)
        
        self.worker2.quit()

        self.Manager.start()
    
    def Button_farm_click(self):
        print("Farm")
        for i in range(self.Lista_Farm.count()):
            alvo = self.Lista_Farm.item(i).text()
            twb.atacar(self, alvo, "farm_pred")

        self.Manager.now = time.time()
            
    def Button_add_coords_click(self):
        coord_x = self.I_Coord_X.text()
        coord_y = self.I_Coord_Y.text()
        
        coord = f"{coord_x} | {coord_y}"
        self.Lista_Farm.addItem(coord)
    
    def Button_build_click(self):
        print("Build")
        cons = self.C_Edificio.currentText()
        self.Fila.addItem(cons)
        
        self.fila_cons =  [str(self.Fila.item(i).text()) for i in range(self.Fila.count())]
        self.Manager.Fila = self.fila_cons
        
        self.Manager.the_ui_know_Q = False
    
    def build_cons(self):
        self.fila_cons =  [str(self.Fila.item(i).text()) for i in range(self.Fila.count())]
        self.Manager.Fila = self.fila_cons
    
    def Button_scan_click(self):
        print("Scan")
        alvos = twb.escanear_provincia(self)
        self.Lista_Farm.addItems(alvos)
    
    def cons_built(self, val):
        self.Fila.takeItem(val)
        self.fila_cons =  [str(self.Fila.item(i).text()) for i in range(self.Fila.count())]
        self.Manager.Fila = self.fila_cons
        self.Manager.the_ui_know_Q = False

    def collect_rewards(self):
        #resources = {"Madeira": self.resources["Madeira"].text, "Ferro": self.resources["Ferro"].text, "Argila": self.resources["Argila"].text}
        #print(resources)
        #twb.coletar_missoes(self, resources) # Should have the builder thread doing it
        #self.Manager.the_ui_know_R = False
        print("I should collect my rewards")

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
        
        self.quit()

class Manager_worker(QtCore.QThread):
    # Signals
    cons_built_signal = QtCore.pyqtSignal(int)
    reward_available_signal = QtCore.pyqtSignal(bool)
    farm_signal = QtCore.pyqtSignal(bool)

    def run(self):
        print("Manager awaken")
        self.the_ui_know_Q = False
        self.the_ui_know_R = False
        self.the_ui_know_A = False
        self.auto_attack = False
        self.Fila = False
        self.can_build = False
        self.attack_in = 20
        self.now = time.time()
        self.awaken = True

        while self.awaken:
            queue_empty = twb.isQueueEmpty(self)
            time_since_last_attack = self.now - time.time()
            reward_available = twb.isRewardAvailable(self)

            # Attack
            if (time_since_last_attack > self.attack_in) and (not self.the_ui_know_A ) and (self.auto_attack):
                self.farm_signal.emit(True) # Same as clicking the "Farm" button

                print("Time to attack")
                self.the_ui_know_A = True

            # Building
            if queue_empty and (not self.the_ui_know_Q):
                self.can_build = True

                print("Queue empty")
                self.the_ui_know_Q = True

            # Rewards
            if reward_available and (not self.the_ui_know_R):
                self.reward_available_signal.emit(True)

                print("Rewards available")
                self.the_ui_know_R = True

            if self.can_build and self.Fila:
                print("Trying to build")
                self.build(self.Fila[0])

                self.the_ui_know_Q = False
        
        print("Manager sleeping")
        self.quit()
    
    def build(self, cons):
        print("Builder working...")
        
        if len(self.Fila) == 0:
            print("Sem fila")
            
        else:
            cons = self.Fila[0]
            print(cons)
            
            try:
                twb.construir(self, cons)
            except:
                print("Can't build")
            else:
                # Signal que a construção foi feita
                self.cons_built_signal.emit(0)
                print("Feito")
    

if __name__ == "__main__":
    print("Not main")
