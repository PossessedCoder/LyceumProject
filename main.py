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
        self.ui.settings.clicked.connect(self.settings_open)
        self.password_gen_settings = None

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
        try:
            self.ui.password_gen_out.setPlainText(
                password_gen(self.password_gen_settings[0], *map(lambda x: x[0], self.password_gen_settings[1:])))
            print(self.password_gen_settings)
        except TypeError as e:
            self.settings_open()

    @staticmethod
    def error_call(text, description):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(text)
        msg.setInformativeText(description)
        msg.setWindowTitle("Error")
        msg.exec_()

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

    def settings_open(self):
        form = QtWidgets.QDialog()
        dialog = Settings_dialog()
        dialog.setupUi(form)
        dialog.accept_button.clicked.connect(lambda x: self.checked_close(form, dialog))
        form.exec_()

    def checked_close(self, form, dialog):
        if isinstance(dialog, Settings_dialog):
            value = (int(dialog.length_choice.text()),
                     [b.isChecked() for b in dialog.spec_symb_buttgroup.buttons()],
                     [b.isChecked() for b in dialog.num_buttgroup.buttons()][::-1],
                     [b.isChecked() for b in dialog.upper_buttgroup.buttons()][::-1],
                     [b.isChecked() for b in dialog.lower_buttgroup.buttons()])
            if value[0] <= 0:
                self.error_call('Длина пароля не может быть равна 0', '')
                return value
            if not any([el[0] for el in value[1::]]):
                self.error_call('Недостаточно параметров', '')
                return value
            form.close()
            self.password_gen_settings = value

    def run(self):
        self.form.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    app = App()
    app.run()
