# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtLastName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLastName.setGeometry(QtCore.QRect(120, 70, 171, 20))
        self.txtLastName.setObjectName("txtLastName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.txtFirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFirstName.setGeometry(QtCore.QRect(120, 100, 171, 20))
        self.txtFirstName.setObjectName("txtFirstName")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.txtAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAddress.setGeometry(QtCore.QRect(120, 220, 161, 20))
        self.txtAddress.setObjectName("txtAddress")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 170, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.txtCity = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCity.setGeometry(QtCore.QRect(120, 250, 161, 20))
        self.txtCity.setObjectName("txtCity")
        self.txtState = QtWidgets.QLineEdit(self.centralwidget)
        self.txtState.setGeometry(QtCore.QRect(120, 280, 161, 20))
        self.txtState.setText("")
        self.txtState.setObjectName("txtState")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 280, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.txtZip = QtWidgets.QLineEdit(self.centralwidget)
        self.txtZip.setGeometry(QtCore.QRect(120, 310, 161, 20))
        self.txtZip.setObjectName("txtZip")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 310, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 0, 20, 501))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.txtPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPhone.setGeometry(QtCore.QRect(120, 430, 161, 20))
        self.txtPhone.setObjectName("txtPhone")
        self.txtEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEmail.setGeometry(QtCore.QRect(120, 460, 161, 20))
        self.txtEmail.setObjectName("txtEmail")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 460, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 380, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 430, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(330, 20, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.cbxPlan = QtWidgets.QComboBox(self.centralwidget)
        self.cbxPlan.setGeometry(QtCore.QRect(470, 70, 231, 22))
        self.cbxPlan.setObjectName("cbxPlan")
        self.cbxPlan.addItem("")
        self.cbxPlan.addItem("")
        self.cbxPlan.addItem("")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(330, 150, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.sbxCars = QtWidgets.QSpinBox(self.centralwidget)
        self.sbxCars.setGeometry(QtCore.QRect(470, 200, 42, 22))
        self.sbxCars.setMinimum(1)
        self.sbxCars.setMaximum(3)
        self.sbxCars.setObjectName("sbxCars")
        self.lblPluralCars = QtWidgets.QLabel(self.centralwidget)
        self.lblPluralCars.setGeometry(QtCore.QRect(520, 200, 21, 20))
        self.lblPluralCars.setObjectName("lblPluralCars")
        self.lblDiscount = QtWidgets.QLabel(self.centralwidget)
        self.lblDiscount.setGeometry(QtCore.QRect(570, 190, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblDiscount.setFont(font)
        self.lblDiscount.setText("")
        self.lblDiscount.setObjectName("lblDiscount")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(330, 280, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.btnCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalculate.setGeometry(QtCore.QRect(340, 420, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCalculate.setFont(font)
        self.btnCalculate.setObjectName("btnCalculate")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(500, 420, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.cbxPaymentModel = QtWidgets.QComboBox(self.centralwidget)
        self.cbxPaymentModel.setGeometry(QtCore.QRect(470, 330, 231, 22))
        self.cbxPaymentModel.setObjectName("cbxPaymentModel")
        self.cbxPaymentModel.addItem("")
        self.cbxPaymentModel.addItem("")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(610, 507, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 500, 601, 31))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(660, 420, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(450, 330, 20, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(450, 200, 20, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(450, 70, 20, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionCalculate = QtWidgets.QAction(MainWindow)
        self.actionCalculate.setObjectName("actionCalculate")
        self.actExit = QtWidgets.QAction(MainWindow)
        self.actExit.setObjectName("actExit")
        self.actCalculate = QtWidgets.QAction(MainWindow)
        self.actCalculate.setObjectName("actCalculate")
        self.actClear = QtWidgets.QAction(MainWindow)
        self.actClear.setObjectName("actClear")
        self.menuFile.addAction(self.actExit)
        self.menuView.addAction(self.actCalculate)
        self.menuView.addAction(self.actClear)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Best Car Wash"))
        self.label_2.setText(_translate("MainWindow", "*Last"))
        self.label_3.setText(_translate("MainWindow", "*First"))
        self.label_4.setText(_translate("MainWindow", "Name"))
        self.label_5.setText(_translate("MainWindow", "City"))
        self.label_6.setText(_translate("MainWindow", "Address"))
        self.label_7.setText(_translate("MainWindow", "Address"))
        self.label_8.setText(_translate("MainWindow", "State"))
        self.label_9.setText(_translate("MainWindow", "Zip code"))
        self.label_10.setText(_translate("MainWindow", "*Email"))
        self.label_11.setText(_translate("MainWindow", "Contact Information"))
        self.label_12.setText(_translate("MainWindow", "*Phone"))
        self.label_15.setText(_translate("MainWindow", "Plan"))
        self.cbxPlan.setItemText(0, _translate("MainWindow", "Gold Plan ($36/mo)"))
        self.cbxPlan.setItemText(1, _translate("MainWindow", "Silver Plan ($30/mo)"))
        self.cbxPlan.setItemText(2, _translate("MainWindow", "Bronze Plan ($20/mo)"))
        self.label_16.setText(_translate("MainWindow", "Coverage"))
        self.lblPluralCars.setText(_translate("MainWindow", "car"))
        self.label_18.setText(_translate("MainWindow", "Payment"))
        self.btnCalculate.setText(_translate("MainWindow", "Calculate"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.cbxPaymentModel.setItemText(0, _translate("MainWindow", "Monthly"))
        self.cbxPaymentModel.setItemText(1, _translate("MainWindow", "Annually (1 month free!)"))
        self.label_19.setText(_translate("MainWindow", "Contestant #109 | Best Car Wash"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.label_13.setText(_translate("MainWindow", "*"))
        self.label_14.setText(_translate("MainWindow", "*"))
        self.label_17.setText(_translate("MainWindow", "*"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionCalculate.setText(_translate("MainWindow", "Calculate"))
        self.actExit.setText(_translate("MainWindow", "Exit"))
        self.actCalculate.setText(_translate("MainWindow", "Calculate"))
        self.actClear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
