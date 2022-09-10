# # import time

# # # from numpy import greater_equal
# # import datetime
# # # datetime.datetime.strftime
# # t1=datetime.datetime.strptime("23:59","%H:%M")
# # t2=datetime.datetime.strptime("08:00","%H:%M")
# # # print(t2)
# # d=t2-t1
# # print(d.days)
# # print(d.seconds)
# # tt=3600
# # ct=33
# # pc=0
# # tct=ct
# # print(int(tt/ct))
# # import datetime
# # s1 = '23:00abc'
# # s2 = '04:00abc' # for example
# # FMT = '%H:%Mabc'
# # tdelta = datetime.datetime.strptime(s2, FMT) - datetime.datetime.strptime(s1, FMT)
# # print(tdelta.seconds)
# # # if tdelta.days < 0:
# # #     tdelta = datetime.timedelta(
# # #         days=0,
# # #         seconds=tdelta.seconds,
# # #         microseconds=tdelta.microseconds
# # #     )
# # #     print("Asdf")
# # print(tdelta.seconds)
# # while tct<=tt:
# #     tct=tct+ct
# #     # print(tct)
# #     pc=pc+1
#     # print(pc)
#     # print
# # print(pc,tct)
# # l=[]
# # s=''
# # for i in range(7,128,4):
# #     s=s+str(i)+','
# # print(s)
# # filedic={"1013":"23:30-00:30_PQ"}
# # i=1013
# # common_letters=11
# # spl=filedic[str(i)][:common_letters].split('-')
# # a=spl[0]
# # b=spl[1]
# # import datetime
# # # s1 = '23:00abc'
# # # s2 = '04:00abc' # for example
# # FMT = '%H:%M'
# # tdelta = datetime.datetime.strptime(b, FMT) - datetime.datetime.strptime(a, FMT)
# # print(tdelta.seconds)
# # print(40/60)
# # print(3600//33)
# # a=[]
# # a.append([2,3])
# # a.append([4,5,6])
# # print(a)
# # table_list=[["SPR_BB",[0,20],60,[0,30],30],["SPR_3PGA1",[0,20],60,[0,30],30],["SPR_3PGA2",[0,20],60,[0,30],30]]
# # send_flag=any([s_list[i][0] for s_list in table_list[1:] for i in range(1,len(s_list),2)])
# # print(send_flag)
# # a=9
# # b=0
# # print(a/b)
# # import datetime,time
# # from itertools import cycle
# # def get_shift(ct):
# #     startA=datetime.time(A[0],A[1],A[2])
# #     startB=datetime.time(B[0],B[1],B[2])
# #     startC=datetime.time(C[0],C[1],C[2])
# #     if startA<=ct<startB:
# #         return 'A'
# #     if startB<=ct<startC:
# #         return 'B'
# #     else:
# #         return 'C'
# # time_format="%H:%M:%S"

# # A=[6,0,0]
# # B=[14,30,0]
# # C=[22,30,00]
# # cycle_time=10
# # def ppq_update():
# #     while True:
# #         time_now=datetime.datetime.now()
        
# #         # current_time=datetime.time(time_now.hour,time_now.minute,time_now.second)
# #         current_time=datetime.time(6,0,0)
# #         s=get_shift(current_time)
# #         current_time=f"{time_now.hour}:{time_now.minute}:{time_now.second}"
# #         if s=="A":
# #             shift_start_time=f"{A[0]}:{A[1]}:{A[2]}"
# #         elif s=="B":
# #             shift_start_time=f"{B[0]}:{B[1]}:{B[2]}"
# #         else:
# #             shift_start_time=f"{C[0]}:{C[1]}:{C[2]}"
# #         # currenn
# #         tdelta_diff = datetime.datetime.strptime(current_time, time_format) - datetime.datetime.strptime(shift_start_time, time_format)

# #         print(s,int(tdelta_diff.seconds/cycle_time))
# #         time.sleep(1)
# # ppq_update()
# # import time
# # line_no_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # # slice_by=4
# # # sliced_lists=[]
# # # sliced_lists=[line_no_list[i:i+slice_by] for i in range(0,len(line_no_list),slice_by)]
# # # print(sliced_lists)
# # for i in line_no_list:
# #     line_no_list[i]=i
# #     print(line_no_list)
# #     time.sleep(1)
# # a=[1,2,3,4,5,19]
# # b=[6,7,8,9,10,19]
# # c=[11,12,13,14,15,19]
# # # for i,j,k in zip(a,b,c):
# # #     print(i,j,k)
# # for i in range(1,10):
# #     print(i)
# # a=1/12
# # if int(a)==a:
# #     a=int(a)
# # print(a)
# # print(round(a,1))
# # 101===SPR_BB,16,180,900,2100,2700,1000,#008080
# # 102===SPR_3PGA1,33,180,900,2100,2700,1000,#008080
# # 103===SPR_3PGA2,30,180,900,2100,2700,1000,#008080
# # 104===MSIL_BB,20,180,900,2100,2700,1000,#800080
# # 105===MSIL_3PGA,28,180,900,2100,2700,1000,#800080
# # 106===NEW_FS1_BB,18,180,900,2100,2700,1000,#40E0D0
# # 107===NEW_FS1_3PGA,31,180,900,2100,2700,1000,#40E0D0
# # 108===ABL_HEAD1,10,180,900,2100,2700,1000,#FF00FF
# # 109===ABL_HEAD2,10,180,900,2100,2700,1000,#FF00FF
# # 110===ABL_FINAL1,10,180,900,2100,2700,1000,#FF00FF
# # 111===ABL_FINAL2,12,180,900,2100,2700,1000,#FF00FF
# # 112===ABL_FINAL3,12,180,900,2100,2700,1000,#FF00FF
# # 113===OLD_FS1_BB,20,180,900,2100,2700,1000,#FFBF00
# # 114===OLD_FS1_3PGA1,33,180,900,2100,2700,1000,#FFBF00
# # 115===OLD_FS1_3PGA2,33,180,900,2100,2700,1000,#FFBF00
# # 116===OLD_FS1_3PGA3,33,180,900,2100,2700,1000,#FFBF00
# # 117===OBL,12,180,900,2100,2700,1000,#FFBF00
# # 118===NBL,12,180,900,2100,2700,1000,#FFBF00
# # 119===HONDA_3PGA,30,180,900,2100,2700,1000,#FFBF00
# # q=41
# # ct=30
# # print(round((3600-(q*ct))/60))
# # import datetime, time
 
