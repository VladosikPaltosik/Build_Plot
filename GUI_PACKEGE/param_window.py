
import numpy as np
import matplotlib.pyplot as plt
from BUILD_PLOTS.REFERENCE_PACKAGE.reference_window import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


# Parametric function window
class ParamWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_DesktopIcon')))
        self.setWindowTitle('Parametric Function')
        self.setFixedSize(480, 480)
        # A figure instance to plot on
        self.figure = plt.figure()

        # This is the Canvas Widget that
        # displays the 'figure' it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # This is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # No external window yet.
        self.w = None

        # Create label to enter plot x
        label_x = QLabel('Enter: x=', self)
        label_x.setFont(QFont('Times', 15))

        # Create label to enter plot y
        label_y = QLabel('Enter: y=', self)
        label_y.setFont(QFont('Times', 15))

        # Create label 'From' range
        label_from = QLabel('t ∈ [', self)
        label_from.setFont(QFont('Times', 15))

        # From_line label creating and style
        self.from_line = QLineEdit()
        self.from_line.setText('0')
        self.from_line.setFixedSize(50, 30)

        # To_line label creating and style
        self.to_line = QLineEdit()
        self.to_line.setText('2*np.pi')
        self.to_line.setFixedSize(50, 30)

        # Create label 'To' range
        label_to = QLabel(']', self)
        label_to.setFont(QFont('Times', 15))

        # Creating a line edit
        self.nameLineEdit_x = QLineEdit()
        self.nameLineEdit_x.setText('np.sin(t) + 2*np.sin(2*t)')
        self.nameLineEdit_x.setFixedSize(210, 30)

        self.nameLineEdit_y = QLineEdit()
        self.nameLineEdit_y.setText('np.cos(t) - 2*np.cos(2*t)')
        self.nameLineEdit_y.setFixedSize(210, 30)

        # Create button 'Create plot'
        self.button = QPushButton('CREATE PLOT')
        self.button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )
        self.button.setToolTip("Push to create plot")
        self.button.setFont(QFont('Times', 15))

        # Create button 'Reference'
        self.button_ref = QPushButton('REFERENCE')
        self.button_ref.setStyleSheet("QPushButton"
                                  "{"
                                  "background-color : lightblue;"
                                  "}"
                                  "QPushButton::pressed"
                                  "{"
                                  "background-color : red;"
                                  "}"
                                  )
        self.button_ref.setToolTip("Reference how to create plots using this app")
        self.button_ref.setFont(QFont('Times', 15))

        # Adding action to the button Create Plot
        self.button.clicked.connect(self.button_clicked)

        # Adding action to the button Reference
        self.reference = ReferenceWindow()
        self.button_ref.clicked.connect(lambda checked: self.show_new_window(self.reference))

        # Creating boxes layouts
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        layout3 = QHBoxLayout()

        # Adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # Adding canvas to the layout
        layout.addWidget(self.canvas)

        # Adding input forms 'range' and 'create plot'
        form_layout.addRow(label_x, self.nameLineEdit_x)
        form_layout.addRow(label_y, self.nameLineEdit_y)
        layout.addLayout(form_layout)

        layout3.addWidget(label_from)
        layout3.addWidget(self.from_line)
        layout3.addWidget(self.to_line)
        layout3.addWidget(label_to)
        layout.addLayout(layout3)

        # Adding buttons
        layout3.addWidget(self.button)
        layout3.addWidget(self.button_ref)
        layout.addLayout(layout3)

        # Setting layout to the main window
        self.setLayout(layout)

    # Action called by the push button
    def button_clicked(self):
        if not self.from_line.text() and not self.to_line.text() and \
                not self.nameLineEdit_x.text() and not self.nameLineEdit_y.text():
            error_param = QMessageBox()
            error_param.setWindowTitle('Error')
            error_param.setText('All fields are empty!!!')
            error_param.setIcon(QMessageBox.Warning)
            error_param.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            error_param.setDefaultButton(QMessageBox.Ok)
            error_param.exec_()
        else:
            if 'np.' in self.from_line.text() or 'np.' in self.to_line.text():
                x_1 = str(eval(self.from_line.text()))
                x_2 = str(eval(self.to_line.text()))
                self.from_line.setText(x_1)
                self.to_line.setText(x_2)
            try:
                float(self.from_line.text())
                float(self.to_line.text())
            except ValueError:
                error_param = QMessageBox()
                error_param.setWindowTitle('Error')
                error_param.setText('Incorrect input in range fields!!!')
                error_param.setIcon(QMessageBox.Warning)
                error_param.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                error_param.setDefaultButton(QMessageBox.Ok)
                error_param.exec_()
            else:
                if self.from_line.text() == '' or self.to_line.text() == '' or \
                        eval(self.from_line.text()) >= eval(self.to_line.text()):
                    # Creating 'Error window'
                    error_param = QMessageBox()
                    error_param.setWindowTitle('Error')
                    error_param.setText('Incorrect input in range fields!!!')
                    error_param.setIcon(QMessageBox.Warning)
                    error_param.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                    error_param.setDefaultButton(QMessageBox.Ok)
                    error_param.exec_()
                else:
                    # Create 'x' coordinate
                    t = np.linspace(eval(self.from_line.text()), eval(self.to_line.text()), 100)
                    # Clearing old figure
                    self.figure.clear()
                    # Create an axis
                    ax = self.figure.add_subplot(111)
                    # Create cartesian coordinate system
                    ax.spines["left"].set_position(("data", 0))
                    ax.spines["bottom"].set_position(("data", 0))
                    ax.spines["top"].set_visible(False)
                    ax.spines["right"].set_visible(False)
                    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
                    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
                    # Create 'y' coordinate
                    y = 0
                    x = 0
                    try:
                        x = eval(self.nameLineEdit_x.text())
                        y = eval(self.nameLineEdit_y.text())
                    except (SyntaxError, NameError, AttributeError, ValueError, SyntaxWarning):
                        # Creating 'Error window'
                        error_param = QMessageBox()
                        error_param.setWindowTitle('Error')
                        error_param.setText('Incorrect input in the field "Enter Plot"!!!')
                        error_param.setIcon(QMessageBox.Warning)
                        error_param.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                        error_param.setDefaultButton(QMessageBox.Ok)
                        error_param.exec_()
                    else:
                        # Creating plot
                        ax.plot(x, y)
                        # Refresh canvas
                        self.canvas.draw()

    def show_new_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()