# # from importlib.metadata import requires
# # import os,socket,queue,datetime,time,threading,requests,json,schedule
# # from openpyxl import Workbook,load_workbook
# # from smtplib import SMTP
# # from email.mime.text import MIMEText
# # from email.mime.multipart import MIMEMultipart

# # setting_file=open('server_settings.txt','r')
# # print("MT: I am a Server")
# # filedic={}
# # for line in setting_file:
# #     file_data=line.strip().split('===')
# #     a=file_data[0]
# #     b=file_data[1]
# #     filedic[a]=b
# # setting_file.close()
# # ipaddress_of_system=filedic.pop('ipaddress_of_server_system')
# # port_to_listen=int(filedic.pop('port_to_listen'))
# # shiftA_start=filedic.pop('shiftA_start_time')
# # shiftB_start=filedic.pop('shiftB_start_time')
# # shiftC_start=filedic.pop('shiftC_start_time')
# # filename_of_i_excel=filedic.pop('filename_of_idle_time_excel_sheet')
# # filename_of_h_excel=filedic.pop('filename_of_hourly_excel_sheet')
# # mfg_webhook_url1=filedic.pop('mfg_webhook_url_level1')
# # mfg_webhook_url2=filedic.pop('mfg_webhook_url_level2')
# # mfg_webhook_url3=filedic.pop('mfg_webhook_url_level3')
# # bytes_to_split=int(filedic.pop('bytes_to_split'))
# # level1_name=filedic.pop('level1_name')
# # level2_name=filedic.pop('level2_name')
# # level3_name=filedic.pop('level3_name')
# # hourly_sheet_name=filedic.pop('hourly_sheet_name')
# # header_row_h=int(filedic.pop('header_row_hourly'))
# # total_columns=int(filedic.pop('total_columns'))
# # mfg_space_url=filedic.pop('mfg_space_url')
# # scheduler_delay=int(filedic.pop("scheduler_delay_in_milliseconds"))/1000
# # error_wait=int(filedic.pop("error_wait_in_milliseconds"))/1000
# # h_chat_queue_timeout=int(filedic.pop("hourly_chat_queue_timeout_in_seconds"))
# # mail_trig_delay=int(filedic.pop("mail_trigger_delay_after_next_shift_start_in_seconds"))
# # common_letters=int(filedic.pop("common_letters_count_from_begin_in_pq_and_it_columns"))
# # print("MT: Settings file read")

# # total_file= open("total.txt", "r")
# # mail_file = open("mail.txt", "r")
# # summary_a_file= open("summary_A.txt", "r")
# # summary_b_file= open("summary_B.txt", "r")
# # summary_c_file= open("summary_C.txt", "r")

# # total_dic={}
# # list_of_mails= []
# # summary_a_list= []
# # summary_b_list= []
# # summary_c_list= []
# # for line in total_file:
# #     file_data=line.strip().split('===')
# #     a=int(file_data[0])
# #     # b=.strip().split(",")
# #     b=map(int,file_data[1].strip().split(","))
# #     total_dic[a]=b
# # for line in mail_file:
# #   list_of_mails.append(line.strip())
# # for line in summary_a_file:
# #   summary_a_list.append(line.strip())
# # for line in summary_b_file:
# #   summary_b_list.append(line.strip())
# # for line in summary_c_file:
# #   summary_c_list.append(line.strip())

# # total_file.close()
# # mail_file.close()
# # summary_a_file.close()
# # summary_b_file.close()
# # summary_c_file.close()
# # summary_dic={"A":summary_a_list,"B":summary_b_list,"C":summary_c_list}
# # print("MT: Total, Mail, Summary_A, Summary_B, Summary_C file read")
# # A=list(map(int,shiftA_start.strip().split(":")))
# # B=list(map(int,shiftB_start.strip().split(":")))
# # C=list(map(int,shiftC_start.strip().split(":")))
# # data_queue=queue.Queue()
# # it_excel_queue=queue.Queue()
# # it_chat_queue=queue.Queue()
# # h_chat_queue=queue.Queue()
# # h_excel_queue=queue.Queue()
# # error_register_queue=queue.Queue()
# # h_excel_queue.put([str(104),str(17),9,40,2,round(time.time())])