# # secs = 60*60*24*365
# # def ge():
# #     sec = int( input ('Enter the number of seconds:'.strip()))
# #     if sec <= 60:
# #         minutes = sec // 60
# #         print('The number of minutes is {0:.2f}'.format(minutes)) 
# #     if sec (<= 3600):
# #         hours = sec // 3600
# #         print('The number of minutes is {0:.2f}'.format(hours))
# #     if sec <= 86400:
# #         days = sec // 86400
# #         print('The number of minutes is {0:.2f}'.format(days))
# #     return
 
# # # result = datetime.timedelta(seconds = secs)
 
# # print("\n", result, "\n")
# # import sys# importing various libraries
# # import sys
# # from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout,QLabel
# # from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# # from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# import matplotlib.pyplot as plt
# import random

# # # main window
# # # which inherits QDialog
# # class Window(QDialog):
	
# # 	# constructor
# # 	def __init__(self, parent=None):
# # 		super(Window, self).__init__(parent)

# # 		# a figure instance to plot on
# # 		self.figure = plt.figure()

# # 		# this is the Canvas Widget that
# # 		# displays the 'figure'it takes the
# # 		# 'figure' instance as a parameter to __init__
# # 		# self.canvas = FigureCanvas(self.figure)

# # 		# this is the Navigation widget
# # 		# it takes the Canvas widget and a parent
# # 		# self.toolbar = NavigationToolbar(self.canvas, self)
# #         self.label=QLabel()

# # 		# Just some button connected to 'plot' method
# # 		self.button = QPushButton('Plot')
		
# # 		# adding action to the button
# # 		self.button.clicked.connect(self.plot)

# # 		# creating a Vertical Box layout
# # 		layout = QVBoxLayout()
		
# # 		# adding tool bar to the layout
# # 		layout.addWidget(self.toolbar)
		
# # 		# adding canvas to the layout
# # 		layout.addWidget(self.canvas)
		
# # 		# adding push button to the layout
# # 		layout.addWidget(self.button)
		
# # 		# setting layout to the main window
# # 		self.setLayout(layout)

# # 	# action called by the push button
# # 	def plot(self):
		
# # 		# random data
# # 		data = [random.random() for i in range(10)]

# # 		# clearing old figure
# # 		self.figure.clear()

# # 		# create an axis
# # 		ax = self.figure.add_subplot(111)

# # 		# plot data
# # 		ax.plot(data, '*-')

# # 		# refresh canvas
# # 		self.canvas.draw()

# # # driver code
# # if __name__ == '__main__':
	
# # 	# creating apyqt5 application
# # 	app = QApplication(sys.argv)

# # 	# creating a window object
# # 	main = Window()
	
# # 	# showing the window
# # 	main.show()

# # 	# loop
# # 	sys.exit(app.exec_())
# # import sys
# # from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# # from PyQt5.QtGui import QIcon, QPixmap

# # class App(QWidget):

# #     def __init__(self):
# #         super().__init__()
# #         self.title = 'PyQt5 image - pythonspot.com'
# #         self.left = 10
# #         self.top = 10
# #         self.width = 640
# #         self.height = 480
# #         self.initUI()
    
# #     def initUI(self):
# #         self.setWindowTitle(self.title)
# #         self.setGeometry(self.left, self.top, self.width, self.height)
    
# #         # Create widget
# #         label = QLabel(self)
        
# #         self.figure=plt.figure()
# #         ax = self.figure.add_subplot(111)
# #         data = [random.random() for i in range(10)]
# #         ax.plot(data, '*-')
# #         # self.canvas.draw()
# #         # plt.show()
# #         pixmap=QPixmap(self.figure)
# #         # pixmap = QPixmap('image.jpg')
# #         label.setPixmap(pixmap)
# #         self.resize(pixmap.width(),pixmap.height())
        
# #         self.show()

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = App()
# #     sys.exit(app.exec_())
# # from PyQt5.QtWidgets import*
# # from PyQt5.uic import loadUi

# # from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
# # from matplotlib.backends.backend_qt5agg import FigureCanvas

# # import numpy as np
# # import random
     
# # class MatplotlibWidget(QMainWindow):
    
# #     def __init__(self):
        
