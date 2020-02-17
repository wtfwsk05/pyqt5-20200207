import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QMainWindow,QPushButton
from PyQt5.QtWidgets import QHBoxLayout

def onClick_btn():
    print('输出[工作区]的坐标信息')
    print('w=',widget.width(),'  h=',widget.height())   # 300工作区宽度  240工作区高度
    print('x=',widget.x(),'  y=',widget.y())            # 250窗口横坐标  200窗口纵坐标
    print('输出[窗口]的坐标信息')
    print('w=',widget.geometry().width(),'  h=',widget.geometry().height()) # 300工作区宽度  240工作区高度
    print('x=',widget.geometry().x(),'  y=',widget.geometry().y())          # 266窗口横坐标  272窗口纵坐标
    print('输出[框架]的坐标信息')
    print('w=',widget.frameGeometry().width(),'  h=',widget.frameGeometry().height())
    print('x=',widget.frameGeometry().x(),'  y=',widget.frameGeometry().y())

app = QApplication(sys.argv)    # 应用程序(程序外命令行参数)
widget = QWidget()              # 窗口部件
widget.resize(600,240)          # 工作区 窗口大小(宽,高)
widget.move(250,200)            # 窗口位置(x,y)
widget.setWindowTitle('屏幕坐标系')	# 窗口标题
btn = QPushButton(widget)       # 窗口中 创建 按钮
btn.setText('按钮')             # 设置按钮文本
btn.move(24,52)                 # 按钮位置
btn.clicked.connect(onClick_btn)# 给按钮指定事件及事件相对应的方法
widget.show()
sys.exit(app.exec_())