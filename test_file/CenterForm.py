import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon
class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()
        # 窗口标题
        self.setWindowTitle('居中窗口')
        # 窗口大小
        self.resize(800,300)
        # 创建状态栏并设置相关信息
        self.status = self.statusBar()
        self.status.showMessage('信息显示5秒',5000)
    def center(self):
        '''居中'''
        screen = QDesktopWidget().screenGeometry()  # 获取屏幕的坐标系
        win = self.geometry()                       # 获取窗口坐标系统
        newleft = (screen.width()-win.width())/2    # 宽度计算
        newtop = (screen.height()-win.height())/2   # 高度计算
        # 设置窗口位置
        self.move(newleft,newtop)
if __name__ == '__main__':
    app = QApplication(sys.argv)    # 应用程序,接收程序外的命令参数
    # 设置应用程序的图标
    app.setWindowIcon(QIcon('E:\PythonProject\mypyqt5\images\Cloudy_72px.png'))
    win = CenterForm()  		# 创建【居中窗口】
    win.show()          		# 窗口显示
    sys.exit(app.exec_())   		# 进入主循环并确保退出