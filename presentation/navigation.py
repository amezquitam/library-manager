
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy
from config.fonts import fonts


class Navigation(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)

        h_layout = QHBoxLayout()

        app_title = QLabel('Library Manager')
        # config font
        app_title_font = fonts['Sugoe UI']
        app_title_font.setPointSize(24)
        # config widget
        app_title.setFont(app_title_font)
        app_title.setStyleSheet('color: #fff; margin: 0')

        add_book_button = QPushButton('Add a Book', parent=self)
        add_book_button.setStyleSheet(
            """
            border: 1px solid #efefef;
            background-color: #088F8F;
            padding: 10px 0px;
            font-size: 16px;
            color: #fff;
            """
        )
        add_book_button.setFixedWidth(130)

        h_layout.addWidget(app_title)
        h_layout.addWidget(add_book_button)

        self.setLayout(h_layout)