# #         QMainWindow.__init__(self)

# #         loadUi("test.ui",self)

# #         self.setWindowTitle("PyQt5 & Matplotlib Example GUI")

# #         self.next_button.clicked.connect(self.update_graph)

# #         # self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))


# #     def update_graph(self):

# #         fs = 500
# #         f = random.randint(1, 100)
# #         ts = 1/fs
# #         length_of_signal = 100
# #         t = np.linspace(0,1,length_of_signal)
        
# #         cosinus_signal = np.cos(2*np.pi*f*t)
# #         sinus_signal = np.sin(2*np.pi*f*t)
# #         self.canvas = FigureCanvas(Figure())
# #         self.label.canvas.axes.clear()
# #         self.MplWidget.canvas.axes.plot(t, cosinus_signal)
# #         self.MplWidget.canvas.axes.plot(t, sinus_signal)
# #         self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
# #         self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
# #         self.MplWidget.canvas.draw()
        

# # app = QApplication([])
# # window = MatplotlibWidget()
# # window.show()
# # app.exec_()
# # Import necessary modules

# # import sys

# # from PyQt5 import QtCore, QtWidgets

# # from PyQt5.QtWidgets import QMainWindow, QCheckBox, QLabel, QVBoxLayout, QDesktopWidget

# # # Define class for creating the form with single checkbox

# # class SingleCheckbox(QMainWindow):

# #     def __init__(self):

# #         super().__init__()


# #         # Create the label text for the user

# #         lb = QLabel("Do you like programming?", self)

# #         lb.setGeometry(20, 20, 200, 20)

# #         lb.move(20, 20)


# #         # Create a checkbox with the label

# #         cb = QCheckBox('Yes', self)

# #         cb.stateChanged.connect(self.Check_Answer)

# #         cb.move(20, 50)


# #         # Set the vertical Qt Layout

# #         vbox = QVBoxLayout()

# #         vbox.addWidget(lb)

# #         vbox.addWidget(cb)


# #         # Set the window title and size

# #         self.setWindowTitle('Form with Single Checkbox')

# #         self.setGeometry(60, 60, 300, 100)


# #         # Display the window in the center of the screen

# #         win = self.frameGeometry()

# #         pos = QDesktopWidget().availableGeometry().center()

# #         win.moveCenter(pos)

# #         self.move(win.topLeft())

# #         self.show()


# #     # Define function to check the user's input

# #     def Check_Answer(self, state):


# #         if state == QtCore.Qt.Checked:

# #             print("Wow! You like programming.")

# #         else:

# #             print("Oh no!, You don't like programming.")

# # # Create app object and execute the app

# # app = QtWidgets.QApplication(sys.argv)

# # form = SingleCheckbox()

# # app.exec()
# import time

# # dic={"ln":{"opq":0,"oit":0,"npq":0,"nit":0,"ppq":0,"ogit":0,"ini_t":round(time.time()),"ooc":0,"hrf":False,"srf":False,"mac_s":False,"ef":False,"l1f":False,"l2f":False,"l3f":False, "conn_col":"red","hour_list":[]}}
# # dic["ln"]["hour_list"].insert(6,7)
# # print(dic["ln"]["hour_list"])
# # print(dic["ln"]["hour_list"][6])
# li=[1,2,3,8]
# # li.max
# # ind=4
# # if ind !=len(li)-1:
# #     while len(li)<=ind:
# #         li.append(0)
# # print(li)
# # print(max(li))
# # print(min(li))
# # dic={1:"23",2:"302",3:"20"}
# # a=4
# # if a not in dic:
# #     print(a)
# # pl_list=[4,5,67,7]
# # ql_list=list(pl_list)
# # ql_list.append(0)
# # print(pl_list,ql_list)
# # rl_list=[23,4,5,5]
# # sl_list=[24,5,54,5]
# # for line_pl,ql,rl,sl in zip(enumerate(pl_list),ql_list,rl_list,sl_list):
# #     print(line_pl[0],line_pl[1],ql,rl,sl)

# # import snap7,openpyxl

# # def call():
# #     while True:
# #         pass
# #         # print("jkl")s
# #         # break
# #     # time.sleep(2)
# # # call()
# # wb=openpyxl.load_workbook(r'D:\MyExcel.xlsx')
# # ws = wb.active
# # mr=ws.max_row
# # ws["A{}".format(mr+1)]=123
# # wb.save('MyExcel.xlsx')
# # def get_text_by_sec(sec):
# #     if sec <= 60:
# #         text = str(round(sec ,1))+'S'
# #         # print('The number of minutes is {0:.2f}'.format(minutes)) 
# #     elif sec <= 3600:
# #         text = str(round(sec / 60,1))+'M'
# #         # print('The number of minutes is {0:.2f}'.format(hours))
# #     elif sec <= 86400:
# #         text = str(round(sec / 3600,1))+'H'
# #         # print('The number of minutes is {0:.2f}'.format(days))
# #     else:
# #         text = str(round(sec / 86400,1))+'D'
# #     return text
# # # while True:
# # #     sec = int( input ('Enter the number of seconds:'.strip()))
# # #     print(get_text_by_sec(sec))
# # print(time.time())
# # importing various libraries
# # import sys
# # from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
# # from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# # from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# # import matplotlib.pyplot as plt
# # import random
# # from PyQt5.uic import loadUi
# # import pandas as pd
# # from PyQt5 import QtWidgets


