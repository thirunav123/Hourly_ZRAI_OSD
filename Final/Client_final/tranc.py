import snap7,time,queue,threading,socket

lock=threading.Lock()
file=open('snap7_client_settings.txt','r')
print('MT: I am a Client')
filedic={}
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
port_of_server_system=int(filedic.pop('port_of_server_system'))
plc_db_read_delay=int(filedic.pop('plc_db_read_delay_in_milliseconds'))/1000
error_wait=int(filedic.pop('error_wait_in_milliseconds'))/1000
server_reconnect_delay=int(filedic.pop('server_reconnect_delay_in_milliseconds'))/1000
server_data_move_delay=int(filedic.pop('server_data_move_delay_in_milliseconds'))/1000
sct=int(filedic.pop('server_connect_time_in_seconds'))
print('MT: Settings file read')
unique_no=None

def server_data_move():
    global unique_no
    write_flag=False
    while True:
        try:
            if not server_queue.empty():
                soc_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                try:
                    soc_s.connect((ipaddress_of_server_system,port_of_server_system))
                except:
                    time.sleep(server_reconnect_delay)
                    continue
                data=server_queue.get()
                soc_s.sendall(data)
                un_in_bytes=soc_s.recv(1024)
                unique_no=int.from_bytes(un_in_bytes,'big')
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

def error_register():
    while True:
        err=error_register_queue.get()
        with open('readme.txt', 'a') as f:
            f.write(err)
        f.close()

def snap7_thread(ipaddress_of_plc,db_number,plc):
            global unique_no
            write_flag=False
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
                        connection_flag=True
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
                except Exception as e:
                    if str(e)=="b' TCP : Unreachable peer'":
                        print(f'ST{plc}: Unable to connect')
                        connection_flag=False
                    if str(e)=="b' ISO : An error occurred during send TCP : Connection reset by peer'":
                        print(f'ST{plc}: Disconnected')
                        connection_flag=False
                    if str(e)=="b' ISO : An error occurred during recv TCP : Connection timed out'":
                        print(f'ST{plc}: Unable  to connect')
                        connection_flag=False
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

for index,ip in enumerate(ipaddresses_of_plc):
    plc=filedic[ip]
    client_thread_pro = threading.Thread(target=snap7_thread,args=(ip,int(db_numbers_of_plc_respectively[index]),int(plc)),daemon=True)
    client_thread_pro.start()
    print(f'MT: Client_thread started {plc}')

server_data_mo = threading.Thread(target=server_data_move,daemon=True)
server_data_mo.start()
print(f'MT: Server_data_move thread started')
error_reg = threading.Thread(target=error_register,daemon=True)
error_reg.start()
print(f'MT: Error_register thread started')

while True:
    time.sleep(60)