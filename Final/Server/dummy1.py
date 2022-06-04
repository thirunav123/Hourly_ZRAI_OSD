# import datetime,os
# from openpyxl import Workbook,load_workbook
# total_file= open("total.txt", "r")
# filedic={}
# # list(map(int,shiftA_start.strip().split(":"))
# for line in total_file:
#     file_data=line.strip().split('===')
#     a=int(file_data[0])
#     # b=.strip().split(",")
#     b=map(int,file_data[1].strip().split(","))
#     filedic[a]=b
# total_file.close()
# print(filedic)
# station="st"
# wb=Workbook()
# wb.create_sheet(station)
# ws=wb[station]
# for i in range(68):
#     # if i%2==0:
#         ws.cell(row=1,column=i+1).value=1
# raw_list=list(ws.rows)
# r=1
# for t in filedic:
#     total=0
#     for a in filedic[t]:
#         v=raw_list[r-1][a-1].value
#         if not v is None:
#             total=total+v
#     ws.cell(row=r,column=t).value=total
# wb.save("total.xlsx")
# # wb.close()
# # wob=load_workbook("a.xlsx",data_only=True)
# # wos=wob[station]
# # print(type(int(wos["A1"].value)))

# import time
# print(time.time())
# v=30.54
# if not v is None:
#     print(int(v))
# import datetime
# def get_shift(ct):
#     startA=datetime.time(6,0,0)
#     startB=datetime.time(14,30,0)
#     startC=datetime.time(22,30,0)
#     if startA<ct<startB:
#         return 'A'
#     if startB<ct<startC:
#         return 'B'
#     else:
#         return 'C'
# time_now=datetime.datetime.now()
# current_time=datetime.time(time_now.hour,time_now.minute,time_now.second)
# if current_time<datetime.time(6,0,0):
#     dp=1
# else:
#     dp=0
# # plc,"Total",pq,it,time_of_eve
# time_now=time_now-datetime.timedelta(days=dp)
# # print(date.strftime("%I.%M.%S_%p"))
# date=time_now.strftime('%d%m')
# shift=get_shift(current_time)
# shift_no=ord(shift)-64
# unique_no=int(str(shift_no)+str(date))
# unique_no_in_bytes=unique_no.to_bytes(2,"big")
# print(unique_no_in_bytes)
# error_data=b'\x01\x00\x09'
# if error_data[0]==1:
#     print("A")
# a=20206
# b=str(a).encode()
# # b=a.to_bytes(2,"little")
# a=b.decode()
# print(type(a))
a=1234
b=1234
if not a is b:
    print("same")