# # # main window
# # # which inherits QDialog
# # class firstdialog(QDialog):
# #     def __init__(self):
# #         super(firstdialog,self).__init__()
# #         self.ui=loadUi("page_1.ui",self)
# # 		# a figure instance to plot on
# #         # self.figure = plt.figure("figure 1")
# #         # self.figure2 = plt.figure("figure 2")

# # 		# this is the Canvas Widget that
# # 		# displays the 'figure'it takes the
# # 		# 'figure' instance as a parameter to __init__
        

# # 		# this is the Navigation widget
# # 		# it takes the Canvas widget and a parent
# #         # self.toolbar = NavigationToolbar(self.canvas, self)

# # 		# Just some button connected to 'plot' method
# #         self.button = QPushButton('Plot')
		
# # 		# adding action to the button
# #         self.next_button.clicked.connect(self.plot)
# #         self.count1=0
# #         self.count2=0
# #         self.layout_list=["layout_1","layout_2","layout_3","layout_4"]
# #         for index_i,i in enumerate(self.layout_list):
# #             self.layout_list[index_i]=self.ui.findChild(QtWidgets.QVBoxLayout,i)
# #         self.figure_and_canvas_list=[]
# #         for index_li,layout_i in enumerate(self.layout_list):
# #             self.figure = plt.figure(str(index_li))
# #             self.canvas = FigureCanvas(self.figure)
# #             self.figure_and_canvas_list.append([self.figure ,self.canvas])
# #             layout_i.addWidget(self.canvas)
# #         self.count=0
# #         # self.label_h1.setText("asd\nskdf")
# # 	# action called by the push button
# #     def plot(self):
# #         # self.figure = plt.figure()
# #         print(self.figure_and_canvas_list)
# #         for index_i,i in enumerate(self.figure_and_canvas_list):
# #             i[0].clear()
# #             plt.figure(str(index_i))
# #             self.count=self.count+1
# #             a=[1,2,3,4,5,6,11]
# #             b=[100,200,150,180,170,self.count,313]
# #             cl=['red','yellow','green','red','yellow','green']
# #             plots=plt.bar(a,b,align='center',color=cl)
# #             ii=300
# #             plt.plot([1,2,3,4,5,6,7,8,9],[300,300,300,300,300,300,300,300,150])
# #             plt.text(5,300,f"Capacity={ii}Nos/h",ha="center")
# #             for bar in plots:
# #                     # print(bar.get_height())
# #                     height=bar.get_height()
# #                     plt.annotate('{}'.format(height),
# #                     xy=(bar.get_x()+bar.get_width()/2,height),
# #                     xytext=(0,3),
# #                     textcoords='offset points',ha='center',va='center')
# #             # plt.grid(False)
# #             plt.axis("off")
# #             plt.xlim((0,10))
# #             # plt.legend()
# #             i[0].subplots_adjust(left=0, right=1,
# #                         top=1, bottom=0,
# #                         hspace=0, wspace=0)
# #             i[1].draw()

# #         # self.figure = plt.figure("figure 1")
# #         # # if self.count1<1:
# #         # #     self.canvas = FigureCanvas(self.figure)

# #         # #     self.layout_1.addWidget(self.canvas)
# #         # self.count1=self.count1+1

# # 		# # random data
# #         # # data = [random.random() for i in range(9)]
# #         # # print(data)
# # 		# # clearing old figure
# #         # self.figure.clear()
# #         # a=[1,2,3,4,5,6,11]
# #         # b=[100,200,150,180,170,self.count1,313]
# #         # c=[100,199,150,180,170,self.count2,313]
# #         # cl=['red','yellow','green','red','yellow','green']
# #         # plots=plt.bar(a,b,align='center',color=cl)
# #         # i=300
# #         # plt.plot([1,2,3,4,5,6,7,8,9],[300,300,300,300,300,300,300,300,150])
# #         # plt.text(5,300,f"Capacity={i}Nos/h",ha="center")
# #         # for bar in plots:
# #         #         # print(bar.get_height())
# #         #         height=bar.get_height()
# #         #         plt.annotate('{}'.format(height),
# #         #         xy=(bar.get_x()+bar.get_width()/2,height),
# #         #         xytext=(0,3),
# #         #         textcoords='offset points',ha='center',va='center')
# #         # # plt.grid(False)
# #         # plt.axis("off")
# #         # plt.xlim((0,10))
# #         # # plt.legend()
# #         # self.figure.subplots_adjust(left=0, right=1,
# #         #             top=1, bottom=0,
# #         #             hspace=0, wspace=0)
# #         # self.canvas.draw()
# #         # self.figure2.clear()
# #         # if self.count2<1:
# #         #     self.canvas2 = FigureCanvas(self.figure2)
# #         #     self.layout_2.addWidget(self.canvas2)
# #         # self.count2=self.count2+1
# #         # plt.xlim((0,10))
# #         # plots=plt.bar(a,c,color=cl)
# #         # plt.plot([1,2,3,4,5,6,7,8,9],[300,300,300,300,300,300,300,300,150])
# #         # plt.text(5,300,f"Capacity={i}Nos/h",ha="center")
# #         # for bar in plots:
# #         #         # print(bar.get_height())
# #         #         height=bar.get_height()
# #         #         plt.annotate('{}'.format(height),
# #         #         xy=(bar.get_x()+bar.get_width()/2,height),
# #         #         xytext=(0,3),
# #         #         textcoords='offset points',ha='center',va='center')
# #         # # plt.grid(False)
# #         # plt.axis("off")
# #         # # plt.legend()
# #         # self.figure2.subplots_adjust(left=0, right=1,
# #         #             top=1, bottom=0,
# #         #             hspace=0, wspace=0)
# #         # self.canvas2.draw()
# #         # self.canvas.hide()

