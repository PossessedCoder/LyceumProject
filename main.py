import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor
from cypher_algoritms import *
from ui import Ui_Form
from dialogs.settings_dialog import Settings_dialog


class App:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.app.setStyle("Fusion")
        self.ui.setupUi(self.form)
        self.theme_switch()
        self.ui.theme_switch_button.clicked.connect(self.theme_switch)
        self.ui.pass_gen_button.clicked.connect(self.pass_gen)
        self.ui.open_cypher_button.clicked.connect(self.open_cypher)
        self.ui.save_cypher_button.clicked.connect(self.save_cypher)
        for el in codings_dict.keys():
            self.ui.cypher_list.addItem(el)
        self.ui.decrypt_button.clicked.connect(self.decrypt)
        self.ui.encrypt_button.clicked.connect(self.encrypt)

    def theme_switch(self):
        if self.app.palette().color(QPalette.Window).getRgb() != (53, 53, 53, 255):
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
            palette.setColor(QPalette.Base, QColor(25, 25, 25))
            palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
            palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
            palette.setColor(QPalette.Text, QColor(255, 255, 255))
            palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
            palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
            palette.setColor(QPalette.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
            self.app.setPalette(palette)
        else:
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(255 - 53, 255 - 53, 255 - 53))
            palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
            palette.setColor(QPalette.Base, QColor(255 - 25, 255 - 25, 255 - 25))
            palette.setColor(QPalette.AlternateBase, QColor(255 - 53, 255 - 53, 255 - 53))
            palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
            palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
            palette.setColor(QPalette.Text, QColor(0, 0, 0))
            palette.setColor(QPalette.Button, QColor(255 - 53, 255 - 53, 255 - 53))
            palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
            palette.setColor(QPalette.BrightText, QColor(0, 255, 255))
            palette.setColor(QPalette.Link, QColor(255 - 42, 255 - 130, 255 - 218))
            palette.setColor(QPalette.Highlight, QColor(255 - 42, 255 - 130, 255 - 218))
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
            self.app.setPalette(palette)

    def pass_gen(self):
        self.ui.password_gen_out.setPlainText(password_gen(8, True, True, True, True))

    def save_cypher(self):
        try:
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.form, "Save File", ".",
                                                                "Текстовые файлы (*.txt);;Файлы данных(*.dat)")
            if filename:
                with open(filename, 'w') as file:
                    file.write(self.ui.cypher_out.toPlainText())
        except Exception as e:
            pass

    def open_cypher(self):
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(self.form,
                                                         'Выберите файл', '',
                                                         'Текстовые файлы (*.txt);;Файлы данных (*.dat)')[0]
            with open(file, 'r') as f:
                self.ui.cypher_inp.setText(f.read())
        except Exception as e:
            pass

    def decrypt(self):
        a = codings_dict[self.ui.cypher_list.currentText()]
        self.ui.cypher_out.setText(a.decode(self.ui.cypher_inp.toPlainText()))

    def encrypt(self):
        a = codings_dict[self.ui.cypher_list.currentText()]
        self.ui.cypher_out.setText(a.code(self.ui.cypher_inp.toPlainText()))

    def run(self):
        self.form.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    app = App()
    app.run()
