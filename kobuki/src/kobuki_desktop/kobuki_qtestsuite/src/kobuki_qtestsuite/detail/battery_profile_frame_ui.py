# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/battery_profile_frame.ui'
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

class Ui_battery_profile_frame(object):
    def setupUi(self, battery_profile_frame):
        battery_profile_frame.setObjectName(_fromUtf8("battery_profile_frame"))
        battery_profile_frame.resize(791, 414)
        battery_profile_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        battery_profile_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_2 = QtGui.QGridLayout(battery_profile_frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.text_browser = QtGui.QTextBrowser(battery_profile_frame)
        self.text_browser.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.text_browser.setTabChangesFocus(True)
        self.text_browser.setDocumentTitle(_fromUtf8(""))
        self.text_browser.setSource(QtCore.QUrl(_fromUtf8("qrc:/text/battery_profile.html")))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName(_fromUtf8("text_browser"))
        self.gridLayout_2.addWidget(self.text_browser, 0, 0, 1, 1)
        self.battery_profile_group_box = QtGui.QGroupBox(battery_profile_frame)
        self.battery_profile_group_box.setObjectName(_fromUtf8("battery_profile_group_box"))
        self.gridLayout_2.addWidget(self.battery_profile_group_box, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(battery_profile_frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(96, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.angular_speed_spinbox = QtGui.QDoubleSpinBox(self.groupBox)
        self.angular_speed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.angular_speed_spinbox.setPrefix(_fromUtf8(""))
        self.angular_speed_spinbox.setMaximum(3.14)
        self.angular_speed_spinbox.setSingleStep(0.1)
        self.angular_speed_spinbox.setProperty("value", 1.2)
        self.angular_speed_spinbox.setObjectName(_fromUtf8("angular_speed_spinbox"))
        self.gridLayout.addWidget(self.angular_speed_spinbox, 0, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(96, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(181, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.start_button = QtGui.QPushButton(self.groupBox)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.gridLayout.addWidget(self.start_button, 1, 1, 1, 1)
        self.stop_button = QtGui.QPushButton(self.groupBox)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.gridLayout.addWidget(self.stop_button, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(167, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 2)

        self.retranslateUi(battery_profile_frame)
        QtCore.QMetaObject.connectSlotsByName(battery_profile_frame)

    def retranslateUi(self, battery_profile_frame):
        battery_profile_frame.setWindowTitle(_translate("battery_profile_frame", "Frame", None))
        self.battery_profile_group_box.setTitle(_translate("battery_profile_frame", "Battery Profile", None))
        self.groupBox.setTitle(_translate("battery_profile_frame", "Controls", None))
        self.angular_speed_spinbox.setSuffix(_translate("battery_profile_frame", " rad/s", None))
        self.start_button.setText(_translate("battery_profile_frame", "Start", None))
        self.stop_button.setText(_translate("battery_profile_frame", "Stop", None))

import text_rc
