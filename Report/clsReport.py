from PyQt5.QtWidgets import QMainWindow,QTableWidget,QTableWidgetItem
from Report.Report import Ui_MainWindow
import sqlite3
class clsReport(QMainWindow):
    def __init__(self):
        super(clsReport,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(600)
        self.setFixedWidth(650)
        self.conn=sqlite3.connect('DataBase.db')
        self.cursor=self.conn.cursor()

        sql = "Select*from MyData"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            self.ui.cmbstudent.addItem(str(row[1]))
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "SelectStudentName", "Date", "Fees", "Subject"])
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 150)

        self.ui.cmbstudent.currentIndexChanged.connect(self.loadDataInTable)
    def loadDataInTable(self):
        self.cursor.execute(f"select * from MyFile where SelectStudent='{self.ui.cmbstudent.currentText()}'")
        result = self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        rw = 0
        for row in result:
            rw = int(rw) + 1
            self.ui.tableWidget.setRowCount(rw)
            self.ui.tableWidget.setItem(rw - 1, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(rw - 1, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(rw - 1, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget.setItem(rw - 1, 3, QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(rw - 1, 4, QTableWidgetItem(str(row[4])))
