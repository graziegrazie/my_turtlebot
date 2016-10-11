# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/payload_frame.ui'
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

class Ui_payload_frame(object):
    def setupUi(self, payload_frame):
        payload_frame.setObjectName(_fromUtf8("payload_frame"))
        payload_frame.resize(791, 414)
        payload_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        payload_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(payload_frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.text_browser = QtGui.QTextBrowser(payload_frame)
        self.text_browser.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.text_browser.setTabChangesFocus(True)
        self.text_browser.setDocumentTitle(_fromUtf8(""))
        self.text_browser.setSource(QtCore.QUrl(_fromUtf8("qrc:/text/payload.html")))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName(_fromUtf8("text_browser"))
        self.verticalLayout.addWidget(self.text_browser)
        self.groupBox = QtGui.QGroupBox(payload_frame)
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
        self.speed_spinbox.setProperty("value", 0.3)
        self.speed_spinbox.setObjectName(_fromUtf8("speed_spinbox"))
        self.gridLayout.addWidget(self.speed_spinbox, 0, 2, 2, 1)
        self.distance_spinbox = QtGui.QDoubleSpinBox(self.groupBox)
        self.distance_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.distance_spinbox.setPrefix(_fromUtf8(""))
        self.distance_spinbox.setMaximum(2.0)
        self.distance_spinbox.setSingleStep(0.1)
        self.distance_spinbox.setProperty("value", 1.0)
        self.distance_spinbox.setObjectName(_fromUtf8("distance_spinbox"))
        self.gridLayout.addWidget(self.distance_spinbox, 0, 3, 1, 2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(96, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 1)
        self.stop_button = QtGui.QPushButton(self.groupBox)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.gridLayout.addWidget(self.stop_button, 1, 3, 2, 1)
        spacerItem2 = QtGui.QSpacerItem(181, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.start_button = QtGui.QPushButton(self.groupBox)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.gridLayout.addWidget(self.start_button, 2, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(167, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 4, 1, 3)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(payload_frame)
        QtCore.QMetaObject.connectSlotsByName(payload_frame)

    def retranslateUi(self, payload_frame):
        payload_frame.setWindowTitle(_translate("payload_frame", "Frame", None))
        self.groupBox.setTitle(_translate("payload_frame", "Controls", None))
        self.label_2.setText(_translate("payload_frame", "Speed", None))
        self.speed_spinbox.setSuffix(_translate("payload_frame", " m/s", None))
        self.distance_spinbox.setSuffix(_translate("payload_frame", "m", None))
        self.label_3.setText(_translate("payload_frame", "Side Length", None))
        self.stop_button.setText(_translate("payload_frame", "Stop", None))
        self.start_button.setText(_translate("payload_frame", "Start", None))

import common_rc
import text_rc