# # def move_excel_h():
# #     # line_column,date_column,shift_column,time_h_column,time_i_column,on_off_c_column,reqiured_row=1,1,1,1,1,1,1
# #     reqiured_row=1
# #     write_flag=False
# #     while True:
# #         # try:
# #             transfer_dic={}
# #             plc,h,on_off_c,pq,it,time_eve=h_excel_queue.get()
# #             t=datetime.datetime.fromtimestamp(time_eve)
# #             current_time=datetime.time(t.hour,t.minute,t.second)
# #             if current_time<datetime.time(A[0],A[1],A[2]):
# #                 dp=1
# #             else:
# #                 dp=0
# #             # plc,"Total",pq,it,time_of_eve
# #             date=t-datetime.timedelta(days=dp)
# #             date=date.strftime("%d-%m-%Y")
# #             # time_now=now.strftime("%I.%M.%S_%p")
# #             transfer_dic["LINE"]=filedic[plc]
# #             transfer_dic["DATE"]=date
# #             transfer_dic["HOUR"]=filedic[h]
# #             transfer_dic["SHIFT"]="A"
# #             transfer_dic["ON/OFF_Count"]=on_off_c
# #             transfer_dic["PQ"]=pq
# #             # line_pq=filedic [plc]+"_pq"
# #             # line_it=filedic[plc]+"_it"
# #             # time_h=h+"_pq"
# #             # time_i=h+"_it"
# #             # transfer_dic[time_h]=pq
# #             transfer_dic["IT"]=round(it/60,2)
            
# #             # if not os.path.isfile(filename_of_excel):
# #             if not os.path.isfile(filename_of_h_excel):
# #                 wb=Workbook()
# #             else:
# #                 wb=load_workbook(filename_of_h_excel)
# #             station=hourly_sheet_name
# #             # if station_list!=wb.sheetnames:
# #             #     for station in station_list:
# #             if not station in wb.sheetnames:
# #                 wb.create_sheet(station)
# #                 ws=wb[station]
# #                 for i in range(1,total_columns+1):
# #                     ws.cell(row=header_row_h,column=i).value=filedic[str(i)]
# #             ws=wb[station]        
# #             xl_headers=[]
# #             for i in ws[header_row_h]:
# #                 xl_headers.append(i.value)
# #             # mc=ws.max_column
# #             # mr=ws.max_row
# #             # for i in transfer_dic:
# #             #     if i not in xl_headers:
# #             #         ws.cell(1,mc+1).value=i
# #             #         xl_headers.append(i)
# #             #         mc=ws.max_column
# #             date_column=int(filedic["date_column"])
# #             line_column=int(filedic["line_column"])
# #             # for i in range(1,mc+ 1):
# #             #     # if ws.cell(row=header_row_h,coulmn=i):
# #             #     v=ws.cell(row=header_row_h,column=i).value
# #             #     if v=="LINE":
# #             #         line_column=i
# #             #         # print(i)
# #             #     if v=="DATE":
# #             #         date_column=i
# #                     # print(i)
# #                 # if v=="SHIFT":
# #                 #     shift_column=i
# #                     # print(i)
# #                 # if v==time_h:
# #                 #     time_h_column=i
# #                 #     # print(i)
# #                 # if v==time_i:
# #                 #     time_i_column=i
# #                 # if v=="ON/OFF_Count":
# #                 #     on_off_c_column=i
# #                     # print(i)
# #             compare_list=[transfer_dic["LINE"],transfer_dic["DATE"]]
# #             value_list=[]
# #             exist_flag=False
# #             h=int(h)
# #             for row in ws.rows:
# #                 for cell in row:
# #                     value_list.append(cell.value)
# #                 # print(type(row))
# #                 check = all(item in value_list for item in compare_list)
# #                 if check:
# #                     print("Exist")
# #                     exist_flag=True
# #                     reqiured_row=cell.row
# #                     ws.cell(row=reqiured_row,column=h).value=transfer_dic["PQ"]
# #                     ws.cell(row=reqiured_row,column=h+1).value=transfer_dic["IT"]
# #                     if transfer_dic["SHIFT"]=="A":
# #                         ws.cell(row=reqiured_row,column=int(filedic["on_off_countA"])).value=transfer_dic["ON/OFF_Count"]
# #                     elif transfer_dic["SHIFT"]=="B":
# #                         ws.cell(row=reqiured_row,column=int(filedic["on_off_countB"])).value=transfer_dic["ON/OFF_Count"]
# #                     else:
# #                         ws.cell(row=reqiured_row,column=int(filedic["on_off_countC"])).value=transfer_dic["ON/OFF_Count"]
# #                     break
# #             mr=ws.max_row
# #             # print( line_column,date_column,shift_column,time_h_column,time_i_column)

