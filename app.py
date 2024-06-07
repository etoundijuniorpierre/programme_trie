import sys
from PySide2 import QtWidgets, QtGui
from pathlib import Path
from PyQt5.QtWidgets import *
from gc import isenabled
import shutil


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trie de Fichiers")
        self.interface()
        self.button_click()
        self.setup_css()


#notre interface
    def interface(self):
        self.layout = QtWidgets.QFormLayout(self)

        self.boxanalasyFolder = QtWidgets.QLineEdit()#zone de saisie link du dossier à analyser
        self.boxanalasyFolder.setPlaceholderText("Choisir le lien dossier à analyser")#fonction placeholdertext() pour donner les description d'un box sa saisie 

        self.btnOuvrir = QtWidgets.QPushButton("Ouvrir Répertoire")
        self.btnOuvrir.clicked.connect(self.open_folder_dialog)

        self.choix0 = QtWidgets.QCheckBox("folder")
        self.choix0.stateChanged.connect(self.changecheck)
        self.choix1 = QtWidgets.QCheckBox("extension")
        self.choix1.stateChanged.connect(self.changecheck)
        self.choix2 = QtWidgets.QCheckBox("files")
        self.choix2.stateChanged.connect(self.changecheck)
        

        self.boxchoixtrie = QtWidgets.QLineEdit()#zone saisie de l'extension
        self.boxchoixtrie.setPlaceholderText("Saisir extension")

        self.boxcreateFolder = QtWidgets.QLineEdit()#zone saisie nom du dossier à créer
        self.boxcreateFolder.setPlaceholderText("Saisir nom dossier à créer")

        self.button = QtWidgets.QPushButton("démarrer")


        self.layout.addRow("Reposotory :", self.boxanalasyFolder)
        #self.label1 = QtWidgets.QLabel("Entrer lien dossier à analyser", self.boxanalasyFolder)#text indicatif des fonctions de chaque zone de saisie 

        self.layout.addWidget(self.btnOuvrir)

        self.layout.addWidget(self.choix0)
        self.layout.addWidget(self.choix1)
        self.layout.addWidget(self.choix2)

        self.layout.addRow("for :", self.boxchoixtrie)
        #self.label2 = QtWidgets.QLabel("saisir extension", self.boxchoixtrie)#text indicatif des fonctions de chaque zone de saisie 

        self.layout.addRow("Folder :", self.boxcreateFolder)
        #self.label3 = QtWidgets.QLabel("saisir nom dossier à créer", self.boxcreateFolder)#text indicatif des fonctions de chaque zone de saisie 

        self.layout.addWidget(self.button)
        #self.changeValue()

    def setup_css(self):#stylisation de votre interface
        self.setStyleSheet("""
            width:300px;
            height:40px;
            font-style: uppercase;
            font-size:16px;                  
        """)
        
        self.button.setStyleSheet("color:blue ;")

        #self.label1.setStyleSheet("color: #767e89;")
        #self.label2.setStyleSheet("color: #767e89;")
        #self.label3.setStyleSheet("color: #767e89;")

    def open_folder_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options = QtWidgets.QFileDialog.ShowDirsOnly  # Only show directories
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", self.boxanalasyFolder.text(), options=options)

        if folder_path:
            self.boxanalasyFolder.setText(folder_path)


#fonction pour styliser le comportement notre text indicatif notamment faire disparaitre et réapparaitre les les textes indicatifs en cas de saisie ou d'effacement des zones de saisie  
    ##def text(self):
        #if self.boxanalasyFolder.text() == "":
            #self.label1.setStyleSheet("color: #767e89;")
        #else:
            #self.label1.setStyleSheet("color: rgba(0, 0, 0, 0);")

        #if self.boxchoixtrie.text() == "":
            #self.label2.setStyleSheet("color: #767e89;")
        #else:
            #self.label2.setStyleSheet("color: rgba(0, 0, 0, 0);")

        #if self.boxcreateFolder.text() == "":
            #self.label3.setStyleSheet("color: #767e89;")
        #else:
            #self.label3.setStyleSheet("color: rgba(0, 0, 0, 0);")

