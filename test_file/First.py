import sys
from PyQt5.QtWidgets import QApplication,QWidget    #应用程序、应用窗口


# 创建应用程序对象
app = QApplication(sys.argv)
# 创建应用窗口对象
w = QWidget()

# 设置窗口尺寸[宽*高]
w.resize(800,200)
# 移动窗口
w.move(300,300)
# 设置窗口标题
w.setWindowTitle('第一个基于PyQt5的桌面应用:')
# 显示窗口
w.show()

# 进入程序的主循环，并通过exit函数确保主循环安全结束
sys.exit(app.exec_())

#

