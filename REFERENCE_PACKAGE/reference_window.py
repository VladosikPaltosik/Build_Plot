
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# Create reference class
class ReferenceWindow(QWidget):

    # Constructor of the class Window
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Reference')
        self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_DesktopIcon')))
        layout = QVBoxLayout()
        self.setFixedSize(500, 450)
        self.label = QLabel("In this reference you find out how to correctly use this app.")

        self.label_rule = QLabel('\nRules:\n1. To add, subtract, multiply divide and power you should use\n'
                                 '"+", "-", "*", "/", "**"\n'
                                 '2. To build plot all fields of app should be filled.\n'
                                 '3. To add 2 or more plots you should use ";" between them.\n'
                                 '4. Before the function and constants, which you can examine in the\n'
                                 'table below, you should use "np." for correct work of app.\n'
                                 '\nFunctions and constants:')
        self.label.setFont(QFont('Times', 12))
        self.label_rule.setFont(QFont('Times', 12))

        # Crate table of functions
        self.create_table()

        # Add widgets
        layout.addWidget(self.label)
        layout.addWidget(self.label_rule)
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def create_table(self):
        self.table_widget = QTableWidget()

        # Row count
        self.table_widget.setRowCount(17)

        # Column count
        self.table_widget.setColumnCount(2)

        # Crate table
        self.table_widget.setItem(0, 0, QTableWidgetItem("np.cos()"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("Trigonometric sine."))
        self.table_widget.setItem(1, 0, QTableWidgetItem("np.sin()"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("Trigonometric cosine."))
        self.table_widget.setItem(2, 0, QTableWidgetItem("np.tan()"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("Compute tangent."))
        self.table_widget.setItem(3, 0, QTableWidgetItem("np.arcsin()"))
        self.table_widget.setItem(3, 1, QTableWidgetItem("Inverse sine."))
        self.table_widget.setItem(4, 0, QTableWidgetItem("np.arccos()"))
        self.table_widget.setItem(4, 1, QTableWidgetItem("Trigonometric inverse cosine."))
        self.table_widget.setItem(5, 0, QTableWidgetItem("np.arctan()"))
        self.table_widget.setItem(5, 1, QTableWidgetItem("Trigonometric inverse tangent."))
        self.table_widget.setItem(6, 0, QTableWidgetItem("np.exp()"))
        self.table_widget.setItem(6, 1, QTableWidgetItem("Calculate the exponential."))
        self.table_widget.setItem(7, 0, QTableWidgetItem("np.log()"))
        self.table_widget.setItem(7, 1, QTableWidgetItem("Natural logarithm."))
        self.table_widget.setItem(8, 0, QTableWidgetItem("np.log10()"))
        self.table_widget.setItem(8, 1, QTableWidgetItem("Base-10 logarithm of x."))
        self.table_widget.setItem(9, 0, QTableWidgetItem("np.log2()"))
        self.table_widget.setItem(9, 1, QTableWidgetItem("Base-2 logarithm of x."))
        self.table_widget.setItem(10, 0, QTableWidgetItem("np.power(x1, x2)"))
        self.table_widget.setItem(10, 1, QTableWidgetItem("x1 raised to powers from x2"))
        self.table_widget.setItem(11, 0, QTableWidgetItem("np.sqrt()"))
        self.table_widget.setItem(11, 1, QTableWidgetItem("Root of the element."))
        self.table_widget.setItem(12, 0, QTableWidgetItem("np.sinh()"))
        self.table_widget.setItem(12, 1, QTableWidgetItem("Hyperbolic sine"))
        self.table_widget.setItem(13, 0, QTableWidgetItem("np.cosh()"))
        self.table_widget.setItem(13, 1, QTableWidgetItem("Hyperbolic cosine"))
        self.table_widget.setItem(14, 0, QTableWidgetItem("np.tanh()"))
        self.table_widget.setItem(14, 1, QTableWidgetItem("Hyperbolic tangent"))
        self.table_widget.setItem(15, 0, QTableWidgetItem("np.pi"))
        self.table_widget.setItem(15, 1, QTableWidgetItem("pi = 3.14159265358..."))
        self.table_widget.setItem(16, 0, QTableWidgetItem("np.e"))
        self.table_widget.setItem(16, 1, QTableWidgetItem("e = 2.718281828459..."))

        # Table will fit the screen horizontally
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
