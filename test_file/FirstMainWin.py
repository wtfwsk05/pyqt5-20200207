import sys
from PyQt5.QtWidgets import QApplication,QMainWindow    # 应用程序,主窗口
from PyQt5.QtGui import QIcon                           # 图标
class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin, self).__init__(parent)
        # 设置窗口标题
        self.setWindowTitle('第一个主窗口应用')
        # 设置窗口大小
        self.resize(400,300)
        # 创建状态栏
        self.status = self.statusBar()
        # 设置状态栏信息
        self.status.showMessage('只显示5秒',5000)
if __name__ == '__main__':
    # 创建应用程序    sys.argv获取程序外命令行参数
    app = QApplication(sys.argv)
    # 设置应用程序的图标
    app.setWindowIcon(QIcon(r'E:\PythonProject\mypyqt5\images\doc.ico'))
    main = FirstMainWin()       # 实例化所创建的类
    main.show()                 # 显示窗体
    sys.exit(app.exec_())       # 进行程序主循环并通过exit函数确保主循环结束