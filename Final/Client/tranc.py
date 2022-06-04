import snap7,time,queue,threading,datetime,schedule,socket
# from snap7.types import *

lock=threading.Lock()
file=open('snap7_client_settings.txt','r')
print('MT: I am a Client')
filedic={}
# uno_queue=queue.Queue()
server_queue=queue.Queue()
error_register_queue=queue.Queue()
for line in file:
    file_data=line.strip().split('===')
    a=file_data[0]
    b=file_data[1]
    filedic[a]=b
ipaddresses_of_plc=filedic.pop('ipaddresses_of_plc').split(',')
ipaddress_of_server_system=filedic.pop('ipaddress_of_server_system')
db_numbers_of_plc_respectively=filedic.pop('data_block_numbers_of_plc_respectively').split(',')
# hourly_list=filedic.pop('hourly_intimate').split(",")
port_of_server_system=int(filedic.pop('port_of_server_system'))
# bytes_to_split=int(filedic.pop('bytes_to_split'))
shiftA_start=filedic.pop('shiftA_start_time')
shiftB_start=filedic.pop('shiftB_start_time')
shiftC_start=filedic.pop('shiftC_start_time')
A=list(map(int,shiftA_start.strip().split(':')))
B=list(map(int,shiftB_start.strip().split(':')))
C=list(map(int,shiftC_start.strip().split(':')))
# min_idle_time_to_register=int(filedic.pop('minimum_idle_time_to_register_in_seconds'))
# columns_before_pq_and_it_in_excel_server=int(filedic.pop('columns_before_pq_and_it_in_excel_server'))
# i_level1_timeout=int(filedic.pop('idle_time_level1_timeout_in_seconds'))
# i_level2_timeout=int(filedic.pop('idle_time_level2_timeout_in_seconds'))
# i_level3_timeout=int(filedic.pop('idle_time_level3_timeout_in_seconds'))
plc_db_read_delay=int(filedic.pop('plc_db_read_delay_in_milliseconds'))/1000
error_wait=int(filedic.pop('error_wait_in_milliseconds'))/1000
# scheduler_delay=int(filedic.pop("scheduler_delay_in_milliseconds"))/1000
server_reconnect_delay=int(filedic.pop('server_reconnect_delay_in_milliseconds'))/1000
server_data_move_delay=int(filedic.pop('server_data_move_delay_in_milliseconds'))/1000
# it_register=int(filedic.pop("idletime_register_count"))
sct=int(filedic.pop('server_connect_time_in_seconds'))


# ta=filedic.pop("Total_A")
# tb=filedic.pop("Total_B")
# tc=filedic.pop("Total_C")
print('MT: Settings file read')
# raw_dict={}
# sub_dict={}
# idle_time=1
unique_no=None

