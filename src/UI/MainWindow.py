import json
import webbrowser

from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon, QFont

from utils import global_path
from src.UI.menubar import menubar
from src.UI.window import window
from src.utils import font
from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMainWindow,
)


class vysiz_UI_MainWindow(QMainWindow):
    def __init__(self):
        super(vysiz_UI_MainWindow, self).__init__()
        font.load_font(w=self)
        with open(global_path.get_proj_abs_path("config/config.json"), "r") as j:
            self.config = json.load(j)

        widget = QWidget()
        menubar.setup(w=self)
        window.setup(w=self)

        self.GRID = QGridLayout(widget)
        self.initUI()

    def initUI(self):
        with open(
            file=global_path.get_proj_abs_path("assets/stylesheet.txt"), mode="r"
        ) as f:
            self.setStyleSheet(f.read())

        self.setLayout(self.GRID)
