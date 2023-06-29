# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Projects\Python\demo-exam-test\app\ui\WarehouseMan.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 784)
        Dialog.setMinimumSize(QtCore.QSize(350, 600))
        Dialog.setStyleSheet("background: white;")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_field = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_field.sizePolicy().hasHeightForWidth())
        self.login_field.setSizePolicy(sizePolicy)
        self.login_field.setMinimumSize(QtCore.QSize(70, 0))
        self.login_field.setMaximumSize(QtCore.QSize(16777215, 30))
        self.login_field.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_field.setText("")
        self.login_field.setAlignment(QtCore.Qt.AlignCenter)
        self.login_field.setObjectName("login_field")
        self.horizontalLayout.addWidget(self.login_field)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_cloth = QtWidgets.QLineEdit(Dialog)
        self.search_cloth.setStyleSheet("QLineEdit {\n"
"border: 1px solid gray;\n"
"border-radius: 15px;\n"
"padding: 10px;\n"
"}")
        self.search_cloth.setObjectName("search_cloth")
        self.verticalLayout.addWidget(self.search_cloth)
        self.label_cloth = QtWidgets.QLabel(Dialog)
        self.label_cloth.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cloth.setObjectName("label_cloth")
        self.verticalLayout.addWidget(self.label_cloth)
        self.cloth_table = QtWidgets.QTableWidget(Dialog)
        self.cloth_table.setBaseSize(QtCore.QSize(0, 0))
        self.cloth_table.setObjectName("cloth_table")
        self.cloth_table.setColumnCount(0)
        self.cloth_table.setRowCount(0)
        self.cloth_table.horizontalHeader().setCascadingSectionResizes(True)
        self.cloth_table.horizontalHeader().setMinimumSectionSize(0)
        self.cloth_table.horizontalHeader().setStretchLastSection(False)
        self.cloth_table.verticalHeader().setCascadingSectionResizes(True)
        self.cloth_table.verticalHeader().setHighlightSections(False)
        self.cloth_table.verticalHeader().setMinimumSectionSize(23)
        self.cloth_table.verticalHeader().setSortIndicatorShown(False)
        self.cloth_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.cloth_table)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search_fittings = QtWidgets.QLineEdit(Dialog)
        self.search_fittings.setStyleSheet("QLineEdit {\n"
"border: 1px solid gray;\n"
"border-radius: 15px;\n"
"padding: 10px;\n"
"}")
        self.search_fittings.setObjectName("search_fittings")
        self.verticalLayout_2.addWidget(self.search_fittings)
        self.label_fittings = QtWidgets.QLabel(Dialog)
        self.label_fittings.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fittings.setObjectName("label_fittings")
        self.verticalLayout_2.addWidget(self.label_fittings)
        self.fittings_table = QtWidgets.QTableWidget(Dialog)
        self.fittings_table.setObjectName("fittings_table")
        self.fittings_table.setColumnCount(0)
        self.fittings_table.setRowCount(0)
        self.verticalLayout_2.addWidget(self.fittings_table)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search_cloth.setPlaceholderText(_translate("Dialog", "Введите название таблицы"))
        self.label_cloth.setText(_translate("Dialog", "TextLabel"))
        self.cloth_table.setSortingEnabled(True)
        self.search_fittings.setPlaceholderText(_translate("Dialog", "Введите название таблицы"))
        self.label_fittings.setText(_translate("Dialog", "TextLabel"))