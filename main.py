import sys
from PyQt5.QtWidgets import QApplication
from janela import Janela


def main():
    app = QApplication(sys.argv)

    window = Janela()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()