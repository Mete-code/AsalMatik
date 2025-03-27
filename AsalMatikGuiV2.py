# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AsalMatikGuiV2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
import sys

from Yetenekler import MatematikKutuphanesi


class Ui_AsalMatikAnaForm(QDialog):
    def setupUi(self, AsalMatikAnaForm):
        AsalMatikAnaForm.setObjectName("AsalMatikAnaForm")
        AsalMatikAnaForm.resize(315, 406)
        self.setFixedSize(self.size())
        self.btnKapat = QtWidgets.QPushButton(AsalMatikAnaForm)
        self.btnKapat.setGeometry(QtCore.QRect(0, 360, 311, 41))
        self.btnKapat.setObjectName("btnKapat")
        self.btnKapat.clicked.connect(self.btnKapat_clicked)
        self.tabWidget = QtWidgets.QTabWidget(AsalMatikAnaForm)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 311, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 10, 81, 31))
        self.label.setObjectName("label")
        self.teAsalSayi = QtWidgets.QTextEdit(self.tab)
        self.teAsalSayi.setGeometry(QtCore.QRect(93, 10, 81, 31))
        self.teAsalSayi.setObjectName("teAsalSayi")
        self.btnAsalSayiHesapla = QtWidgets.QPushButton(self.tab)
        self.btnAsalSayiHesapla.setGeometry(QtCore.QRect(190, 9, 101, 33))
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(False)
        self.btnAsalSayiHesapla.setFont(font)
        self.btnAsalSayiHesapla.setObjectName("btnAsalSayiHesapla")
        self.btnAsalSayiHesapla.clicked.connect(self.btnAsalSayiHesapla_pressed)
        self.asalStart = QtWidgets.QSpinBox(self.tab)
        self.asalStart.setMaximum(1000000)
        self.asalStart.setGeometry(QtCore.QRect(90, 81, 91, 27))
        self.asalStart.setObjectName("asalStart")
        self.asalStop = QtWidgets.QSpinBox(self.tab)
        self.asalStop.setMaximum(1000000)
        self.asalStop.setGeometry(QtCore.QRect(90, 111, 91, 27))
        self.asalStop.setObjectName("asalStop")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 81, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 34, 21))
        self.label_3.setObjectName("label_3")
        self.btnAsalSayilariBul = QtWidgets.QPushButton(self.tab)
        self.btnAsalSayilariBul.setGeometry(QtCore.QRect(190, 80, 99, 58))
        self.btnAsalSayilariBul.clicked.connect(self.btnAsalSayilariBul_pressed)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btnAsalSayilariBul.setFont(font)
        self.btnAsalSayilariBul.setObjectName("btnAsalSayilariBul")
        self.lblAsalmiDegilmi = QtWidgets.QLabel(self.tab)
        self.lblAsalmiDegilmi.setGeometry(QtCore.QRect(100, 50, 191, 17))
        self.lblAsalmiDegilmi.setObjectName("lblAsalmiDegilmi")
        self.twAsalSayilar = QtWidgets.QTableWidget(self.tab)
        self.twAsalSayilar.setGeometry(QtCore.QRect(20, 150, 281, 151))
        self.twAsalSayilar.setObjectName("twAsalSayilar")
        self.twAsalSayilar.setColumnCount(1)
        self.twAsalSayilar.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.twAsalSayilar.setHorizontalHeaderItem(0, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 281, 261))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_3, "")



        self.retranslateUi(AsalMatikAnaForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AsalMatikAnaForm)

    def retranslateUi(self, AsalMatikAnaForm):
        _translate = QtCore.QCoreApplication.translate
        AsalMatikAnaForm.setWindowTitle(_translate("AsalMatikAnaForm", "Asal Matik"))
        self.btnKapat.setText(_translate("AsalMatikAnaForm", "Kapat"))
        self.label.setText(_translate("AsalMatikAnaForm", "Sayı Giriniz:"))
        self.btnAsalSayiHesapla.setText(_translate("AsalMatikAnaForm", "Hesapla"))
        self.label_2.setText(_translate("AsalMatikAnaForm", "Baslangıç:"))
        self.label_3.setText(_translate("AsalMatikAnaForm", "Bitiş:"))
        self.btnAsalSayilariBul.setText(_translate("AsalMatikAnaForm", "Hesapla"))
        self.lblAsalmiDegilmi.setText(_translate("AsalMatikAnaForm", "--"))
        item = self.twAsalSayilar.horizontalHeaderItem(0)
        item.setText(_translate("AsalMatikAnaForm", "Asal Sayılar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AsalMatikAnaForm", "AsalMatik"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AsalMatikAnaForm", "Çarpanları Bulma"))
        self.textEdit.setPlaceholderText(_translate("AsalMatikAnaForm", "AsalMatik V2.0, (c) by MeteEken"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("AsalMatikAnaForm", "Help"))


    def btnAsalSayiHesapla_pressed(self):
        mathLib = MatematikKutuphanesi()
        try:
            self.lblAsalmiDegilmi.setText(str(mathLib.AsalSayi(int(self.teAsalSayi.toPlainText()))))
        except:
            self.lblAsalmiDegilmi.setText("Sayı Girmelisiniz")
            #self.twAsalSayilar.setItem(-1, 1, QTableWidgetItem("2"))
    def btnAsalSayilariBul_pressed(self):
        mathLib = MatematikKutuphanesi()
        self.twAsalSayilar.setRowCount(0)
        counter = -1
        for i in range(self.asalStart.value(), self.asalStop.value()):
            asalmidegilmi = mathLib.AsalSayilar(i)
            if asalmidegilmi:
                self.twAsalSayilar.setRowCount(self.twAsalSayilar.rowCount() + 1)
                self.twAsalSayilar.setItem(counter, 1, QTableWidgetItem(str(i)))
                #self.twAsalSayilar.insertRow(counter, 1, QTableWidgetItem(str(i)))
                counter = counter + 1
    def btnKapat_clicked(self):
        sys.exit(0)
app = QApplication(sys.argv)
asalGui = Ui_AsalMatikAnaForm()
asalGui.setupUi(asalGui)
asalGui.show()
sys.exit(app.exec_())
