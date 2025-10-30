from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow,QTableWidget,QTableWidgetItem
from Yearly_Report.Yearly_Report import Ui_MainWindow
import sqlite3
class clsYearly_Report(QMainWindow):
    def __init__(self):
        super(clsYearly_Report,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(440)
        self.setFixedWidth(650)

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
        Select_Year = self.ui.cmbYear.currentText()
        sql=f"Select * From MyFile"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        rw = 0
        for row in result:
            my_data=str(row[2])
            my_data=my_data.split("/")
            if int(my_data[0])==int(Select_Year):
                rw = int(rw) + 1
                self.ui.tableWidget.setRowCount(rw)
                self.ui.tableWidget.setItem(rw - 1, 0, QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(rw - 1, 1, QTableWidgetItem(str(row[1])))
                self.ui.tableWidget.setItem(rw - 1, 2, QTableWidgetItem(str(row[2])))
                self.ui.tableWidget.setItem(rw - 1, 3, QTableWidgetItem(str(row[3])))
                self.ui.tableWidget.setItem(rw - 1, 4, QTableWidgetItem(str(row[4])))

