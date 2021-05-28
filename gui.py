from PyQt5 import QtCore, QtGui, QtWidgets
import downloadyoutube


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(485, 272)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.txtUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUrl.setGeometry(QtCore.QRect(80, 200, 350, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtUrl.setFont(font)
        self.txtUrl.setText("")
        self.txtUrl.setObjectName("txtUrl")
        self.btnDownload = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.downloadPressed())
        self.btnDownload.setGeometry(QtCore.QRect(210, 230, 61, 23))
        self.btnDownload.setObjectName("btnDownload")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 90, 141, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.progressBar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -150, 500, 771))
        self.background.setStyleSheet("background-image: url(background.jpg)")
        self.background.setText("")
        self.background.setObjectName("background")
        self.background.raise_()
        self.txtUrl.raise_()
        self.btnDownload.raise_()
        self.progressBar.raise_()
        window.setCentralWidget(self.centralwidget)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Youtube Downloader"))
        self.btnDownload.setText(_translate("window", "Download"))

    # Sets the progressbar.
    def setProgress(self, amount):
        self.progressBar.setProperty("value", amount)

    # This happens when the download button is clicked.
    def downloadPressed(self):
        link = self.txtUrl.text()
        print(link)
        downloadyoutube.download_video(link)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
