import sys
from BUILD_PLOTS.GUI_PACKEGE.param_window import *
from BUILD_PLOTS.GUI_PACKEGE.polar_window import *
from BUILD_PLOTS.GUI_PACKEGE.simple_window import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# Main window
class MainWindow(QWidget):

    # Constructor of main window
    def __init__(self):
        super().__init__()
        self.window1 = SimpleWindow()
        self.window2 = ParamWindow()
        self.window3 = PolarWindow()

        self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_DesktopIcon')))
        self.setFixedSize(400, 150)
        layout = QVBoxLayout()

        label = QLabel('     Which type of function you would like to build?')
        label.setFont(QFont('Times', 12))

        # Create button to create simple functions
        self.button1 = QPushButton("Simple Function")
        self.button1.setStyleSheet("QPushButton"
                                  "{"
                                  "background-color : lightblue;"
                                  "}"
                                  "QPushButton::pressed"
                                  "{"
                                  "background-color : red;"
                                  "}"
                                  )
        self.button1.setToolTip("Push to start build simple functions")
        self.button1.setFont(QFont('Times', 12))
        self.button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )

        # Create button to create parametric functions
        self.button2 = QPushButton("Parametric function")
        self.button2.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightblue;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : red;"
                                   "}"
                                   )
        self.button2.setToolTip("Push to start build parametric functions")
        self.button2.setFont(QFont('Times', 12))
        self.button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )

        # Create button to create Polar coordinate
        self.button3 = QPushButton("Polar coordinate")
        self.button3.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightblue;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : red;"
                                   "}"
                                   )
        self.button3.setToolTip("Push to start build Polar coordinate")
        self.button3.setFont(QFont('Times', 12))
        self.button3.clicked.connect(
            lambda checked: self.toggle_window(self.window3)
        )

        layout.addWidget(label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()


# Driver code
if __name__ == '__main__':
    # Creating a pyqt5 application
    app = QApplication(sys.argv)
    app.setApplicationName("Built Plot App")
    # Creating a window object
    main = MainWindow()
    # Showing the window
    main.show()
    # Loop
    sys.exit(app.exec_())