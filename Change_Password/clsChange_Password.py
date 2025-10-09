from PyQt5.QtWidgets import QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox
from Change_Password.Change_Password import Ui_MainWindow
import sqlite3
class clsChange_Password(QMainWindow):
    def __init__(self):
        super(clsChange_Password,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(400)
        self.setFixedWidth(400)
        self.ui.cmbusername.setFocus()
        self.conn = sqlite3.connect('DataBase.db')
        self.cursor = self.conn.cursor()
        self.ui.btnchange.clicked.connect(self.changeBtnClick)
        sql = "select * from Add_User"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            self.ui.cmbusername.addItem(str(row[1]))

    def changeBtnClick(self):
        if self.ui.cmbusername.currentText() != "":
            if self.ui.txtpassword.text() != "":
                if self.ui.txtpassword.text() == self.ui.txtpassword1.text():
                    UserName = self.ui.cmbusername.currentText()
                    sql = f"Insert Into Change_Password Values(null,'{UserName}','{self.ui.txtoldpassword.text()}','{self.ui.txtpassword.text()}','{self.ui.txtpassword1.text()}')"
                    self.cursor.execute(sql)
                    self.conn.commit()
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Info")
                    msg.setText("User Added Successfully ")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.setDefaultButton(QMessageBox.Ok)
                    result = msg.exec_()
                    self.ui.cmbusername.setCurrentText("")
                    self.ui.txtoldpassword.setText("")
                    self.ui.txtpassword.setText("")
                    self.ui.txtpassword1.setText("")
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Info")
                    msg.setText("Both Password Must be Same")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.setDefaultButton(QMessageBox.Ok)
                    result = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Info")
                msg.setText("Password  can not be blank")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.setDefaultButton(QMessageBox.Ok)


        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Info")
            msg.setText("User name  can not be blank")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Ok)
            result = msg.exec_()











