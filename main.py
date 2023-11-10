import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor

from cypher_algoritms import *
from dialogs.bd_view import Bd_view
from dialogs.register import Registration
from dialogs.settings_dialog import Settings_dialog
from scbd import *
from ui import Ui_Form


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
        self.key_buttonn = QtWidgets.QSpinBox(self.form)
        self.key_buttonw = QtWidgets.QLineEdit(self.form)
        self.key_buttonw.setFixedHeight(20)
        self.key_buttonw.setFixedWidth(110)
        self.key_buttonw.hide()
        self.key_buttonn.hide()
        self.ui.verticalLayout_2.addWidget(self.key_buttonn)
        self.ui.verticalLayout_2.addWidget(self.key_buttonw)
        for el in codings_dict.keys():
            self.ui.cypher_list.addItem(el)
        self.ui.cypher_list.currentIndexChanged.connect(self.flag_check)
        self.flags = []
        self.active_but = None
        self.ui.decrypt_button.clicked.connect(self.decrypt)
        self.ui.encrypt_button.clicked.connect(self.encrypt)
        self.ui.settings.clicked.connect(self.settings_open)
        self.ui.password_save_button.clicked.connect(self.register_open)
        self.ui.reference_button.clicked.connect(self.reference_show)
        self.ui.bd_view.clicked.connect(self.bd_view)
        self.password_gen_settings = None
        self.last_edited_login = None
        self.last_edited_table_item = None

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
        except TypeError:
            self.settings_open()

    @staticmethod
    def error_call(text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle("Error")
        msg.exec_()

    @staticmethod
    def info_call(text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setWindowTitle("Info")
        msg.exec_()

    def reference_show(self):
        self.info_call(codings_info[self.ui.cypher_list.currentText()])

    def save_cypher(self):
        try:
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.form, "Save File", ".",
                                                                "Текстовые файлы (*.txt)")
            if filename:
                with open(filename, 'w') as file:
                    file.write(self.ui.cypher_out.toPlainText())
        except Exception:
            pass

    def open_cypher(self):
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(self.form,
                                                         'Выберите файл', '',
                                                         'Текстовые файлы (*.txt)')[0]
            with open(file, 'r') as f:
                self.ui.cypher_inp.setText(f.read())
        except Exception:
            pass

    def flag_check(self):
        if 'keyn' in codings_dict[self.ui.cypher_list.currentText()][1]:
            self.ui.verticalLayout_2.addWidget(self.key_buttonn)
            self.active_but = self.key_buttonn
            self.key_buttonn.show()
            self.key_buttonw.hide()
        elif 'keyw' in codings_dict[self.ui.cypher_list.currentText()][1]:
            self.ui.verticalLayout_2.addWidget(self.key_buttonw)
            self.active_but = self.key_buttonw
            self.key_buttonw.show()
            self.key_buttonn.hide()
        else:
            self.key_buttonn.hide()
            self.key_buttonw.hide()
        self.flags = codings_dict[self.ui.cypher_list.currentText()][1]

    def decrypt(self):
        if not self.flags:
            a = codings_dict[self.ui.cypher_list.currentText()][0]
            self.ui.cypher_out.setText(a.decode(self.ui.cypher_inp.toPlainText()))
        elif 'keyn' in self.flags:
            a = codings_dict[self.ui.cypher_list.currentText()][0]
            self.ui.cypher_out.setText(a.decode(self.ui.cypher_inp.toPlainText(), self.key_buttonn.value()))
        elif 'keyw' in self.flags:
            a = codings_dict[self.ui.cypher_list.currentText()][0]
            if self.key_buttonw.text().strip() != '':
                try:
                    self.ui.cypher_out.setText(a.decode(self.ui.cypher_inp.toPlainText(), self.key_buttonw.text()))
                except ZeroDivisionError:
                    self.error_call('Ключ шифрования должен содержать буквы русского или английского алфавитов')
            else:
                self.error_call('Нет ключа шифрования')

    def encrypt(self):
        if not self.flags:
            a = codings_dict[self.ui.cypher_list.currentText()][0]
            self.ui.cypher_out.setText(a.code(self.ui.cypher_inp.toPlainText()))
        elif 'keyn' in self.flags:
            a = codings_dict[self.ui.cypher_list.currentText()][0]
            self.ui.cypher_out.setText(a.code(self.ui.cypher_inp.toPlainText(), self.key_buttonn.value()))
        elif 'keyw' in self.flags:
            a = codings_dict[self.ui.cypher_list.currentText()][0]
            if self.key_buttonw.text().strip() != '':
                try:
                    self.ui.cypher_out.setText(a.code(self.ui.cypher_inp.toPlainText(), self.key_buttonw.text()))
                except ZeroDivisionError:
                    self.error_call('Ключ шифрования должен содержать буквы русского или английского алфавитов')
            else:
                self.error_call('Нет ключа шифрования')

    def settings_open(self):
        form = QtWidgets.QDialog()
        dialog = Settings_dialog()
        dialog.setupUi(form)
        dialog.accept_button.clicked.connect(lambda x: self.checked_close(form, dialog))
        form.exec_()

    def register_open(self):
        form = QtWidgets.QDialog()
        dialog = Registration()
        dialog.setupUi(form)
        dialog.password.setText(self.ui.password_gen_out.toPlainText())
        dialog.accept_button.clicked.connect(lambda x: self.checked_close(form, dialog))
        form.exec_()

    def bd_view(self):
        form = QtWidgets.QDialog()
        dialog = Bd_view()
        dialog.setupUi(form)
        for value in show_all_data():
            for i in range(len(value[1])):
                dialog.table.insertRow(dialog.table.rowCount())
                dialog.table.setItem(dialog.table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(value[0]))
                dialog.table.setItem(dialog.table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(value[1][i][0]))
                dialog.table.setItem(dialog.table.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(value[1][i][1]))

        def add_login_visable():
            self.register_open()
            val = self.last_edited_login
            if val:
                dialog.table.insertRow(dialog.table.rowCount())
                dialog.table.setItem(dialog.table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(val[0]))
                dialog.table.setItem(dialog.table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(val[1]))
                dialog.table.setItem(dialog.table.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(val[2]))
            self.last_edited_login = None

        def delete_all_visable():
            delete_ALL()
            dialog.table.setRowCount(0)

        def double_clicked():
            row, col = dialog.table.selectionModel().selection().indexes()[0].row(), \
                dialog.table.selectionModel().selection().indexes()[0].column()
            self.last_edited_table_item = (dialog.table.item(row, 0).text(), dialog.table.item(row, 1).text(),
                                           dialog.table.item(row, 2).text())

        def edit_visiable(upd):
            if upd == '':
                try:
                    row, col, update = dialog.table.selectionModel().selection().indexes()[0].row(), \
                        dialog.table.selectionModel().selection().indexes()[0].column(), ''
                except IndexError:
                    self.error_call('Ничего не выделено')
                    return
            else:
                row, col, update = upd.row(), upd.column(), upd.text()
            try:
                login, password, notes = self.last_edited_table_item
                self.last_edited_table_item = None
            except TypeError:
                if upd == '':
                    login, password, notes = dialog.table.item(row, 0).text(), dialog.table.item(row, 1).text(), \
                        dialog.table.item(row, 2).text()
                else:
                    return
            if show_all_data() and \
                    len(tuple(
                        filter(lambda x: x[0] == login and (password, update) if col == 2 else (update, notes) in x[1],
                               show_all_data()))) > 1:
                self.error_call('Не может быть двух одинаковых комбинаций логина, пароля и примечаний')
                dialog.table.setItem(row, col, QtWidgets.QTableWidgetItem(password) if col == 1 else
                QtWidgets.QTableWidgetItem(notes))
                return
            if col == 0:
                if not upd:
                    delete_login(dialog.table.item(row, col).text())
                    dialog.table.removeRow(row)
            elif col == 1:
                if not upd:
                    dialog.table.setItem(row, col, QtWidgets.QTableWidgetItem(update))
                edit_password(login, password, notes, update)
            elif col == 2:
                if not upd:
                    dialog.table.setItem(row, col, QtWidgets.QTableWidgetItem(update))
                edit_notes(login, password, notes, update)

        dialog.accept_button.clicked.connect(lambda x: self.checked_close(form, dialog))
        dialog.add.clicked.connect(add_login_visable)
        dialog.delete_all.clicked.connect(delete_all_visable)
        dialog.delete.clicked.connect(lambda: edit_visiable(''))
        dialog.table.itemChanged.connect(edit_visiable)
        dialog.table.doubleClicked.connect(double_clicked)

        form.exec_()

    def checked_close(self, form, dialog):
        if isinstance(dialog, Settings_dialog):
            value = (int(dialog.length_choice.text()),
                     [b.isChecked() for b in dialog.spec_symb_buttgroup.buttons()],
                     [b.isChecked() for b in dialog.num_buttgroup.buttons()][::-1],
                     [b.isChecked() for b in dialog.upper_buttgroup.buttons()][::-1],
                     [b.isChecked() for b in dialog.lower_buttgroup.buttons()])
            if value[0] <= 0:
                self.error_call('Длина пароля не может быть равна 0')
                return value
            if not any([el[0] for el in value[1::]]):
                self.error_call('Недостаточно параметров')
                return value
            form.close()
            self.password_gen_settings = value
        elif isinstance(dialog, Registration):
            value = (dialog.login.toPlainText(), dialog.password.toPlainText(), dialog.notes.toPlainText())
            if len(value[0]) <= 0:
                self.error_call('Длина логина не может быть пустым')
            elif len(value[1]) <= 0:
                self.error_call('Длина пароля не может быть пустым')
            elif len(value[2]) <= 0:
                self.error_call('Длина примечаний не может быть пустым')
            elif show_all_data() and \
                    tuple(filter(lambda x: x[0] == value[0] and tuple(value[1:]) in x[1], show_all_data())):
                self.error_call('Не может быть двух одинаковых комбинаций логина, пароля и примечаний')
            else:
                try:
                    add_login(value[0])
                    add_data(*value[1:], value[0])
                except LoginInTableError:
                    add_data(*value[1:], value[0])
                finally:
                    self.last_edited_login = value
                    form.close()
        elif isinstance(dialog, Bd_view):
            form.close()

    def run(self):
        self.form.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    app = App()
    app.run()

# Это буду редачить