def server_data_move():
    global unique_no
    write_flag=False
    while True:
        try:
            if not server_queue.empty():
                soc_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                # print('SDM: Connecting to Server...')
                try:
                    soc_s.connect((ipaddress_of_server_system,port_of_server_system))
                    # print('SDM: Server Connected')
                except:
                    # print('SDM: Reconnecting to Server...')
                    time.sleep(server_reconnect_delay)
                    continue
                # soc_s.did
                data=server_queue.get()
                
                soc_s.sendall(data)
                un_in_bytes=soc_s.recv(1024)
                unique_no=int.from_bytes(un_in_bytes,'big')
                # uno_queue.put(unique_no)
                # print(data)
                # soc.send(b'\x00')
            # soc.
            # soc.recv(1024)
                # soc.shutdown(socket.SHUT_RDWR)
                print('SDM: Data sent to Server') 
                soc_s.close()
            time.sleep(server_data_move_delay)
            write_flag=False
        except Exception as e:
            soc_s.close()
            if not write_flag:
                error_register_queue.put(f'SDM: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
                write_flag=True
                print(f'SDM: Error acquired and recorded. Error: {e}')
            else: 
                print(f'SDM: Error acquired and already recorded. Error: {e}')
            time.sleep(error_wait)

# def get_shift(ct):
#     startA=datetime.time(A[0],A[1],A[2])
#     startB=datetime.time(B[0],B[1],B[2])
#     startC=datetime.time(C[0],C[1],C[2])
#     if startA<ct<startB:
#         return 1
#     if startB<ct<startC:
#         return 2
#     else:
#         return 3


# def get_unique_number():
#     # t=datetime.datetime.now()
#     # print(t)
#     # t=1654016400
#     # print(t)
#     time_now=datetime.datetime.now()
#     current_time=datetime.time(time_now.hour,time_now.minute,time_now.second)
#     if current_time<datetime.time(A[0],A[1],A[2]):
#         dp=1
#     else:
#         dp=0
#     # plc,"Total",pq,it,time_of_eve
#     time_now=time_now-datetime.timedelta(days=dp)
#     # print(date.strftime("%I.%M.%S_%p"))
#     date=time_now.strftime('%d%m')
#     shift=get_shift(current_time)
#     un=str(date)+str(shift)
#     # un=un.encode()
#     return int(un)

# def shift_reset_job():

#     # time.sleep(5)
#     # inf=2
#     # hour=shift_total
#     # ct=round(time.time())
#     try:
#         for ip in ipaddresses_of_plc:
#             # hpq=raw_dict[ip]["npq"]
#             # hit=round(raw_dict[ip]["nit"])
#             # data=inf.to_bytes(1,'big')+raw_dict[ip]["name"].to_bytes(1,'big')+hour.to_bytes(1,'big')+raw_dict[ip]['on_off_count'].to_bytes(1,'big')+hpq.to_bytes(bytes_to_split,'big')+hit.to_bytes(bytes_to_split,'big')+ct.to_bytes(bytes_to_split,'big')
#             # server_queue.put(data)
#             lock.acquire()
#             raw_dict[ip]["reset_flag"]=True
#             raw_dict[ip]["on_off_count"]=0
#             raw_dict[ip]["opq"]=0
#             raw_dict[ip]["npq"]=0
#             raw_dict[ip]["oit"]=0
#             raw_dict[ip]["nit"]=0
#             lock.release()

#         print("SRJ: All reset")
#     except Exception as e:
#         error_register_queue.put(f'SRJ: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
#         print(f'SRJ: Error acquired and recorded. Error: {e}') 
#         time.sleep(error_wait)

# def hourly(hour):
#     try:
#         inf=2
#         # lock.acquire()
#         for ip in ipaddresses_of_plc:
#             if raw_dict[ip]["machine_status"]:
#                 ct=round(time.time())-prior_time
#                 hpq=raw_dict[ip]["npq"]-raw_dict[ip]["opq"]
#                 hit=round(raw_dict[ip]["nit"]-raw_dict[ip]["oit"])
#                 data=inf.to_bytes(1,'big')+raw_dict[ip]["name"].to_bytes(1,'big')+hour.to_bytes(1,'big')+raw_dict[ip]['on_off_count'].to_bytes(1,'big')+hpq.to_bytes(bytes_to_split,'big')+hit.to_bytes(bytes_to_split,'big')+raw_dict[ip]["npq"].to_bytes(bytes_to_split,'big')+raw_dict[ip]["nit"].to_bytes(bytes_to_split,'big')+ct.to_bytes(bytes_to_split,'big')
#                 server_queue.put(data)
#                 lock.acquire()
#                 raw_dict[ip]["opq"]=raw_dict[ip]["npq"]
#                 raw_dict[ip]["oit"]=raw_dict[ip]["nit"]
#                 lock.release()
#                 print("H: Hourly message triggered   ",hour)

#     except Exception as e:
#         error_register_queue.put(f'H: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
#         print(f'H: Error acquired and recorded. Error: {e}')
#         time.sleep(error_wait)
#     # lock.release()
    
# def reset_thread():
#     try:
#         # schedule.every().day.at(shiftA_start).do(shift_reset_job)
#         # schedule.every().day.at(shiftB_start).do(shift_reset_job)
#         # schedule.every().day.at(shiftC_start).do(shift_reset_job)
#         for index_i,i in enumerate(hourly_list):
#             # print(i)
#             schedule.every().day.at(i).do(hourly,(index_i*2)+columns_before_pq_and_it_in_excel_server+1)
#             # schedule.every().day.at(i).do(hourly,(hourly_list.index(i)*2)+columns_before_pq_and_it_in_excel_server+1)
#             # print(hourly_list.index(i))
#         schedule.every().day.at(shiftA_start).do(shift_reset_job)
#         schedule.every().day.at(shiftB_start).do(shift_reset_job)
#         schedule.every().day.at(shiftC_start).do(shift_reset_job)
#         while True:
#             schedule.run_pending()
#             time.sleep(scheduler_delay)

#     except Exception as e:
#         error_register_queue.put(f'RT: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
#         print(f'RT: Error acquired and recorded. Error: {e}')
#         time.sleep(error_wait)

def error_register():
    while True:
        err=error_register_queue.get()
        with open('readme.txt', 'a') as f:
            f.write(err)
        f.close()

# def pq_and_it_calc_thread(ip,pdq,plc):
#     machine_status_flag=False
#     inf=0
#     it_count=0
#     entry_flag,level1_flag,level2_flag,level3_flag,register_flag=False,False,False,False,False
#     initial_time=round(time.time())
#     int_value=raw_dict[ip]["nit"]
#     write_flag=False
#     while True:
#         try:
#                 if raw_dict[ip]["machine_status"]:
#                     inf=1
#                     # if not pdq.empty():
#                     pq_count=pdq.get()
#                     if pq_count==raw_dict[ip]["npq"]:
#                     # entry_flag,level1_flag,level2_flag,level3_flag=False,False,False,False
#                         current_time=round(time.time())
#                         if initial_time+min_idle_time_to_register<current_time:
#                             if not entry_flag:
#                                 state=0
#                                 data=inf.to_bytes(1,'big')+plc.to_bytes(1,'big')+state.to_bytes(1,'big')+initial_time_in_bytes+current_time.to_bytes(bytes_to_split,'big')
#                                 server_queue.put(data)
#                                 entry_flag=True
#                                 print(f"PAICT: Idle time started, Entry registered {plc}")
#                             if initial_time+i_level1_timeout<current_time:
#                                 if not level1_flag:
#                                     state=1
#                                     data=inf.to_bytes(1,'big')+plc.to_bytes(1,'big')+state.to_bytes(1,'big')+initial_time_in_bytes+current_time.to_bytes(bytes_to_split,'big')
#                                     server_queue.put(data)
#                                     level1_flag=True
#                                     print(f"PAICT: LLLLLLLLLLLLLLLLLLLLLevel1 {plc}")
#                                 if initial_time+i_level2_timeout<current_time:
#                                     if not level2_flag:
#                                         state=2
#                                         data=inf.to_bytes(1,'big')+plc.to_bytes(1,'big')+state.to_bytes(1,'big')+initial_time_in_bytes+current_time.to_bytes(bytes_to_split,'big')
#                                         server_queue.put(data)
#                                         level2_flag=True
#                                         print(f"PAICT: LLLLLLLLLLLLLLLLLLLLLevel2 {plc}")
#                                     if initial_time+i_level3_timeout<current_time:
#                                         if not level3_flag:
#                                             state=3
#                                             data=inf.to_bytes(1,'big')+plc.to_bytes(1,'big')+state.to_bytes(1,'big')+initial_time_in_bytes+current_time.to_bytes(bytes_to_split,'big')
#                                             server_queue.put(data)
#                                             level3_flag=True
#                                             print(f"PAICT: LLLLLLLLLLLLLLLLLLLLLevel3 {plc}")
#                         it_count=it_count+1
#                         if entry_flag or level1_flag or level2_flag or level3_flag:
#                             if not register_flag:
#                                 int_value=raw_dict[ip]["nit"]  
#                                 idle_time=(current_time-initial_time)
#                                 lock.acquire()
#                                 raw_dict[ip]["nit"]=int_value+idle_time
#                                 lock.release()
#                                 it_count=0
                                
#                                 register_flag=True
#                             if it_count>=it_register:  
#                                 idle_time=(current_time-initial_time)
#                                 # print(idle_time)
#                                 lock.acquire()
#                                 raw_dict[ip]["nit"]=int_value+idle_time
#                                 lock.release()
#                                 it_count=0
#                         # time.sleep()
#                     # initial_time=round(time.time())
#                     # initial_time_in_bytes=initial_time.to_bytes(bytes_to_split,'big')
                    
#                     else:
#                         # if trig_event.isSet():
#                         #     trig_event.clear()
#                             if register_flag:
#                                 lock.acquire()
#                                 raw_dict[ip]["nit"]=int_value
#                                 lock.release()
#                             if level3_flag:
#                                 state=7
#                                 data=inf.to_bytes(1,'big')+plc.to_bytes(1,'big')+state.to_bytes(1,'big')+initial_time_in_bytes+current_time.to_bytes(bytes_to_split,'big')
#                                 server_queue.put(data)
#                                 idle_time=(current_time-initial_time)
#                                 lock.acquire()
#                                 raw_dict[ip]["nit"]=raw_dict[ip]["nit"]+idle_time
#                                 lock.release()
#                                 print(f"PAICT: Idle time cleared {plc}")
#                             elif level2_flag:
#                                 state=6
#                                 data=inf.to_bytes(1,'big')+plc.to_bytes(1,'big')+state.to_bytes(1,'big')+initial_time_in_bytes+current_time.to_bytes(bytes_to_split,'big')
#                                 server_queue.put(data)
#                                 idle_time=(current_time-initial_time)  
#                                 lock.acquire()
#                                 raw_dict[ip]["nit"]=raw_dict[ip]["nit"]+idle_time
#                                 lock.release()
#                                 print(f"PAICT: Idle time cleared {plc}")
#                             elif level1_flag:
#                                 state=5
#                                 data=inf.to_bytes(1,'big')+plc.to_bytes(1,'big')+state.to_bytes(1,'big')+initial_time_in_bytes+current_time.to_bytes(bytes_to_split,'big')
#                                 server_queue.put(data)
#                                 idle_time=(current_time-initial_time)  
#                                 lock.acquire()
#                                 raw_dict[ip]["nit"]=raw_dict[ip]["nit"]+idle_time
#                                 lock.release()
#                                 print(f"PAICT: Idle time cleared {plc}")
#                             elif entry_flag:
#                                 state=4
#                                 data=inf.to_bytes(1,'big')+plc.to_bytes(1,'big')+state.to_bytes(1,'big')+initial_time_in_bytes+current_time.to_bytes(bytes_to_split,'big')
#                                 server_queue.put(data)
#                                 idle_time=(current_time-initial_time)  
#                                 lock.acquire()
#                                 raw_dict[ip]["nit"]=raw_dict[ip]["nit"]+idle_time
#                                 lock.release()
#                                 print(f"PAICT: Idle time cleared {plc}")
#                             # print(f"TP: Idle time cleared {plc}")
#                             entry_flag,level1_flag,level2_flag,level3_flag,register_flag=False,False,False,False,False
#                             lock.acquire()
#                             raw_dict[ip]["npq"]=pq_count
#                             lock.release()
#                             initial_time=round(time.time())
#                             initial_time_in_bytes=initial_time.to_bytes(bytes_to_split,'big')
#                     # time.sleep(1)
#                 write_flag=False
#                 # else:
#         except Exception as e:
#             if not write_flag:
#                 error_register_queue.put(f'PAICT: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
#                 write_flag=True
#                 print(f'PAICT: Error acquired and recorded. Error: {e}')
#             else: 
#                 print(f'PAICT: Error acquired and already recorded. Error: {e}')
#             time.sleep(error_wait)        
        
#         # time.sleep(0.1)

#     # if 
#     # 
#     #                     it

def snap7_thread(ipaddress_of_plc,db_number,plc):
            global unique_no
            write_flag=False
    # while True:
    #     try:
            connection_flag=False
            alive_flag=True
            alive=alive_flag.to_bytes(1,'big')
            pc=0
            pt=round(time.time())
            while True:
                try:
                    ct=round(time.time())
                    if not connection_flag:
                        client=snap7.client.Client()
                        client.connect(ipaddress_of_plc,0,1,102)
                        # print(bool(client.get_connected))
                        connection_flag=True
                        # raw_dict[ipaddress_of_plc]["machine_status"]=True
                    if pt+sct<ct:
                        data=client.db_read(db_number,0,6)
                        cc=int.from_bytes(data[4:6],'big')
                        if not unique_no is None:
                            if not unique_no==int.from_bytes(data[2:4],'big'):
                                reset=0
                                byte_data=unique_no.to_bytes(2,'big')+reset.to_bytes(2,'big')
                                client.db_write(db_number,2,byte_data)
                                print(f'ST{plc}: Count Reset')
                        if not pc==cc:
                            server_data=plc.to_bytes(1,'big')+data[4:6]
                            server_queue.put(server_data)
                            pc=cc
                        else:
                            temp=1
                            server_data=temp.to_bytes(1,'big')
                            server_queue.put(server_data)
                        pt=ct
                        print(f'ST{plc}: Production Count = {cc}')
                    client.db_write(db_number,0,alive)
                    time.sleep(plc_db_read_delay)
                    write_flag=False
                    # uni_no=get_unique_number()
                    # cc=int.from_bytes(data[4:6],'big')
                    # if pc is cc:
                        # if not unique_no is int.from_bytes(data[1:3],'big'):
                            # reset=0
                            # byte_data=unique_no.to_bytes(2,'big')+reset.to_bytes(2,'big')
                            # client.db_write(db_number,1,byte_data)
                            # print(f'ST{plc}: Count Reset')
                    # else:
                        # byte_data=alive_flag.to_bytes(1,'big')
                        
                    #         print(f'ST{plc}: Current production count : {cc}')
                    #         pc=cc    
                    # client.db_write(db_number,0,alive)                
                    # time.sleep(plc_db_read_delay)
                    # write_flag=False
                    # write_flag_2=False
                except Exception as e:
                    # print(type(str(e)))
                    if str(e)=="b' TCP : Unreachable peer'":
                        print(f'ST{plc}: Unable to connect')
                        connection_flag=False
                        # raw_dict[ipaddress_of_plc]["machine_status"]=False
                    if str(e)=="b' ISO : An error occurred during send TCP : Connection reset by peer'":
                        print(f'ST{plc}: Disconnected')
                        connection_flag=False
                        # raw_dict[ipaddress_of_plc]["machine_status"]=False
                    if str(e)=="b' ISO : An error occurred during recv TCP : Connection timed out'":
                        print(f'ST{plc}: Unable  to connect')
                        connection_flag=False
                        # raw_dict[ipaddress_of_plc]["machine_status"]=False
                    # print(Exception)
                    if not write_flag:
                        error_register_queue.put(f'ST{plc}: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
                        if str(e)=="b' TCP : Unreachable peer'" or str(e)=="b' ISO : An error occurred during send TCP : Connection reset by peer'" or str(e)=="b' ISO : An error occurred during recv TCP : Connection timed out'":
                            off_no=65535
                            server_data=plc.to_bytes(1,'big')+off_no.to_bytes(2,'big')
                            server_queue.put(server_data)
                            print(f'ST{plc}: Machine OFF')
                        write_flag=True
                        print(f'ST{plc}: Error acquired and recorded. Error: {e}')
                    else: 
                        print(f'ST{plc}: Error acquired and already recorded. Error: {e}')
                    time.sleep(error_wait)
                    # time.sleep(3)
                    
                    # time.sleep(1)
                    # connection_flag=False
        # except Exception as e:
        #     if not write_flag_1:
        #         error_register_queue.put(f'ST{i}: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
        #         write_flag_1=True
        #         print(f'ST{i}: Error acquired and recorded. Error: {e}')
        #     else: 
        #         print(f'ST{i}: Error acquired and already recorded. Error: {e}')
        #     time.sleep(error_wait) 

# sub_defalut_value_dic={"name":0,"npq":0,"nit":0,"opq":0,"oit":0,"reset_flag":False,"on_off_count":0,"machine_status":False}

# for ip in ipaddresses_of_plc:
#     sub_defalut_value_dic['name']=int(filedic[ip])
#     raw_dict[ip]=sub_defalut_value_dic.copy()
# raw_dict[i]["it"]=4903
# print(raw_dict)

for index,ip in enumerate(ipaddresses_of_plc):
    plc=filedic[ip]
    client_thread_pro = threading.Thread(target=snap7_thread,args=(ip,int(db_numbers_of_plc_respectively[index]),int(plc)),daemon=True)
    client_thread_pro.start()
    # pq_and_it_calc_th = threading.Thread(target=pq_and_it_calc_thread,args=(ipaddresses_of_plc[i],plc_data_queue,int(filedic[ipaddresses_of_plc[i]])),daemon=True)
    # print(ip)
    # pq_and_it_calc_th.start()
    # print(plc_data_queue)
    # raw_dict[ipaddresses_of_plc[i]]=sub_dict
    print(f'MT: Client_thread started {plc}')

server_data_mo = threading.Thread(target=server_data_move,daemon=True)
server_data_mo.start()
print(f'MT: Server_data_move thread started')
# reset_th = threading.Thread(target=reset_thread,daemon=True)
# reset_th.start()
# print(f"MT: Reset_thread thread started")
error_reg = threading.Thread(target=error_register,daemon=True)
error_reg.start()
print(f'MT: Error_register thread started')

while True:
    time.sleep(60)
    # print(f"MT: {raw_dict}")
# client=snap7.client.Client()
# client.connect("192.168.0.1",0,1,102)
# print(bool(client.get_connected))
# while 

# print("Before change:")

# print(data1)
# data2=client.db_read(1,1,1)
# print(data2)

# print("After change:")
# client.db_write(1,0,b'\x01')
# client.db_write(1,1,b'\x01')
# data1=client.db_read(1,0,1)
# print(data1)
# data2=client.db_read(1,1,1)
# print(data2)