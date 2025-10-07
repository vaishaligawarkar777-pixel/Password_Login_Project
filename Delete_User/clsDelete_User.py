from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
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
        sql=f"Select * From Add_User"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()

    def deleteBtnClick(self):
        self.cursor.execute(f"delete from Delete_User where Id={self.id}")
        self.conn.commit()
        self.loadDataInTable()