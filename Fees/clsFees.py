from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from Fees.Fees import Ui_MainWindow
import sqlite3
class clsFees(QMainWindow):
    def __init__(self):
        super(clsFees,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(500)
        self.setFixedWidth(1200)
        self.ui.cmbselectstudent.setFocus()
        self.conn = sqlite3.connect('DataBase.db')
        self.cursor = self.conn.cursor()

        self.ui.btnnew1.clicked.connect(self.NewBtnClick)
        self.ui.btnsave1.clicked.connect(self.SaveBtnClick)
        self.ui.btnupdate1.clicked.connect(self.UpdateBtnClick)
        self.ui.btndelete1.clicked.connect(self.DeleteBtnClick)

        sql="select * from MyData"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            self.ui.cmbselectstudent.addItem(str(row[1]))

        self.ui.tableWidget1.setColumnCount(5)
        self.ui.tableWidget1.setHorizontalHeaderLabels(["ID", "SelectStudentName", "Date", "Fees", "Subject"])
        self.ui.tableWidget1.setColumnWidth(0, 50)
        self.ui.tableWidget1.setColumnWidth(1, 150)
        self.ui.tableWidget1.setColumnWidth(2, 150)

        current_date = QDate.currentDate()
        self.ui.dateedit.setDate(current_date)
        self.ui.cmbselectstudent.currentTextChanged.connect(self.studentChange)
        self.ui.tableWidget1.clicked.connect(self.tableClick)
        self.loadDataInTable()
    def studentChange(self):
        currentStudent= self.ui.cmbselectstudent.currentText()
        sql = f"select * from MyData where Studentname='{currentStudent}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            # self.ui.cmbselectstudent.addItem(str(row[1]))
            self.ui.txtsubject.setText(str(row[3]))
            self.ui.txtfees.setText(str(row[4]))

    def loadDataInTable(self):
        self.cursor.execute(f"select * from MyFile")
        result = self.cursor.fetchall()
        self.ui.tableWidget1.setRowCount(0)
        rw = 0
        for row in result:
            rw = int(rw) + 1
            self.ui.tableWidget1.setRowCount(rw)
            self.ui.tableWidget1.setItem(rw - 1, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget1.setItem(rw - 1, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget1.setItem(rw - 1, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget1.setItem(rw - 1, 3, QTableWidgetItem(str(row[3])))
            self.ui.tableWidget1.setItem(rw - 1, 4, QTableWidgetItem(str(row[4])))

    def tableClick(self):
        cr = self.ui.tableWidget1.currentRow().__index__()
        print(cr)
        self.id = self.ui.tableWidget1.item(cr, 0).text()
        self.ui.cmbselectstudent.setCurrentText(self.ui.tableWidget1.item(cr,1).text())
        sdate = self.ui.tableWidget1.item(cr, 2).text()
        sdate = sdate.split("/")
        f_date = QDate(int(sdate[0]), int(sdate[1]), int(sdate[2]))
        self.ui.dateedit.setDate(f_date)
        self.ui.txtfees.setText(self.ui.tableWidget1.item(cr, 3).text())
        self.ui.txtsubject.setText(self.ui.tableWidget1.item(cr,4).text())

    def NewBtnClick(self):
        self.ui.cmbselectstudent.setCurrentText("")
        self.ui.dateedit.setDate("")
        self.ui.txtfees.setText("")
        self.ui.txtsubject.setText("")

    def SaveBtnClick(self):
        SelectStudent = self.ui.cmbselectstudent.currentText()
        Date = self.ui.dateedit.date().toString("yyyy/MM/dd")
        sql = f"insert into MyFile values(null,'{SelectStudent}','{Date}','{self.ui.txtfees.text()}','{self.ui.txtsubject.text()}')"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()
    def UpdateBtnClick(self):
        SelectStudent = self.ui.cmbselectstudent.currentText()
        Date = self.ui.dateedit.date().toString("yyyy/MM/dd")
        sql=f"Update MyFile set SelectStudent='{SelectStudent}',Date='{Date}',Fees='{self.ui.txtfees.text()}',Subject='{self.ui.txtsubject.text()}'"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()
    def DeleteBtnClick(self):
        self.cursor.execute(f"delete from MyFile where Id={self.id}")
        self.conn.commit()
        self.loadDataInTable()