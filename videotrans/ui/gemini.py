# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from videotrans.configure import config
from videotrans.util import tools


class Ui_geminiform(object):
    def setupUi(self, geminiform):
        self.has_done = False
        geminiform.setObjectName("geminiform")
        geminiform.setWindowModality(QtCore.Qt.NonModal)
        geminiform.resize(600, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(geminiform.sizePolicy().hasHeightForWidth())
        geminiform.setSizePolicy(sizePolicy)
        geminiform.setMaximumSize(QtCore.QSize(600, 500))

        v1 = QtWidgets.QVBoxLayout(geminiform)

        h1=QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel(geminiform)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.gemini_key = QtWidgets.QLineEdit(geminiform)
        self.gemini_key.setMinimumSize(QtCore.QSize(0, 35))
        self.gemini_key.setObjectName("gemini_key")
        h1.addWidget(self.label_2)
        h1.addWidget(self.gemini_key)
        v1.addLayout(h1)

        h2=QtWidgets.QHBoxLayout()
        self.label_3 = QtWidgets.QLabel(geminiform)
        self.label_3.setObjectName("label_3")
        self.model = QtWidgets.QComboBox(geminiform)
        self.model.setMinimumSize(QtCore.QSize(0, 35))
        self.model.setObjectName("model")
        h2.addWidget(self.label_3)
        h2.addWidget(self.model)
        v1.addLayout(h2)

        self.label_allmodels = QtWidgets.QLabel(geminiform)
        self.label_allmodels.setObjectName("label_allmodels")
        self.label_allmodels.setText(
            '填写所有可用模型，以英文逗号分隔，填写后可在上方选择' if config.defaulelang == 'zh' else 'Fill in all available models, separated by commas. After filling in, you can select them above')
        self.label_allmodels.setStyleSheet("color:#999")

        self.edit_allmodels = QtWidgets.QPlainTextEdit(geminiform)
        self.edit_allmodels.setObjectName("edit_allmodels")
        v1.addWidget(self.label_allmodels)
        v1.addWidget(self.edit_allmodels)

        self.label_4 = QtWidgets.QLabel(geminiform)
        self.label_4.setObjectName("label_4")
        self.gemini_template = QtWidgets.QPlainTextEdit(geminiform)
        self.gemini_template.setObjectName("gemini_template")
        v1.addWidget(self.label_4)
        v1.addWidget(self.gemini_template)


        self.label_srt=QtWidgets.QLabel(geminiform)
        self.label_srt.setObjectName("label_srt")
        
        hrecogn=QtWidgets.QHBoxLayout()        
        hrecogn.addWidget(self.label_srt)

        
        v1.addLayout(hrecogn)
        
        self.gemini_srtprompt=QtWidgets.QPlainTextEdit(geminiform)
        self.gemini_srtprompt.setObjectName("gemini_srtprompt")
        
        


        v1.addWidget(self.gemini_srtprompt)


        h3=QtWidgets.QHBoxLayout()
        self.set_gemini = QtWidgets.QPushButton(geminiform)
        self.set_gemini.setMinimumSize(QtCore.QSize(0, 35))
        self.set_gemini.setObjectName("set_gemini")
        
        self.test = QtWidgets.QPushButton(geminiform)
        self.test.setObjectName("test")

        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText("查看填写教程" if config.defaulelang == 'zh' else "Fill out the tutorial")
        help_btn.clicked.connect(lambda: tools.open_url(url='https://pyvideotrans.com/gemini'))

        h3.addWidget(self.set_gemini)
        h3.addWidget(self.test)
        h3.addWidget(help_btn)
        v1.addLayout(h3)



        self.retranslateUi(geminiform)
        QtCore.QMetaObject.connectSlotsByName(geminiform)

    def retranslateUi(self, geminiform):
        geminiform.setWindowTitle("Gemini Pro")
        self.gemini_template.setPlaceholderText("prompt")
        self.label_4.setText(
            "{lang}代表目标语言名称，不要删除。" if config.defaulelang == 'zh' else "{lang} represents the target language name, do not delete it.")
        self.label_4.setStyleSheet("color: #999;")
        self.set_gemini.setText('保存' if config.defaulelang == 'zh' else "Save")
        self.test.setText('测试' if config.defaulelang == 'zh' else "Test")
        self.gemini_key.setPlaceholderText("secret key")
        self.label_2.setText("Gemini  Key ")
        self.label_srt.setText('转录音视频为字幕时的提示词' if config.defaulelang=='zh' else 'Prompt for subtitles when converting audio to video')
        self.label_srt.setStyleSheet("color: #999;")
        self.label_3.setText('选择模型' if config.defaulelang == 'zh' else "Select model")
