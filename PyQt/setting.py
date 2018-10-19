# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 496)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 30, 521, 451))
        self.widget.setObjectName("widget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setGeometry(QtCore.QRect(160, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.praser_setting_label = QtWidgets.QLabel(self.widget)
        self.praser_setting_label.setGeometry(QtCore.QRect(10, 10, 191, 16))
        self.praser_setting_label.setObjectName("praser_setting_label")
        self.praser_list = QtWidgets.QListWidget(self.widget)
        self.praser_list.setGeometry(QtCore.QRect(0, 30, 421, 161))
        self.praser_list.setObjectName("praser_list")
        self.upload_label = QtWidgets.QLabel(self.widget)
        self.upload_label.setGeometry(QtCore.QRect(10, 230, 191, 16))
        self.upload_label.setObjectName("upload_label")
        self.upload_dir = QtWidgets.QLineEdit(self.widget)
        self.upload_dir.setGeometry(QtCore.QRect(0, 380, 421, 20))
        self.upload_dir.setObjectName("upload_dir")
        # self.upload_list = QtWidgets.QListWidget(self.widget)
        # self.upload_list.setGeometry(QtCore.QRect(0, 250, 421, 121))
        # self.upload_list.setObjectName("upload_list")

        self.video_list = QtWidgets.QTableWidget(self.tab)
        self.video_list.setGeometry(QtCore.QRect(0, 0, 451, 521))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_list.sizePolicy().hasHeightForWidth())
        self.video_list.setSizePolicy(sizePolicy)
        self.video_list.setMinimumSize(QtCore.QSize(0, 0))
        self.video_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.video_list.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.video_list.setObjectName("video_list")
        self.video_list.setColumnCount(4)
        self.video_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.video_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.video_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.video_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.video_list.setHorizontalHeaderItem(3, item)

        item = self.video_list.horizontalHeaderItem(0)
        item.setText(_translate("Form", "title"))
        item = self.video_list.horizontalHeaderItem(1)
        item.setText(_translate("Form", "url"))


        self.praser_url = QtWidgets.QLineEdit(self.widget)
        self.praser_url.setGeometry(QtCore.QRect(0, 200, 271, 20))
        self.praser_url.setObjectName("praser_url")
        self.praser_company = QtWidgets.QLineEdit(self.widget)
        self.praser_company.setGeometry(QtCore.QRect(300, 200, 121, 20))
        self.praser_company.setObjectName("praser_company")
        self.praser_add = QtWidgets.QPushButton(self.widget)
        self.praser_add.setGeometry(QtCore.QRect(420, 200, 51, 23))
        self.praser_add.setObjectName("praser_add")
        self.upload_add = QtWidgets.QPushButton(self.widget)
        self.upload_add.setGeometry(QtCore.QRect(420, 380, 51, 23))
        self.upload_add.setObjectName("upload_add")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.praser_setting_label.setText(_translate("Dialog", "praser setting"))
        self.upload_label.setText(_translate("Dialog", "upload script"))
        self.praser_add.setText(_translate("Dialog", "add"))
        self.upload_add.setText(_translate("Dialog", "add"))

# if __name__=='__main__':
#     import sys
#     app=QtWidgets.QApplication(sys.argv)
#     window=QtWidgets.QWidget()
#     ui=Ui_Dialog()
#     ui.setupUi(window)
#     # window.setFixedHeight(700)
#     # window.setFixedWidth(1000)
#     window.setWindowFlags(Qt.FramelessWindowHint)
#
#     window.show()
#
#     app.exec_()