# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets

from videotrans.configure import config


class Ui_azureform(object):
    def setupUi(self, azureform):
        self.has_done = False
        azureform.setObjectName("azureform")
        azureform.setWindowModality(QtCore.Qt.NonModal)
        azureform.resize(600, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(azureform.sizePolicy().hasHeightForWidth())
        azureform.setSizePolicy(sizePolicy)
        azureform.setMaximumSize(QtCore.QSize(600, 580))
        self.label = QtWidgets.QLabel(azureform)
        self.label.setGeometry(QtCore.QRect(10, 10, 130, 35))
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.azure_api = QtWidgets.QLineEdit(azureform)
        self.azure_api.setGeometry(QtCore.QRect(150, 10, 431, 35))
        self.azure_api.setMinimumSize(QtCore.QSize(0, 35))
        self.azure_api.setObjectName("azure_api")

        self.label_2 = QtWidgets.QLabel(azureform)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 130, 35))
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")

        self.azure_key = QtWidgets.QLineEdit(azureform)
        self.azure_key.setGeometry(QtCore.QRect(150, 60, 431, 35))
        self.azure_key.setMinimumSize(QtCore.QSize(0, 35))
        self.azure_key.setObjectName("azure_key")

        self.label_version = QtWidgets.QLabel(azureform)
        self.label_version.setGeometry(QtCore.QRect(10, 120, 121, 16))
        self.label_version.setObjectName("label_version")
        self.azure_version = QtWidgets.QComboBox(azureform)
        self.azure_version.setGeometry(QtCore.QRect(130, 110, 451, 35))
        self.azure_version.setMinimumSize(QtCore.QSize(0, 35))
        self.azure_version.setObjectName("azure_version")
        self.azure_version.addItems([
            "2024-06-01",
            "2024-08-01-preview",
            "2024-07-01-preview",
            "2024-05-01-preview",
            "2024-04-01-preview",
            "2024-03-01-preview",
            "2024-02-01"
        ])

        self.label_3 = QtWidgets.QLabel(azureform)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 121, 16))
        self.label_3.setObjectName("label_3")
        self.azure_model = QtWidgets.QComboBox(azureform)
        self.azure_model.setGeometry(QtCore.QRect(130, 150, 451, 35))
        self.azure_model.setMinimumSize(QtCore.QSize(0, 35))
        self.azure_model.setObjectName("azure_model")

        self.label_allmodels = QtWidgets.QLabel(azureform)
        self.label_allmodels.setGeometry(QtCore.QRect(10, 200, 571, 21))
        self.label_allmodels.setObjectName("label_allmodels")
        self.label_allmodels.setText(
            '填写所有可用模型，以英文逗号分隔，填写后可在上方选择' if config.defaulelang == 'zh' else 'Fill in all available models, separated by commas. After filling in, you can select them above')

        self.edit_allmodels = QtWidgets.QPlainTextEdit(azureform)
        self.edit_allmodels.setGeometry(QtCore.QRect(10, 230, 571, 100))
        self.edit_allmodels.setObjectName("edit_allmodels")

        self.label_4 = QtWidgets.QLabel(azureform)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 571, 21))
        self.label_4.setObjectName("label_4")
        self.azure_template = QtWidgets.QPlainTextEdit(azureform)
        self.azure_template.setGeometry(QtCore.QRect(10, 360, 571, 151))
        self.azure_template.setObjectName("azure_template")

        self.set_azure = QtWidgets.QPushButton(azureform)
        self.set_azure.setGeometry(QtCore.QRect(10, 540, 93, 35))
        self.set_azure.setMinimumSize(QtCore.QSize(0, 35))
        self.set_azure.setObjectName("set_azure")

        self.retranslateUi(azureform)
        QtCore.QMetaObject.connectSlotsByName(azureform)

    def retranslateUi(self, azureform):
        azureform.setWindowTitle("AzureGPT")
        self.label_3.setText("Azure Model")
        self.label_version.setText("API Version")
        self.azure_template.setPlaceholderText("prompt")
        self.label_4.setText(
            "{lang}代表目标语言名称，不要删除。" if config.defaulelang == 'zh' else "{lang} represents the target language name, do not delete it.")
        self.set_azure.setText('保存' if config.defaulelang == 'zh' else "Save")
        self.azure_api.setPlaceholderText('填写你的api地址' if config.defaulelang == 'zh' else "Api url")
        self.azure_key.setPlaceholderText('填写你的密钥' if config.defaulelang == 'zh' else "Secret key")
        self.label.setText("API URL")
        self.label_2.setText("Azure  Key ")