# #             if not exist_flag:
# #                 print("Not Exist")
# #                 reqiured_row=mr+1
# #                 ws.cell(row=reqiured_row,column=line_column).value=transfer_dic["LINE"]
# #                 ws.cell(row=reqiured_row,column=date_column).value=transfer_dic["DATE"]
# #                 ws.cell(row=reqiured_row,column=h).value=transfer_dic["PQ"]
# #                 ws.cell(row=reqiured_row,column=h+1).value=transfer_dic["IT"]
# #                 if transfer_dic["SHIFT"]=="A":
# #                         ws.cell(row=reqiured_row,column=int(filedic["on_off_countA"])).value=transfer_dic["ON/OFF_Count"]
# #                 elif transfer_dic["SHIFT"]=="B":
# #                         ws.cell(row=reqiured_row,column=int(filedic["on_off_countB"])).value=transfer_dic["ON/OFF_Count"]
# #                 else:
# #                         ws.cell(row=reqiured_row,column=int(filedic["on_off_countC"])).value=transfer_dic["ON/OFF_Count"]
# #             raw_list=list(ws.rows)
# #             for t in total_dic:
# #                 total=0
# #                 for a in total_dic[t]:
# #                     v=raw_list[reqiured_row-1][a-1].value
# #                     if not v is None:
# #                         total=total+int(v)
# #                 ws.cell(row=reqiured_row,column=t).value=total
# #                 # if ws.cell(row=i,column=line_column).value==transfer_dic["LINE"]:
# #                     # if ws.cell(row=i,column=line_column).value==transfer_dic["LINE"]:
                
# #             # it_chat_queue.put([2,transfer_dic["LINE"],transfer_dic["DATE"],transfer_dic["SHIFT"],transfer_dic[time_h],transfer_dic[time_i]])

# #             # for i in xl_headers:.lo0  
# #             # .0   
# #             #     for j in transfer_dic:
# #             #         if i==j:
# #             #             ws.cell(mr+1,xl_headers.index(i)+1).value=excel_dic[i]
# #             while True:
# #                 try:
# #                     wb.save(filename_of_h_excel)
# #                     print(f"EXH: Hourly and Idle time data saved successfully {time.strftime('%d-%m-%Y_%I.%M.%S_%p')} {transfer_dic['LINE']}")
# #                 except:
# #                     # wb.save(filename_of_excel)
# #                     print(f"EXH: Data not saved, Close the excel file({filename_of_h_excel}) if it is opened. Retrying to save...")
# #                     time.sleep(3)
# #                     continue
# #                 break
# #             wb.close()
# #             write_flag=False
# #         # except Exception as e:
# #         #     if not write_flag:
# #         #         error_register_queue.put(f'EXH: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
# #         #         write_flag=True
# #         #         print(f'EXH: Error acquired and recorded. Error: {e}')
# #         #     else: 
# #         #         print(f'EXH: Error acquired and already recorded. Error: {e}')
# #         #     time.sleep(error_wait)

