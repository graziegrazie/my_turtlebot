# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/kobuki_qtestsuite/ui/testsuite.ui'
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

class Ui_testsuite_widget(object):
    def setupUi(self, testsuite_widget):
        testsuite_widget.setObjectName(_fromUtf8("testsuite_widget"))
        testsuite_widget.resize(1021, 562)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/kobuki_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        testsuite_widget.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(testsuite_widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.testsuite_tab_widget = QtGui.QTabWidget(testsuite_widget)
        self.testsuite_tab_widget.setEnabled(True)
        self.testsuite_tab_widget.setObjectName(_fromUtf8("testsuite_tab_widget"))
        self.battery_profile_tab = QtGui.QWidget()
        self.battery_profile_tab.setObjectName(_fromUtf8("battery_profile_tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.battery_profile_tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.battery_profile_frame = BatteryProfileFrame(self.battery_profile_tab)
        self.battery_profile_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.battery_profile_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.battery_profile_frame.setObjectName(_fromUtf8("battery_profile_frame"))
        self.verticalLayout_3.addWidget(self.battery_profile_frame)
        self.testsuite_tab_widget.addTab(self.battery_profile_tab, _fromUtf8(""))
        self.gyro_tab = QtGui.QWidget()
        self.gyro_tab.setObjectName(_fromUtf8("gyro_tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.gyro_tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gyro_drift_frame = GyroDriftFrame(self.gyro_tab)
        self.gyro_drift_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.gyro_drift_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gyro_drift_frame.setObjectName(_fromUtf8("gyro_drift_frame"))
        self.verticalLayout_4.addWidget(self.gyro_drift_frame)
        self.testsuite_tab_widget.addTab(self.gyro_tab, _fromUtf8(""))
        self.payload_tab = QtGui.QWidget()
        self.payload_tab.setObjectName(_fromUtf8("payload_tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.payload_tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.payload_frame = PayloadFrame(self.payload_tab)
        self.payload_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.payload_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.payload_frame.setObjectName(_fromUtf8("payload_frame"))
        self.verticalLayout_5.addWidget(self.payload_frame)
        self.testsuite_tab_widget.addTab(self.payload_tab, _fromUtf8(""))
        self.cliff_sensor_tab = QtGui.QWidget()
        self.cliff_sensor_tab.setObjectName(_fromUtf8("cliff_sensor_tab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.cliff_sensor_tab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.cliff_sensor_frame = CliffSensorFrame(self.cliff_sensor_tab)
        self.cliff_sensor_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.cliff_sensor_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.cliff_sensor_frame.setObjectName(_fromUtf8("cliff_sensor_frame"))
        self.verticalLayout_6.addWidget(self.cliff_sensor_frame)
        self.testsuite_tab_widget.addTab(self.cliff_sensor_tab, _fromUtf8(""))
        self.life_tab = QtGui.QWidget()
        self.life_tab.setObjectName(_fromUtf8("life_tab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.life_tab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.life_frame = LifeFrame(self.life_tab)
        self.life_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.life_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.life_frame.setObjectName(_fromUtf8("life_frame"))
        self.verticalLayout_7.addWidget(self.life_frame)
        self.testsuite_tab_widget.addTab(self.life_tab, _fromUtf8(""))
        self.wandering_tab = QtGui.QWidget()
        self.wandering_tab.setObjectName(_fromUtf8("wandering_tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wandering_tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.wandering_frame = WanderingFrame(self.wandering_tab)
        self.wandering_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.wandering_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.wandering_frame.setObjectName(_fromUtf8("wandering_frame"))
        self.verticalLayout_2.addWidget(self.wandering_frame)
        self.testsuite_tab_widget.addTab(self.wandering_tab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.testsuite_tab_widget)
        self.configuration_dock = ConfigurationDockWidget(testsuite_widget)
        self.configuration_dock.setObjectName(_fromUtf8("configuration_dock"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.configuration_dock.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.configuration_dock)

        self.retranslateUi(testsuite_widget)
        self.testsuite_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(testsuite_widget)

    def retranslateUi(self, testsuite_widget):
        testsuite_widget.setWindowTitle(_translate("testsuite_widget", "Kobuki Test Suite", None))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.battery_profile_tab), _translate("testsuite_widget", "Battery Profile", None))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.gyro_tab), _translate("testsuite_widget", "Gyro Drift", None))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.payload_tab), _translate("testsuite_widget", "Payload", None))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.cliff_sensor_tab), _translate("testsuite_widget", "Cliff", None))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.life_tab), _translate("testsuite_widget", "Life", None))
        self.testsuite_tab_widget.setTabText(self.testsuite_tab_widget.indexOf(self.wandering_tab), _translate("testsuite_widget", "Wander", None))

from kobuki_qtestsuite.battery_profile_frame import BatteryProfileFrame
from kobuki_qtestsuite.cliff_sensor_frame import CliffSensorFrame
from kobuki_qtestsuite.configuration_dock_widget import ConfigurationDockWidget
from kobuki_qtestsuite.gyro_drift_frame import GyroDriftFrame
from kobuki_qtestsuite.life_frame import LifeFrame
from kobuki_qtestsuite.payload_frame import PayloadFrame
from kobuki_qtestsuite.wandering_frame import WanderingFrame
import common_rc
import text_rc
