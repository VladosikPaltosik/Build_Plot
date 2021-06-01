import pytest
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore
from BUILD_PLOTS.MAIN_PACKAGE.main_window import *
from BUILD_PLOTS.GUI_PACKEGE.param_window import *
from BUILD_PLOTS.GUI_PACKEGE.simple_window import *
from BUILD_PLOTS.GUI_PACKEGE.polar_window import *


def test_main_button_sim(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button1, QtCore.Qt.LeftButton)


def test_main_button_param(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button2, QtCore.Qt.LeftButton)


def test_main_button_polar(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button3, QtCore.Qt.LeftButton)


def test_simple_button_plot(qtbot):
    widget = SimpleWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button, QtCore.Qt.LeftButton)


def test_param_button_plot(qtbot):
    widget = ParamWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button, QtCore.Qt.LeftButton)


def test_polar_button_plot(qtbot):
    widget = PolarWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button, QtCore.Qt.LeftButton)


def test_simple_button_ref(qtbot):
    widget = SimpleWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button_ref, QtCore.Qt.LeftButton)


def test_param_button_ref(qtbot):
    widget = ParamWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button_ref, QtCore.Qt.LeftButton)


def test_polar_button_ref(qtbot):
    widget = PolarWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button_ref, QtCore.Qt.LeftButton)

