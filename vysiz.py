import os
import sys

from PySide6.QtWidgets import QApplication

from src.UI.MainWindow import vysiz_UI_MainWindow
from utils import global_path

global_path.set_proj_abs_path(os.path.abspath(__file__))
vysiz_QApplication = QApplication()
vysiz_window = vysiz_UI_MainWindow()
vysiz_window.show()
sys.exit(vysiz_QApplication.exec())
