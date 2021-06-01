
import numpy as np
import matplotlib.pyplot as plt
from BUILD_PLOTS.REFERENCE_PACKAGE.reference_window import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


# Polar coordinate window
class PolarWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_DesktopIcon')))
        self.setWindowTitle('Polar Function')
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

        # Create label to enter plot
        label = QLabel('Enter: r=', self)
        label.setFont(QFont('Times', 15))

        # Create label 'From' range
        label_from = QLabel('t ∈ [', self)
        label_from.setFont(QFont('Times', 15))

        # From_line label creating and style
        self.from_line = QLineEdit()
        self.from_line.setText('0')
        self.from_line.setFixedSize(50, 30)

        # To_line label creating and style
        self.to_line = QLineEdit()
        self.to_line.setText('2 * np.pi')
        self.to_line.setFixedSize(50, 30)

        # Create label 'To' range
        label_to = QLabel(']', self)
        label_to.setFont(QFont('Times', 15))

        # Creating a line edit
        self.nameLineEdit_r = QLineEdit()
        self.nameLineEdit_r.setText('np.sin(t)')
        self.nameLineEdit_r.setFixedSize(210, 30)

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
        form_layout.addRow(label, self.nameLineEdit_r)
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
        # First check error
        if not self.from_line.text() and not self.to_line.text() and not self.nameLineEdit_r.text():
            # Creating 'Error window'
            error = QMessageBox()
            error.setWindowTitle('Error')
            error.setText('All fields are empty!!!')
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            error.setDefaultButton(QMessageBox.Ok)
            error.exec_()
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
                error = QMessageBox()
                error.setWindowTitle('Error')
                error.setText('Incorrect input in range fields!!!')
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                error.setDefaultButton(QMessageBox.Ok)
                error.exec_()
            else:
                # create plots parameters
                if self.from_line.text() == '' or self.to_line.text() == '' or \
                        eval(self.from_line.text()) >= eval(self.to_line.text()):
                    # Creating 'Error window'
                    error = QMessageBox()
                    error.setWindowTitle('Error')
                    error.setText('Incorrect input in range fields!!!')
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                    error.setDefaultButton(QMessageBox.Ok)
                    error.exec_()
                else:
                    # Create 'x' coordinate
                    t = np.linspace(eval(self.from_line.text()), eval(self.to_line.text()), 100)
                    # Clearing old figure
                    self.figure.clear()
                    # Create an axis
                    ax = self.figure.add_subplot(111, projection='polar')
                    # Create 'y' coordinate
                    r = 0
                    try:
                        r = eval(self.nameLineEdit_r.text())
                    except (SyntaxError, NameError, AttributeError, ValueError, SyntaxWarning):
                        # Creating 'Error window'
                        error = QMessageBox()
                        error.setWindowTitle('Error')
                        error.setText('Incorrect input in the field "Enter Plot"!!!')
                        error.setIcon(QMessageBox.Warning)
                        error.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                        error.setDefaultButton(QMessageBox.Ok)
                        error.exec_()
                    else:
                        # Creating plot
                        ax.plot(t, r)
                        # Refresh canvas
                        self.canvas.draw()

    def show_new_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()