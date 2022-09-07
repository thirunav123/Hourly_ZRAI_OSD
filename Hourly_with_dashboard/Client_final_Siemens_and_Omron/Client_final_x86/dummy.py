# # # import queue,requests,json
# # # h_chat_queue=queue.Queue()
# # # mfg_space_url="https://chat.googleapis.com/v1/spaces/AAAAiv8Wo8o/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=B3XrZpw5XjaY7LWqAFB6-ap30QuXNl7Haehs5hnIFgE%3D"
# # # h_chat_queue.put([1,"23:00-33:00",983,9000])
# # # plc,h,pq,it=h_chat_queue.get()
# # # line_color="#40E0D0"
# # # line="ASSDD"
# # # date="dd/mm/yyyy"
# # # shift="S"
# # # temp_data = f'<i><b><font color=\"{line_color}">Hourly Intimation!</b></i>\n'\
# # #                         f'<b><font color=\"{line_color}">Production Line &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : {line}</b>\n'\
# # #                         f'<b><font color=\"{line_color}">Date and Shift &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : {date} {shift}</b>\n'\
# # #                         f'<b><font color=\"{line_color}">Hour Time &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : {h}</b>\n'\
# # #                         f'<b><font color=\"{line_color}">Prodution Quantity &nbsp;&nbsp; : {pq}</b>\n'\
# # #                         f'<b><font color=\"{line_color}">Machine Idle in mins : {round(it/60)}</b>\n'
# # # data_dir = {"cards": [{"sections":[{"widgets":[{"textParagraph":{ 'text':f'{temp_data}'}}]}]}]}#,
# # # r = requests.post(mfg_space_url, data=json.dumps(data_dir))
# # # Import Library

# # import matplotlib.pyplot as plt
# # import pandas as pd

# # # Define Data

# # data = {'101': [15, 20, 25, 30, 35],
# #         '102': [25, 30, 28, 19, 40] ,
# #         '103': [15, 20, 25, 30, 35],
# #         '104': [25, 30, 28, 19, 40],
# #         '105': [15, 20, 25, 30, 35],
# #         '106': [25, 30, 28, 19, 40],
# #         '107': [15, 20, 25, 30, 35],
# #         }
# # df = pd.DataFrame(data,columns=['101','102','103','104','105'], index = ['Team-1','Team-2','Team-3','Team-4','Team-5'])

# # # Multiple horizontal bar chart

# # df.plot.barh()

# # # Display

# # plt.show()
# # importing the required libraries
 
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import *
# import sys
 
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
 
#         # set the title
#         self.setWindowTitle("Label")
 
#         # setting  the geometry of window
#         self.setGeometry(0, 0, 650, 400)
 
#         # creating a label widget and setting properties
#         self.label_1 = QLabel("Bottom", self)
#         self.label_1.move(20, 100)
#         self.label_1.resize(60, 60)
#         self.label_1.setStyleSheet("border: 1px solid black;")
 
#         # aligning label to the bottom
#         self.label_1.setAlignment(Qt.AlignBottom)
 
#         # creating a label widget and setting properties
#         self.label_2 = QLabel("Center", self)
#         self.label_2.move(90, 100)
#         self.label_2.resize(60, 60)
#         self.label_2.setStyleSheet("border: 1px solid black;")
 
#         # aligning label to the center
#         self.label_2.setAlignment(Qt.AlignCenter)
 
#         # creating a label widget and setting properties
#         self.label_3 = QLabel("Left", self)
#         self.label_3.move(160, 100)
#         self.label_3.resize(60, 60)
#         self.label_3.setStyleSheet("border: 1px solid black;")
 
#         # aligning label to the left
#         self.label_3.setAlignment(Qt.AlignLeft)
 
#         # creating a label widget and setting properties
#         self.label_4 = QLabel("Right", self)
#         self.label_4.move(230, 100)
#         self.label_4.resize(60, 60)
#         self.label_4.setStyleSheet("border: 1px solid black;")
 
#         # aligning label to the right
#         self.label_4.setAlignment(Qt.AlignRight)
 
#         # creating a label widget and setting properties
#         self.label_5 = QLabel("Top", self)
#         self.label_5.move(300, 100)
#         self.label_5.resize(60, 60)
#         self.label_5.setStyleSheet("border: 1px solid black;")
 
#         # aligning label to the top
#         self.label_5.setAlignment(Qt.AlignTop)
 
#         # creating a label widget and setting properties
#         self.label_6 = QLabel("H center", self)
#         self.label_6.move(370, 100)
#         self.label_6.resize(60, 60)
#         self.label_6.setStyleSheet("border: 1px solid black;")
 
#         # aligning label to the Hcenter
#         self.label_6.setAlignment(Qt.AlignHCenter)
 
#         # creating a label widget and setting properties
#         self.label_7 = QLabel("V center", self)
#         self.label_7.move(440, 100)
#         self.label_7.resize(60, 60)
#         self.label_7.setStyleSheet("border: 1px solid black;")
 
#         # aligning label to the Vcenter
#         self.label_7.setAlignment(Qt.AlignVCenter)
 
#         # show all the widgets
#         self.show()
 
 
# # create pyqt5 app
# App = QApplication(sys.argv)
 
# # create the instance of our Window
# window = Window()
 
# # start the app
# sys.exit(App.exec())
# # Output
l=[0,0,0,0,0,0,0]
print(any(l))
