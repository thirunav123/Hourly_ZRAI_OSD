import os,sys,time,json,datetime,threading,psutil
import matplotlib.pyplot as plt
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtGui import  QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

name_list=os.path.basename(__file__).split('.')
name_list[-1]="exe"
exe_name=".".join(name_list)
print(exe_name)
process_count=0
for p in psutil.process_iter():
    if p.name()==exe_name:
        process_count=process_count+1
    if process_count>2:
        print(process_count)
        print("Already execution file ran")
        sys.exit()

gui_setting_file=open('GUI_settings.txt','r')
gui_filedic={}
for line in gui_setting_file:
    file_data=line.strip().split('===')
    a=file_data[0]
    b=file_data[1]
    gui_filedic[a]=b
work_folder_path=gui_filedic.pop('path_to_work_folder')
json_file_name=gui_filedic.pop('json_file_name')
json_load_delay=int(gui_filedic.pop('json_file_load_delay_in_milliseconds'))/1000
time_file_name=gui_filedic.pop('time_file_name')
conn_refresh_time=int(gui_filedic.pop("gui_connection_refresh_time_in_milliseconds"))
screen_refresh_time=int(gui_filedic.pop("gui_screen_refresh_time_in_milliseconds"))
next_page_time=int(gui_filedic.pop("gui_auto_next_page_time_in_milliseconds"))
low_prod_color=gui_filedic.pop('low_production_indication_color')
medium_prod_color=gui_filedic.pop('medium_production_indication_color')
high_prod_color=gui_filedic.pop('high_production_indication_color')
min_percent_of_medium_prod=int(gui_filedic.pop("minimum_percentage_of_medium_production"))
max_percent_of_medium_prod=int(gui_filedic.pop("maximum_percentage_of_medium_production"))
line_no_list=gui_filedic.pop('LINE_NUMBERS').split(",")
shiftA_start=gui_filedic.pop('shiftA_start_time')
shiftB_start=gui_filedic.pop('shiftB_start_time')
shiftC_start=gui_filedic.pop('shiftC_start_time')
A=list(map(int,shiftA_start.strip().split(":")))
B=list(map(int,shiftB_start.strip().split(":")))
C=list(map(int,shiftC_start.strip().split(":")))
json_file_path=os.path.join(work_folder_path,json_file_name)
time_file_path=os.path.join(work_folder_path,time_file_name)

loaded_dict={}
json_read_file=open(r'{}'.format(json_file_path),"r")
loaded_str=json_read_file.read()
json_read_file.close()
loaded_dict=json.loads(loaded_str)

dt_object=datetime.datetime.now()

line_data_dict={}
for line_no in line_no_list:
    details_list = gui_filedic.pop(line_no).split(",")
    cycle_time = int(details_list.pop())
    line_name = details_list.pop()
    # l_n : Line name, cy_t : cycle_time
    sub_dict={"l_n":line_name,"hour_cap":int(3600/cycle_time)}
    line_data_dict[line_no]=sub_dict

def get_server_time():
    while True:
        tf = open(time_file_path, "r")
        t = tf.readlines()
        print(t)
        if not t == []:
            timestamp = float(t.pop(0).split().pop(0))
            dt_object = datetime.datetime.fromtimestamp(timestamp)
            break
        time.sleep(.3)
    return dt_object


def get_shift(ct):
    startA=datetime.time(A[0],A[1],A[2])
    startB=datetime.time(B[0],B[1],B[2])
    startC=datetime.time(C[0],C[1],C[2])
    if startA<=ct<startB:
        return 'A'
    if startB<=ct<startC:
        return 'B'
    else:
        return 'C'
    
def load_dict_from_json():
    global loaded_dict
    while True:
        try:
            json_read_file=open(r'{}'.format(json_file_path),"r")
            loaded_str=json_read_file.read()
            json_read_file.close()
            loaded_dict=json.loads(loaded_str)
            time.sleep(json_load_delay)
        except Exception as e :
            print(e)
            pass
        # print(loaded_dict)

def get_text_by_sec(sec):
    if sec < 60:
        text = str(round(sec ,1))+'S'
        # print('The number of minutes is {0:.2f}'.format(minutes)) 
    elif sec < 3600:
        text = str(round(sec / 60,1))+'M'
        # print('The number of minutes is {0:.2f}'.format(hours))
    # elif sec <= 86400:
    #     text = str(round(sec / 3600,1))+'H'
        # print('The number of minutes is {0:.2f}'.format(days))
    else:
        text = str(round(sec / 3600,1))+'H'
    return text

