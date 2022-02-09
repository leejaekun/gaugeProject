# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from analogGaugeWidget import AnalogGaugeWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout


class Ui_Form(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.initX = 20
        self.initY = 20

    ################################################################################################
    # FIRST GAUGE - SPEED METER
    ################################################################################################
    def gaugeForm1(self, Form, Theme):
        self.widget = AnalogGaugeWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            self.initX+self.width*0, self.initX, self.width, self.height))
        self.retranslateUi(Form)

        ################################################################################################
        # GET GAUGE UNIT
        ################################################################################################
        self.widget.units = "[r/min]"

        ################################################################################################
        # SET MINIMUM AND MAXIMUM VALUE
        ################################################################################################
        self.widget.minValue = 0
        self.widget.maxValue = 120

        ################################################################################################
        # SET GAUGE THEME
        ################################################################################################
        self.widget.setGaugeTheme(Theme)

    ################################################################################################
    # SECOND GAUGE - VOLT METER
    ################################################################################################
    def gaugeForm2(self, Form, Theme):
        self.widget = AnalogGaugeWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            self.initX+self.width*1, self.initX, self.width, self.height))
        self.retranslateUi(Form)

        ################################################################################################
        # GET GAUGE UNIT
        ################################################################################################
        self.widget.units = "[V]"

        ################################################################################################
        # SET MINIMUM AND MAXIMUM VALUE
        ################################################################################################
        self.widget.minValue = 0
        self.widget.maxValue = 400

        ################################################################################################
        # SET GAUGE THEME
        ################################################################################################
        self.widget.setGaugeTheme(Theme)

    ################################################################################################
    # THIRD GAUGE - CURRENT METER
    ################################################################################################
    def gaugeForm3(self, Form, Theme):
        self.widget = AnalogGaugeWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            self.initX+self.width*2, self.initX, self.width, self.height))
        self.retranslateUi(Form)

        ################################################################################################
        # GET GAUGE UNIT
        ################################################################################################
        self.widget.units = "[A]"

        ################################################################################################
        # SET SCALE VALUE
        ################################################################################################
        self.widget.setScalaCount(10)
        self.widget.scala_subdiv_count = 1

        ################################################################################################
        # SET MINIMUM AND MAXIMUM VALUE
        ################################################################################################
        self.widget.minValue = 0
        self.widget.maxValue = 5
        self.widget.floatValue = True

        ################################################################################################
        # SET GAUGE THEME
        ################################################################################################
        self.widget.setGaugeTheme(Theme)

    ################################################################################################
    # FORTH GAUGE - POWER METER
    ################################################################################################
    def gaugeForm4(self, Form, Theme):
        self.widget = AnalogGaugeWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            self.initX+self.width*3, self.initX, self.width, self.height))
        self.retranslateUi(Form)

        ################################################################################################
        # GET GAUGE UNIT
        ################################################################################################
        self.widget.units = "[W]"

        ################################################################################################
        # SET MINIMUM AND MAXIMUM VALUE
        ################################################################################################
        self.widget.minValue = 0
        self.widget.maxValue = 2000

        ################################################################################################
        # SET GAUGE THEME
        ################################################################################################
        self.widget.setGaugeTheme(Theme)

    ################################################################################################
    # 원래 사용된 코드 
    ################################################################################################
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        self.widget = AnalogGaugeWidget(Form)
        self.widget.setGeometry(QtCore.QRect(33, 170, 343, 265))
        self.widget.setObjectName("widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
    ################################################################################################


