
from PyQt5 import QtCore, QtGui, QtWidgets



class FAQ(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Form")
        self.resize(612, 300)
        self.setMinimumSize(QtCore.QSize(612, 300))
        self.setMaximumSize(QtCore.QSize(612, 300))
        font = QtGui.QFont()
        font.setFamily("SamsungOneUI")
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(90, 90, 90);")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 611, 301))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FAQ"))
        Form.plainTextEdit.setPlainText(
            _translate("Form", "В режиме генерации вы можете выбрать биом который будет сгенерирован\n"
                               "\n"
                               "  Уровни: Уровень каждого слоя показывает максимальное значение альфа-канала пикселя для отрисовки какого-то конкретного цвета. Чем выше значение уровня- тем больше данного цвета будет на карте\n"
                               "\n"
                               "Для правильного отображения уровней каждый следующий ползунок зависит от предыдущего, а точнее его минимальное значение становится (значение предыдущего ползунка + 1) \n"
                               "\n"
                               "\n"
                               "Можно отключить отдельный слой с помощью галочки сбоку.\n"
                               "\n"
                               "\n"
                               " По умолчанию уже установлены оптимальные настройки отображения, но вы можете поставить свои значения. "))