# # # driver code
# # # if __name__ == '__main__':
	
# # # 	# creating apyqt5 application
# # # 	app = QApplication(sys.argv)

# # # 	# creating a window object
# # # 	main = firstdialog()
	
# # # 	# showing the window
# # # 	main.show()

# # # 	# loop
# # # 	sys.exit(app.exec_())
# # # from smtplib import SMTP
# # # from email.mime.text import MIMEText
# # # from email.mime.multipart import MIMEMultipart

# # # message = MIMEMultipart()
# # # message['Subject'] = 'Production report'
# # # message['From'] = 'p.thirunavukkarasu@ranegroup.com'
# # # message['To'] = 'p.thirunavukkarasu@ranegroup.com'
# # # body_content = "text"
# # # message.attach(MIMEText(body_content, "html"))
# # # msg_body = message.as_string()
# # # count=0
# # # while True:
# # #     try:
# # #         server = SMTP('smtp.gmail.com', 587)
# # #         server.starttls()
# # #         server.login(message['From'], app_password)
# # #         server.send_message(message)
# # #         server.quit()
# # #         print("SM: Summary mail sent...")
# # #     except Exception as e:
# # #         print("SM: Unable to sent mail, ",e)
# # #         time.sleep(3)
# # #         count=count+1
# # #         if count<3:
# # #             continue
# # #         else:
# # #             break
# # #     break
# # data_dict={1:"OP10",2:"OP20",3:"OP30"}
# # while True:
# #     inp=input("enter no :")
# #     print(data_dict[int(inp)])





# import os,datetime
# from smtplib import SMTP
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from openpyxl import Workbook,load_workbook

# setting_file=open('server_settings.txt','r')
# print("MT: I am a Server")
# filedic={}
# for line in setting_file:
#     file_data=line.strip().split('===')
#     a=file_data[0]
#     b=file_data[1]
#     filedic[a]=b
# setting_file.close()
# ipaddress_of_system=filedic.pop('ipaddress_of_system')
# port_to_listen=int(filedic.pop('port_to_listen'))
# shiftA_start=filedic.pop('shiftA_start_time')
# shiftB_start=filedic.pop('shiftB_start_time')
# shiftC_start=filedic.pop('shiftC_start_time')
# filename_of_i_excel=filedic.pop('filename_of_idle_time_excel_sheet')
# filename_of_h_excel=filedic.pop('filename_of_hourly_excel_sheet')
# hourly_list=filedic.pop('hourly_intimate').split(",")
# columns_before_pq_and_it_in_excel=int(filedic.pop('columns_before_pq_and_it_in_excel'))
# mfg_webhook_url1=filedic.pop('mfg_webhook_url_level1')
# mfg_webhook_url2=filedic.pop('mfg_webhook_url_level2')
# mfg_webhook_url3=filedic.pop('mfg_webhook_url_level3')
# level1_name=filedic.pop('level1_name')
# level2_name=filedic.pop('level2_name')
# level3_name=filedic.pop('level3_name')
# line_no_list=filedic.pop('LINE_NUMBERS').split(",")
# hourly_sheet_name=filedic.pop('hourly_sheet_name')
# header_row_h=int(filedic.pop('header_row_hourly'))
# total_columns=int(filedic.pop('total_columns'))
# last_hour_column_of_day=int(filedic.pop('last_hour_column_of_day'))
# mfg_space_url=filedic.pop('mfg_space_url')
# scheduler_delay=int(filedic.pop("scheduler_delay_in_milliseconds"))/1000
# delay_for_update_unique_no_and_ppq=int(filedic.pop("delay_for_unique_no_creation_and_planned_prodution_quantity_update_in_milliseconds"))/1000
# error_wait=int(filedic.pop("error_wait_in_milliseconds"))/1000
# mail_trig_delay=int(filedic.pop("mail_trigger_delay_after_next_shift_start_in_seconds"))
# common_time_letters=int(filedic.pop("common_time_letters_count_from_begining_in_pq_and_it_columns"))
# column_no_start=int(filedic.pop("column_no_start_from"))
# json_file_name=filedic.pop('json_file_name_for_store_values')
# dict_backup_time=int(filedic.pop('dict_backup_time_in_seconds'))
# idle_time_calc_delay=int(filedic.pop("idle_time_calc_delay_in_seconds"))
# prior_time=int(filedic.pop('prior_time_for_hourly_trigger_in_seconds'))
# end_timing_pos=filedic.pop('end_timing_index_positions')
# mail_user_name=filedic.pop("mail_user_name")
# app_password=filedic.pop('app_password')
# shiftA_table_color=filedic.pop('shiftA_summary_table_color')
# shiftB_table_color=filedic.pop('shiftB_summary_table_color')
# shiftC_table_color=filedic.pop('shiftC_summary_table_color')
# low_prod_color=filedic.pop('low_production_indication_color')
# medium_prod_color=filedic.pop('medium_production_indication_color')
# high_prod_color=filedic.pop('high_production_indication_color')
# time_split_by=filedic.pop('from_and_to_time_split_by')
# time_format=filedic.pop('time_format_in_column_names')
# not_send_mail_when_all_pq_is_0=int(filedic.pop("not_send_mail_when_all_production_quantity_is_zero"))
# not_send_hourly_chat_message_when_all_pq_is_0=int(filedic.pop("not_send_hourly_chat_message_when_all_production_quantity_is_zero"))
# To_mail_pos_list=list(map(int,filedic.pop('To_mails_pos_in_mail_list').strip().split(",")))
# Cc_mail_pos_list=list(map(int,filedic.pop('Cc_mails_pos_in_mail_list').strip().split(",")))
# min_percent_of_medium_prod=int(filedic.pop("minimum_percentage_of_medium_production"))
# max_percent_of_medium_prod=int(filedic.pop("maximum_percentage_of_medium_production"))
# print("MT: Settings file read")
# total_file= open("total.txt", "r")
# summary_a_file= open("summary_A.txt", "r")
# summary_b_file= open("summary_B.txt", "r")
# summary_c_file= open("summary_C.txt", "r")

