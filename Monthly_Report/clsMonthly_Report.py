from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow,QTableWidget,QTableWidgetItem
from Monthly_Report.Monthly_Report import Ui_MainWindow
import sqlite3
class clsMonthly_Report(QMainWindow):
    def __init__(self):
        super(clsMonthly_Report,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(450)
        self.setFixedWidth(660)

        self.conn = sqlite3.connect('DataBase.db')
        self.cursor = self.conn.cursor()

        self.ui.btnShow.clicked.connect(self.Show_Date)

        sql = "Select*from MyData"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "SelectStudentName", "Date", "Fees", "Subject"])
            self.ui.tableWidget.setColumnWidth(0, 50)
            self.ui.tableWidget.setColumnWidth(1, 150)
            self.ui.tableWidget.setColumnWidth(2, 150)
    def Show_Date(self):
        self.loadDataInTable()
    def loadDataInTable(self):
        Select_Month = self.ui.cmbMonth.currentText()
        Select_Year = self.ui.cmbYear.currentText()
        sql=f"Select * From MyFile"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        rw = 0
        for row in result:
            mydate=str(row[2])
            mydate=mydate.split("/")
            if int(mydate[0])==int(Select_Year) and int(mydate[1])==int(Select_Month):
                rw = int(rw) + 1
                self.ui.tableWidget.setRowCount(rw)
                self.ui.tableWidget.setItem(rw - 1, 0, QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(rw - 1, 1, QTableWidgetItem(str(row[1])))
                self.ui.tableWidget.setItem(rw - 1, 2, QTableWidgetItem(str(row[2])))
                self.ui.tableWidget.setItem(rw - 1, 3, QTableWidgetItem(str(row[3])))
                self.ui.tableWidget.setItem(rw - 1, 4, QTableWidgetItem(str(row[4])))
