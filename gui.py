import sys, traceback
import time

from database_old import Database
from PyQt5 import QtCore, QtWidgets, uic


db = Database()
value = ''
AUTH = False

def check_auth():
    if not AUTH:
        widget.addWidget(Login())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Error(QtWidgets.QDialog):
    def __init__(self, error_message):
        super(Error, self).__init__()
        uic.loadUi("ui/ErrorDialog.ui", self)
        self.error_field.setText(error_message)

class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("ui/loginPage.ui", self)
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.to_register)

    def login(self):
        global AUTH
        login = self.login_field.text()
        password = self.password_field.text()
        try:
            user = db.authenticate_user(login, password)
            if user:
                AUTH = True
                if user[1][2] == 'manager':
                    widget.addWidget(WarehouseManPage(login))
                    widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                message = "Указаны неверные данные"
                dialog = Error(message)
                dialog.exec()

        except:
            print('SignIn error', traceback.format_exc())

    def to_register(self):
        widget.addWidget(Register())
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Main(QtWidgets.QDialog):
    def __init__(self, login):
        super(Main, self).__init__()
        uic.loadUi("ui/MainPage.ui", self)
        check_auth()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.login_field.setText("Ваш логин: " + login)
        self.search_btn.clicked.connect(self.search)

    def load_data(self, table_name):
        try:
            items = db.print_table(table_name)
            tablerow = 0
            tablecolumn = 0
            self.tableWidget.setColumnCount(len(items[0]))
            self.tableWidget.setRowCount(len(items[1]))
            for head in items[0]:
                self.tableWidget.setHorizontalHeaderItem(tablecolumn, QtWidgets.QTableWidgetItem(head))
                tablecolumn += 1
            for row in items[1]:
                for y in range(len(row)):
                    self.tableWidget.setItem(tablerow, y, QtWidgets.QTableWidgetItem(str(row[y])))
                tablerow += 1
        except:
            message = traceback.format_exc()
            dialog = Error(message)
            dialog.exec()
        
    def search(self):
        table_name = self.search_field.text()
        self.load_data(table_name)

class WarehouseManPage(QtWidgets.QDialog):
    def __init__(self, login):
        super(WarehouseManPage, self).__init__()
        uic.loadUi("ui/WarehouseMan.ui", self)
        check_auth()
        self.cloth_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.fittings_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.login_field.setText("Ваш логин: " + login)
        self.items_cloth = db.print_table('cloth')  
        self.items_fittings = db.print_table('fittings')  
        self.search_cloth.textChanged.connect(self.search)
        self.search_fittings.textChanged.connect(self.search)

    def create_table(self, data):
        try:
            tablerow = 0
            tablecolumn = 0
            self.cloth_table.setColumnCount(len(data[0]))
            self.cloth_table.setRowCount(len(data[1]))
            for head in data[0]:
                self.cloth_table.setHorizontalHeaderItem(tablecolumn, QtWidgets.QTableWidgetItem(head))
                tablecolumn += 1
            for row in data[1]:
                for y in range(len(row)):
                    self.cloth_table.setItem(tablerow, y, QtWidgets.QTableWidgetItem(str(row[y])))
                tablerow += 1
        except:
            message = traceback.format_exc()
            dialog = Error(message)
            dialog.exec()
        
    def search(self):
        start_time = time.time()
        new_array = (self.items_cloth[0],[])
        text_search = self.search_cloth.text()
        for item in self.items_cloth[1]:
            for word in enumerate(item):
                if text_search in str(word):
                    new_array[1].append(item)
                    continue

        self.create_table(new_array)
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time} seconds")

        # result = self.cloth_table.findItems(text_search, QtCore.Qt.MatchContains)
        # for item in result:
        #     print(item.text())

class Register(QtWidgets.QDialog):
    def __init__(self):
        super(Register, self).__init__()
        uic.loadUi("ui/RegisterPage.ui", self)    
        self.to_login_button.clicked.connect(self.to_login)
        self.register_button.clicked.connect(self.registration)
        self.buttonGroup.addButton(self.customer_radio)
        self.buttonGroup.addButton(self.manager_radio)
        self.buttonGroup.addButton(self.director_radio)
        self.buttonGroup.addButton(self.worker_radio)
        self.buttonGroup.buttonClicked.connect(self.on_button_clicked)
        self.choice = ''

    def on_button_clicked(self, button):
        self.choice = button.text()

    def to_login(self):
        widget.addWidget(Login())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def registration(self):
        login = self.login_field.text()
        password = self.password_field.text()
        name = self.name_field.text()
        role = self.choice
        if (login and password and role and name != ''): 
            try:
                db.user_register(login, password, role, name)
            except:
                message = traceback.format_exc()
                dialog = Error(message)
                dialog.exec()
            self.to_login()
        else:
            print('Одно из полей не заполнено!')
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(WarehouseManPage('fe'))
    widget.setWindowTitle('Database')
    widget.show()
    app.exec()