class firstdialog(QDialog):
    def __init__(self):
        super(firstdialog,self).__init__()
        self.ui=loadUi("page_1.ui",self)#load the UI file 
        self.setMinimumSize(self.geometry().width(), self.geometry().height())
        # self.showFullScreen()
        self.conn_Timer = QTimer()
        self.screen_Timer = QTimer()
        self.page_Timer = QTimer()
        self.conn_Timer.timeout.connect(self.conn_color_change)
        self.screen_Timer.timeout.connect(self.screen_refresh)
        self.page_Timer.timeout.connect(self.next_page)
        self.conn_Timer.setInterval(conn_refresh_time)  
        self.screen_Timer.setInterval(screen_refresh_time) 
        self.page_Timer.setInterval(next_page_time)  
        self.conn_Timer.start()
        self.screen_Timer.start()
        self.auto_screen.setChecked(True)
        self.state=True
        if self.auto_screen.isChecked():
            self.page_Timer.start()
        self.auto_screen.stateChanged.connect(self.auto_screen_change)
        # self.conn_Timer.setInterval(conn_refresh_time) # 3000 ms 
        # self.conn_Timer.setInterval(10000)
        # self.conn_Timer        
        slice_by=4
        self.sliced_lists=[line_no_list[i:i+slice_by] for i in range(0,len(line_no_list),slice_by)]
        self.current_page_count=0
        self.max_page_index=len(self.sliced_lists)-1
        self.nl_list=["name_label_1","name_label_2","name_label_3","name_label_4"]
        self.ac_list=["actual_count_1","actual_count_2","actual_count_3","actual_count_4"]
        self.pc_list=["plan_count_1","plan_count_2","plan_count_3","plan_count_4"]
        self.pl_list=["percent_label_1","percent_label_2","percent_label_3","percent_label_4"]
        self.layout_list=["layout_1","layout_2","layout_3","layout_4"]
        self.cil_list=["cit_label_1","cit_label_2","cit_label_3","cit_label_4"]
        self.til_list=["tit_label_1","tit_label_2","tit_label_3","tit_label_4"]
        self.sl_list=["status_label_1","status_label_2","status_label_3","status_label_4"]
        for index_i,i in enumerate(self.nl_list):
            self.nl_list[index_i]=self.ui.findChild(QtWidgets.QLabel,i)
        for index_i,i in enumerate(self.ac_list):
            self.ac_list[index_i]=self.ui.findChild(QtWidgets.QLCDNumber,i)
        for index_i,i in enumerate(self.pc_list):
            self.pc_list[index_i]=self.ui.findChild(QtWidgets.QLCDNumber,i)
        for index_i,i in enumerate(self.pl_list):
            self.pl_list[index_i]=self.ui.findChild(QtWidgets.QLabel,i)
        for index_i,i in enumerate(self.layout_list):
            self.layout_list[index_i]=self.ui.findChild(QtWidgets.QVBoxLayout,i)
        for index_i,i in enumerate(self.cil_list):
            self.cil_list[index_i]=self.ui.findChild(QtWidgets.QLabel,i)
        for index_i,i in enumerate(self.til_list):
            self.til_list[index_i]=self.ui.findChild(QtWidgets.QLabel,i)
        for index_i,i in enumerate(self.sl_list):
            self.sl_list[index_i]=self.ui.findChild(QtWidgets.QLabel,i)
        self.figure_and_canvas_list=[]
        for index_li,layout_i in enumerate(self.layout_list):
            self.figure = plt.figure(str(index_li))
            self.canvas = FigureCanvas(self.figure)
            self.figure_and_canvas_list.append([self.figure ,self.canvas])
            layout_i.addWidget(self.canvas)
        self.count=0
        self.next_button.clicked.connect(self.next_page)
        self.previous_button.clicked.connect(self.previous_page)
        self.screen_falg=True
        self.full_and_maxi_screen_button.clicked.connect(self.full_and_maxi_screen)
        self.full_and_maxi_screen_button.setIcon(QIcon("exit_full_screen.png"))
        self.label_high_color.setStyleSheet(f'background-color: {high_prod_color};')
        self.label_high_text.setText(f" Above {max_percent_of_medium_prod}%")
        self.label_mid_color.setStyleSheet(f'background-color: {medium_prod_color};')
        self.label_mid_text.setText(f" {min_percent_of_medium_prod}% ~ {max_percent_of_medium_prod}%")
        self.label_low_color.setStyleSheet(f'background-color: {low_prod_color};')
        self.label_low_text.setText(f" Below {min_percent_of_medium_prod}%")

        
    def screen_refresh(self):
        try:
            self.temp_list=self.sliced_lists[self.current_page_count]
            temp_len=len(self.temp_list)
            nl_len=len(self.nl_list)
            if not temp_len==nl_len:
                for i in range(temp_len,nl_len):
                    self.nl_list[i].hide()
                    self.ac_list[i].hide()
                    self.pc_list[i].hide()
                    self.pl_list[i].hide()
                    self.figure_and_canvas_list[i][1].hide()
                    self.cil_list[i].hide()
                    self.til_list[i].hide()
                    self.sl_list[i].hide()
            for line_no_enum,nl,ac,pc,pl,cil,til,sl in zip(enumerate(self.temp_list),self.nl_list,self.ac_list,self.pc_list,self.pl_list,self.cil_list,self.til_list,self.sl_list):
                line_no_index=line_no_enum[0]
                line_no=line_no_enum[1]
                if loaded_dict[line_no]["ppq"]!=0:
                    self.prod_percent=(loaded_dict[line_no]["npq"]/loaded_dict[line_no]["ppq"])*100
                else:
                    self.prod_percent=0
                self.prod_percent=round(self.prod_percent,1)
                if self.prod_percent>max_percent_of_medium_prod:
                    self.color=high_prod_color
                elif self.prod_percent>=min_percent_of_medium_prod:
                    self.color=medium_prod_color
                else:
                    self.color=low_prod_color
                nl.setText(line_data_dict[line_no]["l_n"])
                # nl.setStyleSheet(f'''font: 87 22pt "Arial Black";
                #         background-color: rgb(0, 255, 0);
                #         color: rgb(0, 0, 0);
                #         border-radius:24px;
                #         background-color: {line_data_dict[line_no]["l_c"]};
                #         color: rgb(255, 255, 255);
                #         border-radius:24px;''')
                # print(round(self.prod_percent,1))
                if int(self.prod_percent)==self.prod_percent:
                    self.prod_percent=int(self.prod_percent)
                pl.setText(str(self.prod_percent)+"%")
                pl.setStyleSheet(f'''font: 87 22pt "Arial Black";
                        background-color: {self.color};
                        color: rgb(0, 0, 0);
                        border-radius:24px;''')
                ac.display(loaded_dict[line_no]["npq"])
                pc.display(loaded_dict[line_no]["ppq"])
                fc_list=self.figure_and_canvas_list[line_no_index]
                fc_list[0].clear()
                plt.figure(str(line_no_index))
                x=[]
                for i in range(1,len(loaded_dict[line_no]["hour_list_pq"])+1):
                    x.append(i)
                y=list(loaded_dict[line_no]["hour_list_pq"])
                y_ppq=list(loaded_dict[line_no]["hour_list_ppq"])                
                lc_per_h=line_data_dict[line_no]["hour_cap"]
                plt.xlim((0,10))
                # plt.title("titl987654567890-0987654567890-098765ree")
                x.append(11)
                maxim=max([max(loaded_dict[line_no]["hour_list_pq"]),lc_per_h])
                # if maxim==lc_per_h:
                #     maxim=10
                # print(maxim)
                y.append(int(maxim+(maxim*0.30)))
                cl=[]
                print(y,y_ppq)
                for i,j in zip(y,y_ppq):
                    if j!=0:
                        per=(i/j)*100
                    else:
                        per=0
                    if per>=max_percent_of_medium_prod:
                        color=high_prod_color
                    elif per>=min_percent_of_medium_prod:
                        color=medium_prod_color
                    else:
                        color=low_prod_color
                    cl.append(color)
                # cl=['red','yellow','green','red','yellow','green']
                plots=plt.bar(x,y,align='center',color=cl)
                tn=get_server_time()
                current_time=datetime.time(tn.hour,tn.minute,tn.second)
                shift=get_shift(current_time)
                if shift=='A':
                    self.label_hour_1.setText("06:00-\n07:00")
                    self.label_hour_2.setText("07:00-\n08:00")
                    self.label_hour_3.setText("08:00-\n09:00")
                    self.label_hour_4.setText("09:00-\n10:00")
                    self.label_hour_5.setText("10:00-\n11:00")
                    self.label_hour_6.setText("11:00-\n12:00")
                    self.label_hour_7.setText("12:00-\n13:00")
                    self.label_hour_8.setText("13:00-\n14:00")
                    self.label_hour_9.setText("14:00-\n14:30")
                    self.label_hour_9.show()
                    px=[]
                    py=[]
                    for i in range(1,10):
                        px.append(i)
                        py.append(lc_per_h)
                    py[8]=py[8]/2
                elif shift=='B':
                    self.label_hour_1.setText("14:30-\n15:30")
                    self.label_hour_2.setText("15:30-\n16:30")
                    self.label_hour_3.setText("16:30-\n17:30")
                    self.label_hour_4.setText("17:30-\n18:30")
                    self.label_hour_5.setText("18:30-\n19:30")
                    self.label_hour_6.setText("19:30-\n20:30")
                    self.label_hour_7.setText("20:30-\n21:30")
                    self.label_hour_8.setText("21:30-\n22:30")
                    self.label_hour_9.hide()
                    px=[]
                    py=[]
                    for i in range(1,9):
                        px.append(i)
                        py.append(lc_per_h)
                else:
                    self.label_hour_1.setText("22:30-\n23:30")
                    self.label_hour_2.setText("23:30-\n00:30")
                    self.label_hour_3.setText("00:30-\n01:30")
                    self.label_hour_4.setText("01:30-\n02:30")
                    self.label_hour_5.setText("02:30-\n03:30")
                    self.label_hour_6.setText("03:30-\n04:30")
                    self.label_hour_7.setText("04:30-\n05:30")
                    self.label_hour_8.setText("05:30-\n06:00")
                    self.label_hour_9.hide()
                    px=[]
                    py=[]
                    for i in range(1,10):
                        px.append(i)
                        py.append(lc_per_h)
                    py[8]=py[8]/2
                # for i in range()
                plt.plot(px,py)
                plt.text(10,lc_per_h,f"Capacity\n{lc_per_h}Nos/h",ha="right")
                for bar in plots:
                        # print(bar.get_height())
                        height=bar.get_height()
                        plt.annotate('{}'.format(height),
                        xy=(bar.get_x()+bar.get_width()/2,height),
                        xytext=(0,3),
                        textcoords='offset points',ha='center',va='center')
                # plt.grid(False)
                plt.axis("off")
                # plt.legend()
                fc_list[0].subplots_adjust(left=0, right=1,
                            top=1, bottom=0,
                            hspace=0, wspace=0)
                fc_list[1].draw()
                self.label_date.setText(tn.strftime('%d/%m/%Y ')+shift)
                self.label_time.setText(tn.strftime('%H:%M:%S'))
                text=get_text_by_sec(loaded_dict[line_no]["ogit"])
                cil.setText(text)
                text=get_text_by_sec(loaded_dict[line_no]["nit"]+loaded_dict[line_no]["ogit"])
                til.setText(text)
                sl.setStyleSheet(f'background-color: {loaded_dict[line_no]["conn_col"]}; border-radius:25px;')
                nl.show()
                ac.show()
                pc.show()
                pl.show()
                cil.show()
                til.show()
                fc_list[1].show()
                sl.show()
            # tamil_no_list=['௧','௨','௩','௪','௫','௬','௭','௮','௯']
            # if self.current_page_count<9:
            #     page_no=tamil_no_list[self.current_page_count]
            # else:
            #     page_no=self.current_page_count+1
            self.page_no_label.setText(str(self.current_page_count+1)+'/'+str(self.max_page_index+1))

            if self.current_page_count>=self.max_page_index:
                self.next_button.setEnabled(False)
            else:
                self.next_button.setEnabled(True)
            if self.current_page_count==0:
                self.previous_button.setEnabled(False)
            else:
                self.previous_button.setEnabled(True) 
        except Exception as e:
            print(e)
    def next_page(self):
        if self.current_page_count>=self.max_page_index:
            self.current_page_count=0
        else:
            self.current_page_count=self.current_page_count+1
        self.page_Timer.stop()
        if self.state:
            self.page_Timer.start()
    def previous_page(self):
        if self.current_page_count>0:
            self.current_page_count=self.current_page_count-1
        if self.state:
            self.page_Timer.stop()
            self.page_Timer.start()

    def conn_color_change(self):
        for line_no in loaded_dict:
                loaded_dict[line_no]["conn_col"]="red"
        loaded_dict[line_no]["conn_col"]='red'

    def auto_screen_change(self,state):
        self.state=state
        if self.state:
            self.page_Timer.start()
        else:
            self.page_Timer.stop()
        
    def full_and_maxi_screen(self):
        global widget
        if self.screen_falg:
            widget.showNormal()
            self.full_and_maxi_screen_button.setIcon(QIcon("full_screen.png"))
            self.screen_falg=False
        else:
            widget.showFullScreen()
            self.full_and_maxi_screen_button.setIcon(QIcon("exit_full_screen.png"))
            self.screen_falg=True
        

dict_bac = threading.Thread(target=load_dict_from_json,daemon=True)
dict_bac.start()
print(f"MT: Load_dict_from_json thread started")
app=QApplication(sys.argv)
mainwindow=firstdialog()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.showFullScreen()
widget.setWindowTitle("ZRAI_OSD")
widget.setWindowIcon(QIcon('gui_icon.ico'))


# widget.setFixedWidth(1280)
# widget.setFixedHeight(720)
widget.show()
sys.exit(app.exec())