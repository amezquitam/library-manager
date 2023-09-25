from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt5.QtCore import Qt
from presentation.navigation import Navigation
from presentation.separator import Separator

import sys


class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.config()
    
    def config(self):
        self.setWindowTitle('Library Manager')
        self.resize(1024, 768)

        self.setStyleSheet('background-color: #1e2120; margin: 0')

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(65, 65, 65, 65)

        navigation = Navigation(self)
        separator = Separator()


        layout.addWidget(navigation)
        layout.addWidget(separator)

        self.setLayout(layout)


def show_main_view():
    app = QApplication(sys.argv)
    main_view = MainView()
    main_view.show()
    app.exec_()