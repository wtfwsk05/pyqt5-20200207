import sys
import demo
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)        # 创建应用对象
    mainWindow = QMainWindow()          # 创建主窗口对象
    ui = demo.Ui_MainWindow()           # 实例化类对象
    ui.setupUi(mainWindow)              # 在主窗口添加控件(需传入一个参数)
    mainWindow.show()                   # 显示窗口
    sys.exit(app.exec_())               # 进入程序主循环，并通过exit函数确保主循环安全结束
