import os
import sys
from PySide2.QtWidgets import QApplication, QStyleFactory
from app import MainWindow

# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
