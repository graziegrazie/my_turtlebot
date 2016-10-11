# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/configuration_dock.ui'
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

class Ui_configuration_dock_widget(object):
    def setupUi(self, configuration_dock_widget):
        configuration_dock_widget.setObjectName(_fromUtf8("configuration_dock_widget"))
        configuration_dock_widget.resize(592, 385)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.topic_group_box = QtGui.QGroupBox(self.dockWidgetContents)
        self.topic_group_box.setObjectName(_fromUtf8("topic_group_box"))
        self.gridLayout = QtGui.QGridLayout(self.topic_group_box)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.topic_group_box)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cmd_vel_topic_combo_box = ExtendedComboBox(self.topic_group_box)
        self.cmd_vel_topic_combo_box.setEditable(False)
        self.cmd_vel_topic_combo_box.setObjectName(_fromUtf8("cmd_vel_topic_combo_box"))
        self.gridLayout.addWidget(self.cmd_vel_topic_combo_box, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.topic_group_box)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.odom_topic_combo_box = ExtendedComboBox(self.topic_group_box)
        self.odom_topic_combo_box.setEditable(False)
        self.odom_topic_combo_box.setObjectName(_fromUtf8("odom_topic_combo_box"))
        self.gridLayout.addWidget(self.odom_topic_combo_box, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.topic_group_box)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.core_topic_combo_box = ExtendedComboBox(self.topic_group_box)
        self.core_topic_combo_box.setEditable(False)
        self.core_topic_combo_box.setObjectName(_fromUtf8("core_topic_combo_box"))
        self.gridLayout.addWidget(self.core_topic_combo_box, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.topic_group_box)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.robot_state_topic_combo_box = ExtendedComboBox(self.topic_group_box)
        self.robot_state_topic_combo_box.setEditable(False)
        self.robot_state_topic_combo_box.setObjectName(_fromUtf8("robot_state_topic_combo_box"))
        self.gridLayout.addWidget(self.robot_state_topic_combo_box, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.topic_group_box)
        spacerItem = QtGui.QSpacerItem(20, 126, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        configuration_dock_widget.setWidget(self.dockWidgetContents)

        self.retranslateUi(configuration_dock_widget)
        QtCore.QMetaObject.connectSlotsByName(configuration_dock_widget)

    def retranslateUi(self, configuration_dock_widget):
        configuration_dock_widget.setWindowTitle(_translate("configuration_dock_widget", "Configuration Dock", None))
        self.topic_group_box.setTitle(_translate("configuration_dock_widget", "Topics", None))
        self.label.setText(_translate("configuration_dock_widget", "Cmd Vel", None))
        self.label_4.setText(_translate("configuration_dock_widget", "Odom", None))
        self.label_5.setText(_translate("configuration_dock_widget", "Core Sensors", None))
        self.label_6.setText(_translate("configuration_dock_widget", "Robot State", None))

from rqt_py_common.extended_combo_box import ExtendedComboBox