# total_dic={}
# list_of_mails= []
# summary_a_list= []
# summary_b_list= []
# summary_c_list= []
# for line in total_file:
#     file_data=line.strip().split('===')
#     a=int(file_data[0])
#     b=list(map(int,file_data[1].strip().split(",")))
#     total_dic[a]=b
# for line in summary_a_file:
#   summary_a_list.append(line.strip())
# for line in summary_b_file:
#   summary_b_list.append(line.strip())
# for line in summary_c_file:
#   summary_c_list.append(line.strip())

# total_file.close()

# To_list_of_mails=[]
# Cc_list_of_mails=[]
# for i in To_mail_pos_list:
#     To_list_of_mails.append("p.thirunavukkarasu@ranegroup.com")
# for i in Cc_mail_pos_list:
#     Cc_list_of_mails.append("osdple@gmail.com")

# summary_a_file.close()
# summary_b_file.close()
# summary_c_file.close()
# summary_dic={"A":summary_a_list,"B":summary_b_list,"C":summary_c_list}
# print("MT: Total, Mail, Summary_A, Summary_B, Summary_C file read")

# def send_mail(date,day,shift,table_list,non_prod_sub_list):
#         head_list=table_list[0]
#         list_len=len(head_list)
#         if shift=="A":
#             table_head_color=shiftA_table_color
#         elif shift=="B":
#             table_head_color=shiftB_table_color
#         else:
#             table_head_color=shiftC_table_color
#         html_str=f'''<!DOCTYPE html>
#         <html><body>
#         <table style="font-family:  Arial, Helvetica,sans-serif;
#         border: 1px solid #ddd;
#         border-collapse:collapse;
#         width: 100%;
#         margin: 25px 0;
#         font-size: 1.0em;
#         min-width: 400px;
#         border-radius: 10px 10px 0 0;
#         overflow: hidden;
#         box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);">
#         <tr>
#             <th style="padding:12px;text-align: center;background-color: {table_head_color};color: white;border: 1px solid #ddd;"colspan="{list_len}">DATE : {date} [{day}]   SHIFT: {shift}</th>
#         </tr>'''
#         html_str=html_str+'<tr>'
#         for i in range(list_len):
#             if 0<i<=(list_len-3):
#                 if i%2: 
#                     html_str=html_str+f'<th style="padding:12px;text-align: center;background-color: {table_head_color};color: white;border: 1px solid #ddd;white-space: nowrap;"colspan="2">{head_list[i][:common_time_letters]}</th>'
#                 else:
#                     pass
#             elif i>=(list_len-3):
#                 html_str=html_str+f'<th style="padding:12px;text-align: center;background-color: {table_head_color};color: white;border: 1px solid #ddd;white-space: nowrap;"colspan="2">{head_list[i][:5]}</th>'
#                 break
#             elif i==0:
#                 html_str=html_str+f'<th style="padding:12px;text-align: center;background-color: {table_head_color};color: white;border: 1px solid #ddd;white-space: nowrap;"rowspan="2">{head_list[i]}</th>'
#         html_str=html_str+'</tr>'
#         html_str=html_str+'<tr>'
#         for i in range(list_len):
#             if i>0:
#                 if i%2:
#                     html_str=html_str+f'<th style="padding:12px;text-align: center;background-color: {table_head_color};color: white;border: 1px solid #ddd;white-space: nowrap;">{head_list[i][-2:]}</th>'
#                 else:
#                     html_str=html_str+f'<th style="padding:12px;text-align: center;background-color: {table_head_color};color: white;border: 1px solid #ddd;white-space: nowrap;">{head_list[i][-2:]}</th>'

