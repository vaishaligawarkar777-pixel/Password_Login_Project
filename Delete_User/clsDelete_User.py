from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem,QMessageBox
from Delete_User.Delete_User import Ui_MainWindow
import sqlite3
class clsDelete_User(QMainWindow):
    def __init__(self):
        super(clsDelete_User,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.id=0
        self.setFixedHeight(200)
        self.setFixedWidth(400)
        self.ui.cmbselectuser.setFocus()
        self.conn=sqlite3.connect('DataBase.db')
        self.cursor=self.conn.cursor()
        self.ui.btndelete.clicked.connect(self.deleteBtnClick)
        sql=f"Select * From User_table"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            self.ui.cmbselectuser.addItem(str(row[1]))

    def deleteBtnClick(self):
        sql = f"select * from User_table where UserName='{self.ui.cmbselectuser.currentText()}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.cursor.execute(f"delete from User_table where Id={self.id}")
        self.conn.commit()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Info")
        msg.setText("Delete user Successfully ")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        result = msg.exec_()
        self.ui.cmbselectuser.setCurrentText("")