# # move_ex_h = threading.Thread(target=move_excel_h,daemon=True)
# # move_ex_h.start()
# # print("MT: Move_excel_h thread started")
# # while True:
# #   time.sleep(1)

# # from ctypes import sizeof
# # from typing import Sized

# # import time,datetime
# # A=[6,0,0]
# # B=[14,30,0]
# # C=[22,30,0]

# # def get_shift(ct):
# #     startA=datetime.time(A[0],A[1],A[2])
# #     startB=datetime.time(B[0],B[1],B[2])
# #     startC=datetime.time(C[0],C[1],C[2])
# #     if startA<ct<startB:
# #         return 'A'
# #     if startB<ct<startC:
# #         return 'B'
# #     else:
# #         return 'C'
# # a=65535
# # time_eve=time.time()
# # t=datetime.datetime.fromtimestamp(time_eve)
# # current_time=datetime.time(t.hour,t.minute,t.second)
# # if current_time<datetime.time(A[0],A[1],A[2]):
# #     dp=1
# # else:
# #     dp=0
# # # plc,"Total",pq,it,time_of_eve
# # date=t-datetime.timedelta(days=dp)
# # date=date.strftime("%d-%m-%Y")
# # shift=get_shift(current_time)
# from pickle import FALSE
# from secrets import token_bytes


# a=11
# b=12
# if a is b:
#     print("Matched")
# # a=112
# # # sizeof
# # b=a.to_bytes(5,"little")
# # print(int.from_bytes(b[0:2],'big'))
# # print(len(b))
# # c=time.strftime("%d-%m-%Y_%I.%M.%S_%p")
# # print(c)
# # # print (chr(ord(u'\u0BAF')))
# # print(ord("C")-64)
# # def get_unique_number():
# #     # t=datetime.datetime.now()
# #     # print(t)
# #     # t=1654016400
# #     # print(t)
# #     t=datetime.datetime.now()
# #     current_time=datetime.time(t.hour,t.minute,t.second)
# #     if current_time<datetime.time(A[0],A[1],A[2]):
# #         dp=1
# #     else:
# #         dp=0
# #     # plc,"Total",pq,it,time_of_eve
# #     date=t-datetime.timedelta(days=dp)
# #     # print(date.strftime("%I.%M.%S_%p"))
# #     date=date.strftime("%d%m")
# #     shift=get_shift(current_time)
# #     un=str(date)+str(ord(shift)-64)
# #     return int(un)

# # print(get_unique_number())
# a=65535
# print(type(a))
# # print(a)
# # b=1
# # b=b.to_bytes(5,"little")
# # print(b)
# b=a.to_bytes(2,"big")
# print(b)
# # print(b[1:3])
# # a=11
# # a.to
# # b=111
# # c=11
# # d=111
# a=[23,3,4,4]
# for i,ine in enumerate(a):
#     print(i,ine)
# # if not a is b and c is d:
# #     print("m")
# total_dic={}
# total_file= open("total.txt", "r")
# for line in total_file:
#     file_data=line.strip().split('===')
#     a=int(file_data[0])
#     # b=.strip().split(",")
#     b=map(int,file_data[1].strip().split(","))
#     total_dic[a]=b
# for t in total_dic:
#                 total=0
#                 for a in total_dic[t]:
#                     print("1 ",a)
#                     # v=raw_list[reqiured_row-1][a-1].value
#                 #     if not v is None:
#                 #         total=total+float(v)
#                 # ws.cell(row=reqiured_row,column=t).value=total

