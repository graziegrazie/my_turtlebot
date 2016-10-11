# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/cliff_sensor_frame.ui'
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

class Ui_cliff_sensor_frame(object):
    def setupUi(self, cliff_sensor_frame):
        cliff_sensor_frame.setObjectName(_fromUtf8("cliff_sensor_frame"))
        cliff_sensor_frame.resize(791, 414)
        cliff_sensor_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        cliff_sensor_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(cliff_sensor_frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.text_browser = QtGui.QTextBrowser(cliff_sensor_frame)
        self.text_browser.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.text_browser.setTabChangesFocus(True)
        self.text_browser.setDocumentTitle(_fromUtf8(""))
        self.text_browser.setSource(QtCore.QUrl(_fromUtf8("qrc:/text/cliff_sensor.html")))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName(_fromUtf8("text_browser"))
        self.verticalLayout.addWidget(self.text_browser)
        self.groupBox = QtGui.QGroupBox(cliff_sensor_frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(96, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.speed_spinbox = QtGui.QDoubleSpinBox(self.groupBox)
        self.speed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speed_spinbox.setPrefix(_fromUtf8(""))
        self.speed_spinbox.setMaximum(0.7)
        self.speed_spinbox.setSingleStep(0.1)
        self.speed_spinbox.setProperty("value", 0.2)
        self.speed_spinbox.setObjectName(_fromUtf8("speed_spinbox"))
        self.gridLayout.addWidget(self.speed_spinbox, 0, 2, 1, 1)
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
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(cliff_sensor_frame)
        QtCore.QMetaObject.connectSlotsByName(cliff_sensor_frame)

    def retranslateUi(self, cliff_sensor_frame):
        cliff_sensor_frame.setWindowTitle(_translate("cliff_sensor_frame", "Frame", None))
        self.groupBox.setTitle(_translate("cliff_sensor_frame", "Controls", None))
        self.label_2.setText(_translate("cliff_sensor_frame", "Speed", None))
        self.speed_spinbox.setSuffix(_translate("cliff_sensor_frame", " m/s", None))
        self.start_button.setText(_translate("cliff_sensor_frame", "Start", None))
        self.stop_button.setText(_translate("cliff_sensor_frame", "Stop", None))

import common_rc
import text_rc
