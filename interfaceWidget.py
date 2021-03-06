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
    # 하나로 사용하는 GAUGE 
    ################################################################################################
    def gaugeForm(self, Form, Theme, value, initX, initY, width, height, units, minValue, maxValue,\
        setScalaCount, scala_subdiv_count, floatValue):
        self.widget = AnalogGaugeWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            initX, initY, width, height))
        # self.initX+self.width*0, self.initX, self.width, self.height))
        self.retranslateUi(Form)

        ################################################################################################
        # GET GAUGE UNIT
        ################################################################################################
        self.widget.units = units

        ################################################################################################
        # SET MINIMUM AND MAXIMUM VALUE
        ################################################################################################
        self.widget.minValue = minValue
        self.widget.maxValue = maxValue

        ################################################################################################
        # SET GAUGE THEME
        ################################################################################################
        self.widget.setGaugeTheme(Theme)

        ################################################################################################
        # SET SCALE VALUE
        ################################################################################################
        self.widget.setScalaCount(setScalaCount)
        self.widget.scala_subdiv_count = scala_subdiv_count
        self.widget.floatValue = True   # float 출력됨.

        ################################################################################################
        # SET MINIMUM AND MAXIMUM VALUE
        ################################################################################################
        self.widget.minValue = minValue
        self.widget.maxValue = maxValue
        self.widget.floatValue = floatValue
        
        self.widget.updateValueManual(value)

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


