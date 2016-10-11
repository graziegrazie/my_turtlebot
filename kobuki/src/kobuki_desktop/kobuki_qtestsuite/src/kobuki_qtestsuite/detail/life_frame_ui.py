# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/life_frame.ui'
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

class Ui_life_frame(object):
    def setupUi(self, life_frame):
        life_frame.setObjectName(_fromUtf8("life_frame"))
        life_frame.resize(791, 414)
        life_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        life_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_2 = QtGui.QGridLayout(life_frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.text_browser = QtGui.QTextBrowser(life_frame)
        self.text_browser.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.text_browser.setTabChangesFocus(True)
        self.text_browser.setDocumentTitle(_fromUtf8(""))
        self.text_browser.setSource(QtCore.QUrl(_fromUtf8("qrc:/text/life.html")))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName(_fromUtf8("text_browser"))
        self.gridLayout_2.addWidget(self.text_browser, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(life_frame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 89, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.run_progress = QtGui.QProgressBar(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_progress.sizePolicy().hasHeightForWidth())
        self.run_progress.setSizePolicy(sizePolicy)
        self.run_progress.setMaximum(60)
        self.run_progress.setProperty("value", 0)
        self.run_progress.setObjectName(_fromUtf8("run_progress"))
        self.verticalLayout.addWidget(self.run_progress)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.idle_progress = QtGui.QProgressBar(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idle_progress.sizePolicy().hasHeightForWidth())
        self.idle_progress.setSizePolicy(sizePolicy)
        self.idle_progress.setMaximum(15)
        self.idle_progress.setProperty("value", 0)
        self.idle_progress.setInvertedAppearance(False)
        self.idle_progress.setObjectName(_fromUtf8("idle_progress"))
        self.verticalLayout.addWidget(self.idle_progress)
        spacerItem1 = QtGui.QSpacerItem(20, 88, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(life_frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem2 = QtGui.QSpacerItem(96, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.angular_speed_spinbox = QtGui.QDoubleSpinBox(self.groupBox)
        self.angular_speed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.angular_speed_spinbox.setPrefix(_fromUtf8(""))
        self.angular_speed_spinbox.setMaximum(3.14)
        self.angular_speed_spinbox.setSingleStep(0.1)
        self.angular_speed_spinbox.setProperty("value", 0.8)
        self.angular_speed_spinbox.setObjectName(_fromUtf8("angular_speed_spinbox"))
        self.gridLayout.addWidget(self.angular_speed_spinbox, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(96, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(181, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.start_button = QtGui.QPushButton(self.groupBox)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.gridLayout.addWidget(self.start_button, 1, 1, 1, 1)
        self.stop_button = QtGui.QPushButton(self.groupBox)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.gridLayout.addWidget(self.stop_button, 1, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(167, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 2)

        self.retranslateUi(life_frame)
        QtCore.QMetaObject.connectSlotsByName(life_frame)

    def retranslateUi(self, life_frame):
        life_frame.setWindowTitle(_translate("life_frame", "Frame", None))
        self.groupBox_2.setTitle(_translate("life_frame", "Life Meters", None))
        self.label.setText(_translate("life_frame", "Run Status", None))
        self.label_4.setText(_translate("life_frame", "Idle Status", None))
        self.groupBox.setTitle(_translate("life_frame", "Controls", None))
        self.label_3.setText(_translate("life_frame", "Angular Speed", None))
        self.angular_speed_spinbox.setSuffix(_translate("life_frame", " rad/s", None))
        self.start_button.setText(_translate("life_frame", "Start", None))
        self.stop_button.setText(_translate("life_frame", "Stop", None))

import common_rc
import text_rc
