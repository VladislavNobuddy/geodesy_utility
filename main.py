import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from counter import to_get_result
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Clear_first.clicked.connect(self.clear_first_func)
        self.ui.Clear_second.clicked.connect(self.clear_second_func)

        self.ui.Count.clicked.connect(self.count_func)

        self.ui.Clear_first_length.clicked.connect(self.clear_first_length_func)
        self.ui.Clear_second_length.clicked.connect(self.clear_second_length_func)

    def clear_first_func(self):
        self.ui.First_x.setText("")
        self.ui.First_y.setText("")

    def clear_second_func(self):
        self.ui.Second_x.setText("")
        self.ui.Second_y.setText("")

    def clear_first_length_func(self):
        self.ui.length_first.setText("")

    def clear_second_length_func(self):
        self.ui.lenght_second.setText("")

    def count_func(self):
        try:
            response = to_get_result(x1=float(self.ui.First_x.text().replace(",", ".")), y1=float(self.ui.First_y.text().replace(",", ".")), x2=float(self.ui.Second_x.text().replace(",", ".")), y2=float(self.ui.Second_y.text().replace(",", ".")), gamma=float(self.ui.angle.text().replace(",", ".")), an=float(self.ui.length_first.text().replace(",", ".")), bn=float(self.ui.lenght_second.text().replace(",", ".")))

            self.ui.Result_x.setText("X: " + str(response[0]))
            self.ui.Result_y.setText("Y: " + str(response[1]))

        except ValueError:
            self.ui.Result_x.setText("Недостаточно данных")
            self.ui.Result_y.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())