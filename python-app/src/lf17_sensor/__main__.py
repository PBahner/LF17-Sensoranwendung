from PySide6.QtWidgets import QApplication
from main_window import Display


def main() -> None:
    app = QApplication()
    window = Display()

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
