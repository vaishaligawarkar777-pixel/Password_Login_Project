from PyQt5.QtWidgets import QMainWindow
from MainWindow.MainWindow import Ui_MainWindow
from Add_User.clsAdd_User import clsAdd_User
from Delete_User.clsDelete_User import clsDelete_User
from Change_Password.clsChange_Password import clsChange_Password
from Student.clsStudent import clsStudentForm


class clsMainWindow(QMainWindow):
    def __init__(self):
        super(clsMainWindow,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionAdd_User.triggered.connect(self.Add_UserClick)
        self.ui.actionChange_Password.triggered.connect(self.Change_PasswordClick)
        self.ui.actionDelete_User.triggered.connect(self.Delete_UserClick)
        self.ui.actionStudent_File.triggered.connect(self.Student_UserClick)
        self.ui.actionFees_Form.triggered.connect(self.Fees_UserClick)
        self.ui.actionDelete_User.triggered.connect(self.Delete_UserClick)

    def Add_UserClick(self):
        self.a1 = clsAdd_User()
        self.ui.mdiArea.addSubWindow(self.a1)
        self.a1.show()


    def Delete_UserClick(self):
        self.d1 = clsDelete_User()
        self.ui.mdiArea.addSubWindow(self.d1)
        self.d1.show()

    def Change_PasswordClick(self):
        self.c1 = clsChange_Password()
        self.ui.mdiArea.addSubWindow(self.c1)
        self.c1.show()

    def Student_UserClick(self):
        self.s1 = clsStudentForm()
        self.ui.mdiArea.addSubWindow(self.s1)
        self.s1.show()

    def Fees_UserClick(self):
        self.f1 =clsFees()
        self.ui.mdiArea.addSubWindow(self.f1)
        self.f1.show()







