# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(922, 877)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.save_cypher_button = QtWidgets.QPushButton(Form)
        self.save_cypher_button.setObjectName("save_cypher_button")
        self.file_work_button_group = QtWidgets.QButtonGroup(Form)
        self.file_work_button_group.setObjectName("file_work_button_group")
        self.file_work_button_group.addButton(self.save_cypher_button)
        self.horizontalLayout_2.addWidget(self.save_cypher_button)
        self.open_cypher_button = QtWidgets.QPushButton(Form)
        self.open_cypher_button.setObjectName("open_cypher_button")
        self.file_work_button_group.addButton(self.open_cypher_button)
        self.horizontalLayout_2.addWidget(self.open_cypher_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.enc_dec_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(15)
        self.enc_dec_label.setFont(font)
        self.enc_dec_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enc_dec_label.setObjectName("enc_dec_label")
        self.verticalLayout_4.addWidget(self.enc_dec_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cypher_inp = QtWidgets.QTextEdit(Form)
        self.cypher_inp.setObjectName("cypher_inp")
        self.horizontalLayout_3.addWidget(self.cypher_inp)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cypher_list = QtWidgets.QComboBox(Form)
        self.cypher_list.setObjectName("cypher_list")
        self.verticalLayout_2.addWidget(self.cypher_list)
        self.decrypt_button = QtWidgets.QPushButton(Form)
        self.decrypt_button.setObjectName("decrypt_button")
        self.cypher_button_group = QtWidgets.QButtonGroup(Form)
        self.cypher_button_group.setObjectName("cypher_button_group")
        self.cypher_button_group.addButton(self.decrypt_button)
        self.verticalLayout_2.addWidget(self.decrypt_button)
        self.encrypt_button = QtWidgets.QPushButton(Form)
        self.encrypt_button.setObjectName("encrypt_button")
        self.cypher_button_group.addButton(self.encrypt_button)
        self.verticalLayout_2.addWidget(self.encrypt_button)
        self.reference_button = QtWidgets.QPushButton(Form)
        self.reference_button.setObjectName("reference_button")
        self.verticalLayout_2.addWidget(self.reference_button)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.cypher_out = QtWidgets.QTextEdit(Form)
        self.cypher_out.setObjectName("cypher_out")
        self.horizontalLayout_3.addWidget(self.cypher_out)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.password_gen_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(15)
        self.password_gen_label.setFont(font)
        self.password_gen_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_gen_label.setObjectName("password_gen_label")
        self.verticalLayout_5.addWidget(self.password_gen_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pass_gen_button = QtWidgets.QPushButton(Form)
        self.pass_gen_button.setObjectName("pass_gen_button")
        self.horizontalLayout_4.addWidget(self.pass_gen_button)
        self.password_gen_out = QtWidgets.QPlainTextEdit(Form)
        self.password_gen_out.setObjectName("password_gen_out")
        self.horizontalLayout_4.addWidget(self.password_gen_out)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.password_save_button = QtWidgets.QPushButton(Form)
        self.password_save_button.setObjectName("password_save_button")
        self.bd_view = QtWidgets.QPushButton(Form)
        self.bd_view.setObjectName("bd_view")
        self.verticalLayout_3.addWidget(self.password_save_button)
        self.verticalLayout_3.addWidget(self.bd_view)
        self.settings = QtWidgets.QPushButton(Form)
        self.settings.setObjectName("settings")
        self.verticalLayout_3.addWidget(self.settings)
        self.theme_switch_button = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.theme_switch_button.setIcon(icon)
        self.theme_switch_button.setObjectName("theme_switch_button")
        self.verticalLayout_3.addWidget(self.theme_switch_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save_cypher_button.setText(_translate("Form", "Сохранить"))
        self.open_cypher_button.setText(_translate("Form", "Открыть"))
        self.enc_dec_label.setText(_translate("Form", "Шифровальщик/Дешифровальщик"))
        self.cypher_inp.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.decrypt_button.setText(_translate("Form", "Расшифровать"))
        self.encrypt_button.setText(_translate("Form", "Зашифровать"))
        self.password_gen_label.setText(_translate("Form", "Генератор паролей"))
        self.pass_gen_button.setText(_translate("Form", "Сгенерировать пароль"))
        self.password_save_button.setText(_translate("Form", "Сохранить пароль"))
        self.settings.setText(_translate("Form", "Settings"))
        self.reference_button.setText(_translate('Form', 'Справка'))
        self.theme_switch_button.setText(_translate("Form", "theme_switch"))
        self.bd_view.setText(_translate('Form', 'Посмотреть пароли'))


# class MyWidget(QtWidgets):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('01.ui', self)  # Загружаем дизайн
#         self.pushButton.clicked.connect(self.run)
#         # Обратите внимание: имя элемента такое же как в QTDesigner
#
#     def run(self):
#         self.label.setText("OK")
        # Имя элемента совпадает с objectName в QTDesigner