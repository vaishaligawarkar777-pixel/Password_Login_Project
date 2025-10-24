from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from Student.Student import Ui_MainWindow
import sqlite3
class clsStudent(QMainWindow):
    def __init__(self):
        super(clsStudent,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.id=0
        self.setFixedHeight(500)
        self.setFixedWidth(1220)
        self.ui.txtstudentname.setFocus()
        self.conn=sqlite3.connect('DataBase.db')
        self.cursor=self.conn.cursor()
        self.ui.btnnew.clicked.connect(self.NewBtnClick)
        self.ui.btnsave.clicked.connect(self.SaveBtnClick)
        self.ui.btnupdate.clicked.connect(self.UpdateBtnClick)
        self.ui.btndelete.clicked.connect(self.DeleteBtnClick)
        self.ui.radMale.setChecked(True)
        Subject = {
            "CP",
            "CPP",
            "Java",
            "Python",
            "SQL"
        }
        self.ui.cmbsubject.addItems(Subject)
        Batch={
            "BCA",
            "BSC-Sci",
            "MCA",
            "MSC-Sci"
        }
        self.ui.cmbbatch.addItems(Batch)
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID","StudentName","Gender","Subject","MonthlyFees","StartingDate","Batch"])
        self.ui.tableWidget.setColumnWidth(0,50)
        self.ui.tableWidget.setColumnWidth(1,150)
        self.ui.tableWidget.setColumnWidth(2,150)

        current_date = QDate.currentDate()
        self.ui.dateEdit.setDate(current_date)

        self.ui.tableWidget.clicked.connect(self.tableClick)
        self.loadDataInTable()
    def loadDataInTable(self):
        self.cursor.execute(f"select * from MyData")
        result=self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        rw=0
        for row in result:
            rw=int(rw)+1
            self.ui.tableWidget.setRowCount(rw)
            self.ui.tableWidget.setItem(rw-1,0,QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(rw-1,1,QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(rw-1,2,QTableWidgetItem(str(row[2])))
            self.ui.tableWidget.setItem(rw - 1, 3, QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(rw - 1, 4, QTableWidgetItem(str(row[4])))
            self.ui.tableWidget.setItem(rw - 1, 5, QTableWidgetItem(str(row[5])))
            self.ui.tableWidget.setItem(rw - 1, 6, QTableWidgetItem(str(row[6])))
    def tableClick(self):
        cr=self.ui.tableWidget.currentRow().__index__()
        print(cr)
        self.id = self.ui.tableWidget.item(cr,0).text()
        self.ui.txtstudentname.setText(self.ui.tableWidget.item(cr,1).text())

        gender=self.ui.tableWidget.item(cr,2).text()
        if gender=="Male":
            self.ui.radMale.setChecked(True)
        if gender=="Female":
            self.ui.radFemale.setChecked(True)
        self.ui.cmbsubject.setCurrentText( self.ui.tableWidget.item(cr, 3).text())
        self.ui.txtmonthlyfee.setText(self.ui.tableWidget.item(cr, 4).text())

        sdate= self.ui.tableWidget.item(cr, 5).text()
        sdate=sdate.split("/")
        fdate=QDate(int(sdate[0]),int(sdate[1]),int(sdate[2]))
        self.ui.dateEdit.setDate(fdate)
        self.ui.cmbbatch.setCurrentText(self.ui.tableWidget.item(cr, 6).text())
    def NewBtnClick(self):
        self.ui.txtstudentname.setText("")
        self.ui.cmbsubject.setText("")
        self.ui.cmbbatch.setText("")
        self.ui.txtmonthlyfee.setText("")
    def SaveBtnClick(self):
        gender = ""
        if self.ui.radMale.isChecked():
            gender = "Male"
        if self.ui.radFemale.isChecked():
            gender = "Female"
        Subject=self.ui.cmbsubject.currentText()
        Batch = self.ui.cmbbatch.currentText()
        Starting_Date = self.ui.dateEdit.date().toString("yyyy/MM/dd")
        sql=f"insert into MyData values(null,'{self.ui.txtstudentname.text()}','{gender}','{Subject}','{self.ui.txtmonthlyfee.text()}','{Starting_Date}','{Batch}')"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()
    def UpdateBtnClick(self):
        gender=""
        if self.ui.radMale.isChecked():
            gender="Male"
        if self.ui.radFemale.isChecked():
            gender="Female"
        Subject=self.ui.cmbsubject.currentText()
        Batch=self.ui.cmbbatch.currentText()
        Starting_Date=self.ui.dateEdit.date().toString("yyyy/MM/dd")
        sql=f"Update MyData set Studentname='{self.ui.txtstudentname.text()}',Gender='{gender}',Subject='{Subject}',Monthlyfee='{self.ui.txtmonthlyfee.text()}',Startingdate='{Starting_Date}',Batch='{Batch}' where id={self.id}"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()
    def DeleteBtnClick(self):
        self.cursor.execute(f"delete from MyData where id={self.id}")
        self.conn.commit()
        self.loadDataInTable()