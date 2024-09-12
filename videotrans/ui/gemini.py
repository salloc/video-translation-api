# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets

from videotrans.configure import config


class Ui_geminiform(object):
    def setupUi(self, geminiform):
        self.has_done = False
        geminiform.setObjectName("geminiform")
        geminiform.setWindowModality(QtCore.Qt.NonModal)
        geminiform.resize(600, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(geminiform.sizePolicy().hasHeightForWidth())
        geminiform.setSizePolicy(sizePolicy)
        geminiform.setMaximumSize(QtCore.QSize(600, 500))

        self.label_2 = QtWidgets.QLabel(geminiform)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 130, 35))
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.gemini_key = QtWidgets.QLineEdit(geminiform)
        self.gemini_key.setGeometry(QtCore.QRect(150, 40, 431, 35))
        self.gemini_key.setMinimumSize(QtCore.QSize(0, 35))
        self.gemini_key.setObjectName("gemini_key")

        self.label_3 = QtWidgets.QLabel(geminiform)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 121, 16))
        self.label_3.setObjectName("label_3")
        self.model = QtWidgets.QComboBox(geminiform)
        self.model.setGeometry(QtCore.QRect(150, 95, 431, 35))
        self.model.setMinimumSize(QtCore.QSize(0, 35))
        self.model.setObjectName("model")

        self.label_allmodels = QtWidgets.QLabel(geminiform)
        self.label_allmodels.setGeometry(QtCore.QRect(10, 140, 571, 21))
        self.label_allmodels.setObjectName("label_allmodels")
        self.label_allmodels.setText(
            '填写所有可用模型，以英文逗号分隔，填写后可在上方选择' if config.defaulelang == 'zh' else 'Fill in all available models, separated by commas. After filling in, you can select them above')

        self.edit_allmodels = QtWidgets.QPlainTextEdit(geminiform)
        self.edit_allmodels.setGeometry(QtCore.QRect(10, 175, 571, 60))
        self.edit_allmodels.setObjectName("edit_allmodels")

        self.label_4 = QtWidgets.QLabel(geminiform)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 571, 21))
        self.label_4.setObjectName("label_4")
        self.gemini_template = QtWidgets.QPlainTextEdit(geminiform)
        self.gemini_template.setGeometry(QtCore.QRect(10, 275, 571, 151))
        self.gemini_template.setObjectName("gemini_template")

        self.set_gemini = QtWidgets.QPushButton(geminiform)
        self.set_gemini.setGeometry(QtCore.QRect(10, 440, 93, 35))
        self.set_gemini.setMinimumSize(QtCore.QSize(0, 35))
        self.set_gemini.setObjectName("set_gemini")

        self.retranslateUi(geminiform)
        QtCore.QMetaObject.connectSlotsByName(geminiform)

    def retranslateUi(self, geminiform):
        geminiform.setWindowTitle("Gemini Pro")
        self.gemini_template.setPlaceholderText("prompt")
        self.label_4.setText(
            "{lang}代表目标语言名称，不要删除。" if config.defaulelang == 'zh' else "{lang} represents the target language name, do not delete it.")
        self.set_gemini.setText('保存' if config.defaulelang == 'zh' else "Save")
        self.gemini_key.setPlaceholderText("secret key")
        self.label_2.setText("Gemini  Key ")
        self.label_3.setText('选择模型' if config.defaulelang == 'zh' else "Select model")
