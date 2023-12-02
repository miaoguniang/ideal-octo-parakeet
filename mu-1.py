from PyQt5.QtWidgets import QApplication, QMainWindow
from mu import *


class muwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def showMinimized(self):  # 最小化窗口
        super().showMinimized()

    def closeEvent(self, event):  # 关闭窗口
        super().closeEvent(event)

    def update(self):
        total = 0.0
        for i in range(self.ui.xiaoshoudan.rowCount()):
            self.ui.xiaoshoudan.item(i, 5)
        if self.ui.xiaoshoudan.item is not None:
            total += float(self.ui.xiaoshoudan.item.text())
        self.ui.pushButton.setText(f'{total:.2f}')

    def mousePressEvent(self, event): # 拖动窗口
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
             self.m_flag = True
             self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
             event.accept()
             self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
             self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
             mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

if __name__ == "__main__":
    app = QApplication([])
    win = muwindow()
    win.show()
    app.exec_()