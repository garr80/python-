# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from  main import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(802, 472)
        self.wild = QtWidgets.QPushButton(Form)
        self.wild.setGeometry(QtCore.QRect(50, 30, 191, 101))
        self.wild.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.wild.setObjectName("wild")
        self.standard = QtWidgets.QPushButton(Form)
        self.standard.setGeometry(QtCore.QRect(480, 30, 191, 101))
        self.standard.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.standard.setMouseTracking(False)
        self.standard.setObjectName("standard")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 140, 151, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(280, 140, 501, 311))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(50)

        self.retranslateUi(Form)
        self.wild.clicked.connect(Form.wild)
        self.standard.clicked.connect(Form.standard)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.report1 = report(b[list1[0]], b[list1[1]], self.tableWidget, self.tableWidget_2)
        self.report2 = report(b[list1[2]], b[list1[3]], self.tableWidget, self.tableWidget_2)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.wild.setText(_translate("Form", "狂野"))
        self.standard.setText(_translate("Form", "标准"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "战士"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "萨满"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "潜行者"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "圣骑"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "猎人"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "德鲁伊"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "术士"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "法师"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "牧师"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "出场率"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "胜率"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Form", "战士"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Form", "萨满"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Form", "潜行者"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Form", "圣骑"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("Form", "猎人"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("Form", "德鲁伊"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("Form", "术士"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("Form", "法师"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("Form", "牧师"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "战士"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "萨满"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "潜行者"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "圣骑"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "猎人"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "德鲁伊"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Form", "术士"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("Form", "法师"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("Form", "牧师"))
    def wild(self):
        self.report1.put()
    def standard(self):
        self.report2.put()

