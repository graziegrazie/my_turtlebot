# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/gyro_drift_frame.ui'
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

class Ui_gyro_drift_frame(object):
    def setupUi(self, gyro_drift_frame):
        gyro_drift_frame.setObjectName(_fromUtf8("gyro_drift_frame"))
        gyro_drift_frame.resize(791, 414)
        gyro_drift_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        gyro_drift_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_2 = QtGui.QGridLayout(gyro_drift_frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.text_browser = QtGui.QTextBrowser(gyro_drift_frame)
        self.text_browser.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.text_browser.setTabChangesFocus(True)
        self.text_browser.setDocumentTitle(_fromUtf8(""))
        self.text_browser.setSource(QtCore.QUrl(_fromUtf8("qrc:/text/gyro_drift.html")))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName(_fromUtf8("text_browser"))
        self.gridLayout_2.addWidget(self.text_browser, 0, 0, 1, 1)
        self.scan_angle_group_box = QtGui.QGroupBox(gyro_drift_frame)
        self.scan_angle_group_box.setObjectName(_fromUtf8("scan_angle_group_box"))
        self.gridLayout_2.addWidget(self.scan_angle_group_box, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(gyro_drift_frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(96, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.angular_speed_spinbox = QtGui.QDoubleSpinBox(self.groupBox)
        self.angular_speed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.angular_speed_spinbox.setPrefix(_fromUtf8(""))
        self.angular_speed_spinbox.setMaximum(3.14)
        self.angular_speed_spinbox.setSingleStep(0.1)
        self.angular_speed_spinbox.setProperty("value", 0.4)
        self.angular_speed_spinbox.setObjectName(_fromUtf8("angular_speed_spinbox"))
        self.gridLayout.addWidget(self.angular_speed_spinbox, 0, 2, 1, 1)
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

        self.retranslateUi(gyro_drift_frame)
        QtCore.QMetaObject.connectSlotsByName(gyro_drift_frame)

    def retranslateUi(self, gyro_drift_frame):
        gyro_drift_frame.setWindowTitle(_translate("gyro_drift_frame", "Frame", None))
        self.scan_angle_group_box.setTitle(_translate("gyro_drift_frame", "Gyro vs Laser", None))
        self.groupBox.setTitle(_translate("gyro_drift_frame", "Controls", None))
        self.label_2.setText(_translate("gyro_drift_frame", "Angular Speed", None))
        self.angular_speed_spinbox.setSuffix(_translate("gyro_drift_frame", " rad/s", None))
        self.start_button.setText(_translate("gyro_drift_frame", "Start", None))
        self.stop_button.setText(_translate("gyro_drift_frame", "Stop", None))

import common_rc
import text_rc