#         html_str=html_str+'</tr>'
#         for index_sub_list,sub_list in enumerate(table_list[1:]):
#             html_str=html_str+'<tr>'
#             if not index_sub_list in non_prod_sub_list: 
#                 for index_i,i in enumerate(sub_list):
#                     if index_i==(list_len-1):
#                         html_str=html_str+f'<td style="border: 1px solid #ddd;padding: 11px;text-align: center;background-color: #e6e6e6;"><b>{i}</b></td>'
#                     elif index_i==(list_len-2):
#                         html_str=html_str+f'<td style="border: 1px solid #ddd;padding: 11px;text-align: center;background-color: {i[1]};"><b>{i[0]}</b></td>'
#                     elif index_i%2:
#                         html_str=html_str+f'<td style="border: 1px solid #ddd;padding: 11px;text-align: center;background-color: {i[1]};">{i[0]}</td>'
#                     else:
#                         html_str=html_str+f'<td style="border: 1px solid #ddd;padding: 11px;text-align: center;background-color: #e6e6e6;">{i}</td>'
#             else:
#                 colo="#7FFFD4"
#                 for index_i,i in enumerate(sub_list):
#                     if index_i==(list_len-1):
#                         html_str=html_str+f'<td style="border: 1px solid #ddd;padding: 11px;text-align: center;background-color: {colo}"><b>{i}</b></td>'
#                     elif index_i==(list_len-2):
#                         html_str=html_str+f'<td style="border: 1px solid #ddd;padding: 11px;text-align: center;background-color: {colo};"><b>{i[0]}</b></td>'
#                     elif index_i%2:
#                         html_str=html_str+f'<td style="border: 1px solid #ddd;padding: 11px;text-align: center;background-color: {colo};">{i[0]}</td>'
#                     else:
#                         html_str=html_str+f'<td style="border: 1px solid #ddd;padding: 11px;text-align: center;background-color: {colo}">{i}</td>'
#             html_str=html_str+'</tr>'
#         html_str=html_str+f'''<tr>
#                                     <th style="text-align: left;padding-left: 10px;background-color: {table_head_color};color: white;border: 1px solid #ddd;"colspan="{list_len}"> 
#                                         <b>Note:</b> <br/> 
#                                         &nbsp;&nbsp;&nbsp; PQ - Production Quantity (in Numbers) <br/>
#                                         &nbsp;&nbsp;&nbsp; IT - Idle Time (in Mins) <br/>
#                                         &nbsp;&nbsp;&nbsp; PQ Color with respect to line prodcution capacity - Green : Above {max_percent_of_medium_prod}%,
#                                                                                                              Yellow : {min_percent_of_medium_prod}% ~ {max_percent_of_medium_prod}%,
#                                                                                                              Red : Below {min_percent_of_medium_prod}%. </th>
#                                 </tr>'''
#         html_str=html_str+'</table>'
#         # html_str=html_str+'<p>* PQ : Production Quantity in Numbers</p><p>* IT: Idle time in Minutes</p>'
#         html_str=html_str+'</body></html>'
#         body=html_str
#         message = MIMEMultipart()
#         message['Subject'] = 'Production report'
#         message['From'] = mail_user_name
#         message['To'] = ', '.join( To_list_of_mails )
#         message['Cc'] = ', '.join( Cc_list_of_mails )
#         body_content = body
#         message.attach(MIMEText(body_content, "html"))
#         msg_body = message.as_string()
#         count=0
#         while True:
#             try:
#                 server = SMTP('smtp.gmail.com', 587)
#                 server.starttls()
#                 server.login(message['From'], app_password)
#                 server.send_message(message)
#                 server.quit()
#                 print("SM: Summary mail sent...")
#             except Exception as e:
#                 print("SM: Unable to sent mail, ",e)
#                 time.sleep(3)
#                 count=count+1
#                 if count<3:
#                     continue
#                 else:
#                     break
#             break

# table_list=[]
# required_row_list=[]
# required_column_list=[]
# shift="A"
# no_data=True
# time_now=datetime.datetime.now()
# if shift=="C":
#         dp=1
# else:
#         dp=0
# time_now=time_now-datetime.timedelta(days=dp)
# date_today=time_now.strftime("%d-%m-%Y")
# day=time_now.strftime("%a").upper()
# summary_list=summary_dic[shift]
# table_list.append(summary_list)
# if os.path.isfile(filename_of_h_excel):
#     wb=load_workbook(filename_of_h_excel)
#     ws=wb[hourly_sheet_name]
#     xl_headers=[]
#     for i in ws[header_row_h]:
#             xl_headers.append(i.value)
#     mr=ws.max_row
#     for i in range(1,mr+1):
#         if ws.cell(row=i,column=int(filedic["date_column"])).value==date_today:
#             required_row_list.append(i)
#     for i in summary_list:
#         required_column_list.append(xl_headers.index(i)+1)

