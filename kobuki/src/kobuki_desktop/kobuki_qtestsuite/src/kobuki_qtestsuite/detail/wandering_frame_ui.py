# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/wandering_frame.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_wandering_frame(object):
    def setupUi(self, wandering_frame):
        wandering_frame.setObjectName(_fromUtf8("wandering_frame"))
        wandering_frame.resize(791, 414)
        wandering_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        wandering_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_2 = QtGui.QGridLayout(wandering_frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.text_browser = QtGui.QTextBrowser(wandering_frame)
        self.text_browser.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.text_browser.setTabChangesFocus(True)
        self.text_browser.setDocumentTitle(_fromUtf8(""))
        self.text_browser.setSource(QtCore.QUrl(_fromUtf8("qrc:/text/wandering.html")))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName(_fromUtf8("text_browser"))
        self.gridLayout_2.addWidget(self.text_browser, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(wandering_frame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 65, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.left_bump_counter_lcd = QtGui.QLCDNumber(self.groupBox_2)
        self.left_bump_counter_lcd.setObjectName(_fromUtf8("left_bump_counter_lcd"))
        self.verticalLayout.addWidget(self.left_bump_counter_lcd)
        self.centre_bump_counter_lcd = QtGui.QLCDNumber(self.groupBox_2)
        self.centre_bump_counter_lcd.setObjectName(_fromUtf8("centre_bump_counter_lcd"))
        self.verticalLayout.addWidget(self.centre_bump_counter_lcd)
        self.right_bump_counter_lcd = QtGui.QLCDNumber(self.groupBox_2)
        self.right_bump_counter_lcd.setObjectName(_fromUtf8("right_bump_counter_lcd"))
        self.verticalLayout.addWidget(self.right_bump_counter_lcd)
        spacerItem1 = QtGui.QSpacerItem(20, 119, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(wandering_frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem2 = QtGui.QSpacerItem(96, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.speed_spinbox = QtGui.QDoubleSpinBox(self.groupBox)
        self.speed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speed_spinbox.setPrefix(_fromUtf8(""))
        self.speed_spinbox.setMaximum(0.7)
        self.speed_spinbox.setSingleStep(0.1)
        self.speed_spinbox.setProperty("value", 0.3)
        self.speed_spinbox.setObjectName(_fromUtf8("speed_spinbox"))
        self.gridLayout.addWidget(self.speed_spinbox, 0, 2, 1, 1)
        self.angular_speed_spinbox = QtGui.QDoubleSpinBox(self.groupBox)
        self.angular_speed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.angular_speed_spinbox.setPrefix(_fromUtf8(""))
        self.angular_speed_spinbox.setMaximum(3.14)
        self.angular_speed_spinbox.setSingleStep(0.1)
        self.angular_speed_spinbox.setProperty("value", 0.8)
        self.angular_speed_spinbox.setObjectName(_fromUtf8("angular_speed_spinbox"))
        self.gridLayout.addWidget(self.angular_speed_spinbox, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(96, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 5, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(181, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 2)
        self.start_button = QtGui.QPushButton(self.groupBox)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.gridLayout.addWidget(self.start_button, 1, 2, 1, 1)
        self.stop_button = QtGui.QPushButton(self.groupBox)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.gridLayout.addWidget(self.stop_button, 1, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(167, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 4, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 2)

        self.retranslateUi(wandering_frame)
        QtCore.QMetaObject.connectSlotsByName(wandering_frame)

    def retranslateUi(self, wandering_frame):
        wandering_frame.setWindowTitle(_translate("wandering_frame", "Frame", None))
        self.groupBox_2.setTitle(_translate("wandering_frame", "Bump Counter", None))
        self.groupBox.setTitle(_translate("wandering_frame", "Controls", None))
        self.label_2.setText(_translate("wandering_frame", "Speed", None))
        self.speed_spinbox.setSuffix(_translate("wandering_frame", " m/s", None))
        self.angular_speed_spinbox.setSuffix(_translate("wandering_frame", " rad/s", None))
        self.label_3.setText(_translate("wandering_frame", "Angular Speed", None))
        self.start_button.setText(_translate("wandering_frame", "Start", None))
        self.stop_button.setText(_translate("wandering_frame", "Stop", None))

import common_rc
import text_rc