# total_file.close()
# print(total_dic)
# import json,time,os
# filename="data.json"
# setting_file=open('server_settings.txt','r')
# filedic={}
# for line in setting_file:
#     file_data=line.strip().split('===')
#     a=file_data[0]
#     b=file_data[1]
#     filedic[a]=b
# setting_file.close()
# line_list=filedic.pop('LINES').split(",")
# if not os.path.isfile(filename):
#     file_dict={}
#     for line in line_list:
#         inner_dict={"opq":0,"oit":0,"npq":0,"nit":0,"on_off_count":0}
#         # inner_dict={"line":filedic[line][0],"mt":filedic[line][1],"l1_t":filedic[line][2],"l2_t":filedic[line][3],"l3_t":filedic[line][4],"lc":filedic[line][5],"opq":0,"oit":0,"npq":0,"nit":0,"on_off_count":0}
#         file_dict[line]=inner_dict
#     # file_dict[line]["line_no"]=1
#     dict_file=open(filename,"w")
#     json.dump(file_dict, dict_file)
#     print("Created")
# dict_file=open(filename,"r")
# loaded_str=dict_file.read()
# loaded_dict=json.loads(loaded_str)
# new_line_added,line_removed=False,False
# for line in line_list:
#     if line not in loaded_dict.keys():
#         inner_dict={"opq":0,"oit":0,"npq":0,"nit":0,"on_off_count":0}
#         loaded_dict[line]=inner_dict
#         new_line_added=True
# line_remove_list=[]
# for line in loaded_dict:
#     if line not in line_list:
#         line_remove_list.append(line)
#         line_removed=True
# if line_removed:
#     for line in line_remove_list:
#         loaded_dict.pop(line)
# if new_line_added or line_removed:
#     dict_file=open(filename,"w")
#     json.dump(loaded_dict, dict_file)
#     if new_line_added:
#         print("MT: New line added")
#     if line_removed:
#         print("MT: Existing line removed")
# print(loaded_dict)

# a={1:"2",3:"3"}
# for i in a.keys():
#     print(i)
# data=bytearray(b'\x01\x00\x00')
# data=bytearray(data)
# print(data.pop(0))
# import time
# from_time_format=time.strftime("%d-%m-%Y_%I.%M.%S_%p")
# print(from_time_format)
import threading,queue,time
eq=queue.Queue()
# cq=queue.Queue()
# a={1:"2",2:"3"}
# def test():
#     nd=a.copy()
#     cq.put(nd)
#     eq.put(nd)
#     del nd
# def chat():
#     d=cq.get()
#     time.sleep(1)
#     print("C",d[1])

# def excel():
#     while True:
#         d=eq.get()
#         time.sleep(1)
#         print("E",d[1])
#         del d

# test()
# test()
# move_ex_h = threading.Thread(target=chat,daemon=True)
# move_ex_h.start()
# move_ex_h = threading.Thread(target=excel,daemon=True)
# move_ex_h.start()
# while True:
#     time.sleep(10)
# hour=1
# a={1:"2",2:"3"}
# eq.put([1,a])
# s,d=eq.get()
# print(s,d)
# print(type(s),type(d))
# import datetime
# a=time.time()-10
import socket
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print(ipaddress_of_system,port_to_listen)
soc.bind(("192.168.0.112",2020))
soc.listen()
print("ST: waiting for message from client...")
# plc_addr=input("ipaddress : ")
# data=  
conn,addr=soc.accept()
pc_addr=addr[0]
print(f"ST: connected {addr}")
error_data=b'\x00\x00\x70\x00'
# print(addr[1],end=' ')
data=conn.recv(1024)
# print()
a=23456
# error_data=b'\x00'
# if error_data[0]:
#     print("A")
# a.enco
# b=
conn.sendall(b"un_no")
print(f"ST: Data received {pc_addr, data} ")
print(data)












# s=time.perf_counter()

# with open("data.json", "a") as a_file:
# # time.sleep(10)
#     loaded_str = a_file.appe
#     time.sleep(10)
# # # loaded_str='{"A":1,"B":2}'
# for line in line_list:
#     if line not in loaded_dict:
#         loaded_dict[line]=101
# # json.dump(dictionary_data, a_file)
# # a_file.close()
# print(loaded_dict)
# a='{"A":1,"B":2}'
# print(dict(a))
# d=json.loads(a)
# print(type(loaded_dict))
# print(d.keys())

# a_file = open("data.json", "wb")
# print(type(output))
# print(output)
# time.sleep(1)
# t=time.perf_counter()
# print(t-s)