#     raw_list=list(ws.rows)
#     for r in required_row_list:
#         no_data=False
#         row_list=[]
#         for index_c,c in enumerate(required_column_list):
#             val=raw_list[r-1][c-1].value
#             if val is None:
#                 val=0
#             if index_c%2:
#                 max_val=raw_list[r-1][c].value
#                 per=(int(val)/int(max_val))*100
#                 if per>max_percent_of_medium_prod:
#                     color=high_prod_color
#                 elif per>=min_percent_of_medium_prod:
#                     color=medium_prod_color
#                 else:
#                     color=low_prod_color
#                 row_list.append([val,color])
#             else:
#                 row_list.append(val)
#         table_list.append(row_list)
#     if no_data:
#         print("TMC: As no data for the shift,  no mail will sent for this shift")
#     else:
#             non_prod_sub_list=[]
#             for index_s_list,s_list in enumerate(table_list[1:]):
#                 temp_list=[]
#                 for i in range(1,len(s_list),2):
#                     temp_list.append(s_list[i][0])
#                 if not any(temp_list):
#                     non_prod_sub_list.append(index_s_list)
#             print(non_prod_sub_list)
#             if not_send_mail_when_all_pq_is_0:
#                 send_flag=any([s_list[i][0] for s_list in table_list[1:] for i in range(1,len(s_list),2)])
#                 if send_flag:
#                     send_mail(date_today,day,shift,table_list,non_prod_sub_list)
#                 else:
#                     print(f"TMC: As all production quantity for this shift is zero, no mail will sent for this shift {date_today} {shift}")
#             else:
#                 send_mail(date_today,day,shift,table_list)
#     wb.close()
# else:
#     print(f"TMC: As no {filename_of_h_excel} found, mail not sent")
# a=b'\x006['
# print(a.decode())
# import socket,time
# soc_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# soc_s.connect(("192.168.250.16",2025))
# while True:
#     soc_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     # soc_s.connect(("192.168.250.16",2025))
#     a=soc_s.recv(1024)
#     soc_s.sendall(b'\x00\x00')
#     print(a)
#     time.sleep(1)
# '''<!DOCTYPE html>
# <html>
# <head>
# <style>
# table {
#   font-family: arial, sans-serif;
#   border-collapse: collapse;
#   width: 100%;
# }

# td, th {
#   border: 1px solid #dddddd;
#   text-align: left;
#   padding: 8px;
# }

# tr:nth-child(even) {
#   background-color: #dddddd;
# }
# </style>
# </head>
# <body>

# <h2>HTML Table</h2>

# <table>
#   <tr>
#     <th><label style="background-color: #ffff00"> Above 80% </label>&nbsp;
#     <label style="background-color: #00ff00"> 60% ~ 80% </label>&nbsp;
#     <label style="background-color: #ff0000"> below 80%  </label>&nbsp; 	<label style="background-color: #00ffff"> No production  </label>&nbsp;</th>
    
#     <th><label style="background-color: #ffff00"> &nbsp;&nbsp;&nbsp; </label>Above 80%
#     <label style="background-color: #00ff00"> &nbsp;&nbsp;&nbsp;</label>60% ~ 80%  <label style="background-color: #ff0000">&nbsp;&nbsp;&nbsp;  </label>below 80% <label style="background-color: #00ffff">&nbsp;&nbsp;&nbsp;  </label>No Prodcuction </th>
#     <th>Country</th>
#   </tr>
#   <tr>
#     <td>Alfreds Futterkiste</td>
#     <td>Maria Anders</td>
#     <td>Germany</td>
#   </tr>
#   <tr>
#     <td>Centro comercial Moctezuma</td>
#     <td>Francisco Chang</td>
#     <td>Mexico</td>
#   </tr>
#   <tr>
#     <td>Ernst Handel</td>
#     <td>Roland Mendel</td>
#     <td>Austria</td>
#   </tr>
#   <tr>
#     <td>Island Trading</td>
#     <td>Helen Bennett</td>
#     <td>UK</td>
#   </tr>
#   <tr>
#     <td>Laughing Bacchus Winecellars</td>
#     <td>Yoshi Tannamuri</td>
#     <td>Canada</td>
#   </tr>
#   <tr>
#     <td>Magazzini Alimentari Riuniti</td>
#     <td>Giovanni Rovelli</td>
#     <td>Italy</td>
#   </tr>
# </table>

# </body>
# </html>'''
# # if (not 1==1) or (not 0==0):
# #   print("matched")
# from queue import Empty
# import threading,time,datetime
# # a="1234.123"
# # print(float(a))
# dt_object=None
# def write_file():
#   while True:
#     f = open("demofile.txt", "w")
#     f.write(str(round(time.time(),2)))
#     # time.st
#     time.sleep(1)


# def read_file():
#   global dt_object
#   while True:
#     f = open("demofile.txt", "r")
#     # print(f)
#     t=f.readlines()
#     if not t==[]:
#       timestamp=float(t.pop(0).split().pop(0))
#       # timestamp = 1545730073
#       dt_object = datetime.datetime.fromtimestamp(timestamp)
#       # # tim=float()
#       # print(type(tim))
#     # print(t)
#     time.sleep(1)
  
# def printasd():
#   global dt_object
#   while True:
#     if not dt_object == None:
#       date_t=dt_object.strftime("%d/%m/%Y")
#       time_t=dt_object.strftime("%H:%M:%S")
#       print(date_t)
#       print(time_t)
#     time.sleep(1)
# dict_bac = threading.Thread(target=write_file,daemon=True)
# dict_bac.start()
# dict_bac = threading.Thread(target=read_file,daemon=True)
# dict_bac.start()
# dict_bac = threading.Thread(target=printasd,daemon=True)
# dict_bac.start()
# while True:
#   time.sleep(1)
import socket,time
from _thread import *
ipaddress_of_system=''
port_to_listen=2020
unique_no_in_bytes=12092
soc=socket.socket()
soc.bind((ipaddress_of_system,port_to_listen))
soc.listen()
conn,addr=soc.accept()
pc_addr=addr[0]
data=conn.recv(1024)
conn.sendall(unique_no_in_bytes)
print(f"ST: Data received {pc_addr, data} ")   
# conn.close()
# soc.close()
while True:
  start_new_thread(socke)
  time.sleep(1)