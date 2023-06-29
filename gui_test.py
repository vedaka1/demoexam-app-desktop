from database import Database
import base64
import sys, traceback
from PyQt5 import QtWidgets, uic, QtGui, QtCore


class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, error_message):
        super(ErrorDialog, self).__init__()
        uic.loadUi("ui/ErrorDialog.ui", self)
        self.error_field.setText(error_message)

class RegisterPage(QtWidgets.QDialog):
    def __init__(self):
        self.check_authentification()
        super(RegisterPage, self).__init__()
        uic.loadUi("ui/RegisterPage.ui", self)
        self.to_login_button.clicked.connect(self.to_login)
        self.register_button.clicked.connect(self.registration)
        self.buttonGroup.buttonClicked.connect(self.on_button_clicked)
        self.choice = ''

    def on_button_clicked(self, button):
        self.choice = button.text()

    def to_login(self):
        widget.addWidget(LoginPage())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def registration(self):
        login = self.login_field.text()
        password = self.password_field.text()
        role = self.choice
        name = self.name_field.text()
        try:
            db.registration(login, password, role, name)
        except:
            print(traceback.format_exc())

class LoginPage(QtWidgets.QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        uic.loadUi("ui/loginPage.ui", self)
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.to_register)

    def login(self):
        login = self.login_field.text()
        password = self.password_field.text()
        try:
            db.authentificate_user(login, password)
            if db.AUTH:
                if db.user_data[2] == 'Заказчик':
                    widget.addWidget(MainPage(login))
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                if db.user_data[2] == 'customer':
                    widget.addWidget(MainPage(login))
                    widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                message = "Указаны неверные данные"
                dialog = ErrorDialog(message)
                dialog.exec()

        except:
            print('SignIn error', traceback.format_exc())

    def to_register(self):
        if db.AUTH:
            widget.addWidget(MainPage())
            widget.setCurrentIndex(widget.currentIndex() + 1)

class MainPage(QtWidgets.QDialog):
    def __init__(self, login):
        super(MainPage, self).__init__()
        uic.loadUi("ui/MainPage.ui", self)
        self.login_field.setText("Ваш логин: " + login)
        self.set_table('cloth', self.cloth_table)
        self.set_table('fittings', self.fittings_table)
        self.set_table('orders', self.orders_table)
        self.order_btn.clicked.connect(self.order_product)
        self.cloth_table.itemClicked.connect(self.get_cloth)
        self.fittings_table.itemClicked.connect(self.get_fitting)
    
    def get_cloth(self, item):
        self.selected_cloth.setText(item.text())

    def get_fitting(self, item):
        self.selected_fitting.setText(item.text())

    def set_table(self, table_name, table):
        try:
            rows = 0
            columns = 0
            table_items = db.print_table(table_name)
            table.setColumnCount(len(table_items[0]))
            table.setRowCount(len(table_items[1]))
            for header in table_items[0]:
                table.setHorizontalHeaderItem(columns, QtWidgets.QTableWidgetItem(header))
                columns += 1
            for row in table_items[1]:
                for y in range(len(row)):
                    table.setItem(rows, y, QtWidgets.QTableWidgetItem(str(row[y])))
                rows += 1
        except:
            message = traceback.format_exc()
            dialog = ErrorDialog(message)
            dialog.exec()
        
    def order_product(self):
        cloth = self.selected_cloth.text()
        fitting = self.selected_fitting.text()
        product_name = self.product_name_field.text()
        note = self.product_note_field.text()
        width = self.product_width_field.text()
        height = self.product_height_field.text()
        try: 
            db.order_product(product_name, width, height, note, cloth, fitting)
            message = traceback.format_exc()
            dialog = ErrorDialog(message)
            dialog.exec()
            
        except:
            print(traceback.format_exc())    

if __name__ == '__main__':
    db = Database()
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(MainPage('ved'))
    widget.show()
    app.exec()