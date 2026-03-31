from calendar import month
from datetime import datetime

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
        current_year = datetime.now().year

        self.ui.cmbYear.clear()

        for year in range(current_year - 26, current_year + 1):
            self.ui.cmbYear.addItem(str(year))

        self.ui.cmbYear.setCurrentText(str(current_year))

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
        Select_Month = int(self.ui.cmbMonth.currentText())
        Select_Year = int(self.ui.cmbYear.currentText())

        sql = "SELECT * FROM MyFile"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        self.ui.tableWidget.setRowCount(0)

        rw = 0
        current_year = datetime.now().year

        for row in result:
            mydate = str(row[2]).split("/")  # assuming DD/MM/YYYY

            day = int(mydate[0])
            month = int(mydate[1])
            year = int(mydate[2])

            if (year == Select_Year or year == current_year) and month == Select_Month:
                self.ui.tableWidget.insertRow(rw)

                self.ui.tableWidget.setItem(rw, 0, QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(rw, 1, QTableWidgetItem(str(row[1])))
                self.ui.tableWidget.setItem(rw, 2, QTableWidgetItem(str(row[2])))
                self.ui.tableWidget.setItem(rw, 3, QTableWidgetItem(str(row[3])))
                self.ui.tableWidget.setItem(rw, 4, QTableWidgetItem(str(row[4])))

                rw += 1