#fonction pour appéler notre fonction text() soit en textChanged en cas de chagement des valeurs de notre zone de saisie et editingfinisched dès la fin des modifications dans cette espace là
    #def changeValue(self):
        #self.boxanalasyFolder.textChanged.connect(self.text)
        #self.boxanalasyFolder.editingFinished.connect(self.text)

        #self.boxchoixtrie.textChanged.connect(self.text)
        #self.boxchoixtrie.editingFinished.connect(self.text)

        #self.boxcreateFolder.textChanged.connect(self.text)
        #self.boxcreateFolder.editingFinished.connect(self.text)

#fonction bouton pour démarrer notre trie
    def button_click(self):
        self.button.clicked.connect(self.create_folder)
        self.button.clicked.connect(self.analyse_folder)
        self.button.clicked.connect(self.extention)
        self.button.clicked.connect(self.changecheck)

#récupération de la valeur du lien de notre dossier 
    def analyse_folder(self):
        self.analysefolder = self.boxanalasyFolder.text()
        print(self.analysefolder)

#récupération de la valeur du box de trie     
    def extention(self):
        self.extent = self.boxchoixtrie.text()
        #print(self.extent)

    def folders(self):
        self.folder = self.boxchoixtrie.text()
        #print(self.folder)

    def files(self):
        self.fichier = self.boxchoixtrie.text()
        #print(self.file)

#récupérer le nom de notre dossier à créer
    def create_folder(self):
        self.createfolder = self.boxcreateFolder.text()
        print(self.createfolder)

#option de trie : par dossier, par extension ou par fichier 
    def changecheck(self):
        if self.choix0.isChecked():
            self.choix1.setEnabled(False)
            self.choix2.setEnabled(False)
            self.boxchoixtrie.setPlaceholderText("Saisir nom dossier")
            self.trie0()
        else:
            self.choix1.setEnabled(True)
            self.choix2.setEnabled(True)

        if self.choix1.isChecked():
            self.choix0.setEnabled(False)
            self.choix2.setEnabled(False)
            self.boxchoixtrie.setPlaceholderText("Saisir extension")
            self.trie1()
        else:
            self.choix0.setEnabled(True)
            
        if self.choix2.isChecked():
            self.choix0.setEnabled(False)
            self.choix1.setEnabled(False)
            self.boxchoixtrie.setPlaceholderText("Saisir nom fichier")
            self.trie2()
        
#fonction qui gère le trie dans notre programme avec création du dossier conténant les élément triés 
    def trie0(self):
        tri_doc = Path(self.analysefolder)
        doc = self.boxchoixtrie.text()
        output_doc = tri_doc / self.createfolder
        output_doc.mkdir(exist_ok=True)
        for item in tri_doc.iterdir():
            if item.is_dir() and item.name == doc:
                shutil.move(str(item), str(output_doc))

    def trie1(self):
        tri_doc = Path(self.analysefolder)
        exten = f".{self.extent}"
        output_doc = tri_doc / self.createfolder
        output_doc.mkdir(exist_ok=True)
        for item in tri_doc.iterdir():
            if item.is_file() and item.suffix == exten:
                item.rename(output_doc / item.name)

    def trie2(self):
        tri_doc = Path(self.analysefolder)
        file_name = self.boxchoixtrie.text().lower()
        output_doc = tri_doc / self.createfolder.title()
        output_doc.mkdir(exist_ok=True)
        for item in tri_doc.iterdir():
            if item.is_file():
                #item.rename(output_doc / item.name)
                file_name2 = item.stem.lower() #utiliser la méthode stem pour récupérer un nom sans son extension
                name_trie = ' '.join(file_name2.split('_')[:2]).lower()  # Joindre les deux premiers éléments avec un soulignement
                if file_name in name_trie:
                    shutil.move(str(item), str(output_doc))
                    #print(item)
            


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windows = App()
    windows.show()
    app.exec_()


