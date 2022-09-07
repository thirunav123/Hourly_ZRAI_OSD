import os,sys,time,threading,queue,socket,psutil,snap7,fins.udp
from aphyt import omron

name_list=os.path.basename(__file__).split('.')
name_list[-1]="exe"
exe_name=".".join(name_list)
print(exe_name)
process_count=0
for p in psutil.process_iter():
    # print(p.name())
    if p.name()==exe_name:
        process_count=process_count+1
        # print
    if process_count>2:
        print(process_count)
        print("Already execution file ran")
        sys.exit()       

lock=threading.Lock()
file=open('client_settings.txt','r')
print('MT: I am a Client')
filedic={}

for line in file:
    file_data=line.strip().split('===')
    a=file_data[0]
    b=file_data[1]
    filedic[a]=b

ipaddress_of_server_system=filedic.pop('ipaddress_of_server_system')
port_of_server_system=int(filedic.pop('port_of_server_system'))
ipaddresses_of_siemens_plc=filedic.pop('ipaddresses_of_siemens_plc').split(',')
db_numbers_of_siemens_plc_respectively=filedic.pop('data_block_numbers_of_siemens_plc_respectively').split(',')
rack_numbers_of_siemens_plc_respectively=filedic.pop('rack_numbers_of_siemens_plc_respectively').split(',')
slot_numbers_of_siemens_plc_respectively=filedic.pop('slot_numbers_of_siemens_plc_respectively').split(',')
siemens_plc_db_read_delay=int(filedic.pop('siemens_plc_db_read_delay_in_milliseconds'))/1000
omron_CS_or_CJ_or_CP_plc_data_read_delay=int(filedic.pop('omron_CS_or_CJ_or_CP_plc_data_read_delay_in_milliseconds'))/1000
ipaddresses_of_omron_CS_or_CJ_or_CP_plc=filedic.pop('ipaddresses_of_omron_CS_or_CJ_or_CP_plc').split(',')
addresses_of_count_of_omron_CS_or_CJ_or_CP_plc_respectively=filedic.pop('addresses_of_count_of_omron_CS_or_CJ_or_CP_plc_respectively').split(',')
addresses_of_unique_no_of_omron_CS_or_CJ_or_CP_plc_respectively=filedic.pop('addresses_of_unique_no_of_omron_CS_or_CJ_or_CP_plc_respectively').split(',')
ipaddresses_of_omron_NX_Series_plc=filedic.pop('ipaddresses_of_omron_NX_Series_plc').split(',')
count_variable_name_of_omron_NX_Series_plc_respectively=filedic.pop('count_variable_name_of_omron_NX_Series_plc_respectively').split(',')
unique_no_variable_name_of_omron_NX_Series_plc_respectively=filedic.pop('unique_no_variable_name_of_omron_NX_Series_plc_respectively').split(',')
omron_NX_Series_plc_data_read_delay=int(filedic.pop('omron_NX_Series_plc_data_read_delay_in_milliseconds'))/1000
error_wait=int(filedic.pop('error_wait_in_milliseconds'))/1000
server_reconnect_delay=int(filedic.pop('server_reconnect_delay_in_milliseconds'))/1000
server_data_move_delay=int(filedic.pop('server_data_move_delay_in_milliseconds'))/1000
max_size_server_queue=int(filedic.pop('maximum_size_server_queue'))
print('MT: Settings file read')
server_queue=queue.Queue(maxsize=max_size_server_queue)
error_register_queue=queue.Queue()
unique_no=None

def server_data_move():
    global unique_no
    write_flag=False
    while True:
        try:
            if not server_queue.empty():
                try:
                    soc_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    soc_s.connect((ipaddress_of_server_system,port_of_server_system))
                except:
                    time.sleep(server_reconnect_delay)
                    print('SDM: Reconnecting to Server')
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

def siemens_snap7_thread(ipaddress_of_plc,db_number,rack,slot,plc):
            global unique_no
            write_flag=False
            connection_flag=False
            alive_flag=True
            alive=alive_flag.to_bytes(1,'big')
            plc_in_bytes=plc.to_bytes(1,'big')
            pc=0
            while True:
                try:
                    if not connection_flag:
                        client=snap7.client.Client()
                        client.connect(ipaddress_of_plc,rack,slot)
                        # client.connect(ipaddress_of_plc,0,1,102)
                        connection_flag=True
                    data=client.db_read(db_number,0,6)
                    cc=int.from_bytes(data[4:6],'big')
                    if not unique_no is None:
                        if not unique_no==int.from_bytes(data[2:4],'big'):
                            reset=0
                            byte_data=unique_no.to_bytes(2,'big')+reset.to_bytes(2,'big')
                            client.db_write(db_number,2,byte_data)
                            print(f'SST{plc}: Count Reset')
                    if not pc==cc:
                        server_data=plc_in_bytes+data[4:6]
                        if server_queue.full():
                            server_queue.get()
                        server_queue.put(server_data)
                        pc=cc
                    else:
                        temp=65534
                        server_data=plc_in_bytes+temp.to_bytes(2,'big')
                        if server_queue.full():
                            server_queue.get()
                        server_queue.put(server_data)
                    print(f'SST{plc}: Production Count = {cc}')
                    client.db_write(db_number,0,alive)
                    time.sleep(siemens_plc_db_read_delay)
                    write_flag=False
                except Exception as e:
                    if str(e)=="b' TCP : Unreachable peer'":
                        print(f'SST{plc}: Unable to connect')
                        connection_flag=False
                    if str(e)=="b' ISO : An error occurred during send TCP : Connection reset by peer'":
                        print(f'SST{plc}: Disconnected')
                        connection_flag=False
                    if str(e)=="b' ISO : An error occurred during recv TCP : Connection timed out'":
                        print(f'SST{plc}: Unable  to connect')
                        connection_flag=False
                    if not write_flag:
                        error_register_queue.put(f'SST{plc}: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
                        if str(e)=="b' TCP : Unreachable peer'" or str(e)=="b' ISO : An error occurred during send TCP : Connection reset by peer'" or str(e)=="b' ISO : An error occurred during recv TCP : Connection timed out'":
                            off_no=65535
                            server_data=plc_in_bytes+off_no.to_bytes(2,'big')
                            if server_queue.full():
                                server_queue.get()
                            server_queue.put(server_data)
                            print(f'SST{plc}: Machine OFF')
                        write_flag=True
                        print(f'SST{plc}: Error acquired and recorded. Error: {e}')
                    else: 
                        print(f'SST{plc}: Error acquired and already recorded. Error: {e}')
                    time.sleep(error_wait)

def omron_CS_or_CJ_or_CP_fins_thread(ip,count_address,unique_no_address,plc):
    global unique_no
    write_flag=False
    fins_instance = fins.udp.UDPFinsConnection()
    fins_instance.connect(ip,9600,0)
    fins_instance.dest_node_add=1
    fins_instance.srce_node_add=25
    cd=count_address.to_bytes(2,'big')+b'\x00'
    ud=unique_no_address.to_bytes(2,'big')+b'\x00'
    plc_in_bytes=plc.to_bytes(1,'big')
    pc=0
    while True:
            count_mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,cd)
            unique_no_mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,ud)
            if not (count_mem_area=='' or unique_no_mem_area==''):
                cc=int.from_bytes(count_mem_area[14:],'big')
                if not unique_no is None:
                    if not unique_no==int.from_bytes(unique_no_mem_area[14:],'big'):
                        reset=0
                        un_byte_data=unique_no.to_bytes(2,'big')
                        c_byte_data=reset.to_bytes(2,'big')
                        fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,cd,c_byte_data,1)
                        fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,ud,un_byte_data,1)
                        print(f'OFCT{plc}: Count Reset')
                if not pc==cc:
                    server_data=plc_in_bytes+count_mem_area[14:]
                    if server_queue.full():
                        server_queue.get()
                    server_queue.put(server_data)
                    pc=cc
                else:
                    temp=65534
                    server_data=plc_in_bytes+temp.to_bytes(2,'big')
                    if server_queue.full():
                        server_queue.get()
                    server_queue.put(server_data)
                    print(f'OFCT{plc}: Production Count = {cc}')
                    write_flag=False
            else:
                if not write_flag:
                    error_register_queue.put(f'OFCT{plc}: timed_out  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
                    off_no=65535
                    server_data=plc_in_bytes+off_no.to_bytes(2,'big')
                    if server_queue.full():
                        server_queue.get()
                    server_queue.put(server_data)
                    print(f'OFCT{plc}: Machine OFF or Unable to connect')
                    write_flag=True
                    print(f'OFCT{plc}: Error acquired and recorded. Error: timed_out')
                else: 
                    print(f'OFCT{plc}: Error acquired and already recorded. Error: timed_out')
                time.sleep(error_wait)
            # client.db_write(db_number,0,alive)
            time.sleep(omron_CS_or_CJ_or_CP_plc_data_read_delay)
        
def omron_NX_Series_aphyt_thread(ip,count_name,unique_no_name,plc):
    global unique_no
    connection_flag=False
    write_flag=False
    plc_in_bytes=plc.to_bytes(1,'big')
    pc=0
    while True:
        try:
            if not connection_flag:
                eip_instance = omron.n_series.NSeries()
                eip_instance.connect_explicit(ip)
                eip_instance.register_session()
                eip_instance.update_variable_dictionary()
                connection_flag=True
            cc = eip_instance.read_variable(count_name)
            un = eip_instance.read_variable(unique_no_name)
            if not unique_no is None:
                if not unique_no==un:
                    reset=0
                    eip_instance.write_variable(count_name,reset)
                    eip_instance.write_variable(unique_no_name,unique_no)
                    print(f'OFNT{plc}: Count Reset')
            if not pc==cc or cc==0:
                server_data=plc_in_bytes+cc.to_bytes(2,'big')
                if server_queue.full():
                    server_queue.get()
                server_queue.put(server_data)
                pc=cc
            else:
                temp=65534
                server_data=plc_in_bytes+temp.to_bytes(2,'big')
                if server_queue.full():
                    server_queue.get()
                server_queue.put(server_data)
                print(f'OFNT{plc}: Production Count = {cc}')
            time.sleep(omron_NX_Series_plc_data_read_delay)
            write_flag=False
        except Exception as e:
            connection_flag=False
            eip_instance.close_explicit()
            if not write_flag:
                error_register_queue.put(f'OFNT{plc}: {e}  {time.strftime("%d-%m-%Y_%I.%M.%S_%p")}\n')
                off_no=65535
                server_data=plc_in_bytes+off_no.to_bytes(2,'big')
                if server_queue.full():
                    server_queue.get()
                server_queue.put(server_data)
                print(f'OFNT{plc}: Machine OFF or Unable to connect')
                write_flag=True
                print(f'OFNT{plc}: Error acquired and recorded. Error: {e}')
            else: 
                print(f'OFNT{plc}: Error acquired and already recorded. Error: {e}')
            time.sleep(error_wait)


if not ipaddresses_of_siemens_plc==['']:    
    for index,ip in enumerate(ipaddresses_of_siemens_plc):
        plc=filedic[ip+'.'+db_numbers_of_siemens_plc_respectively[index]]
        client_thread_pro = threading.Thread(target=siemens_snap7_thread,args=(ip,int(db_numbers_of_siemens_plc_respectively[index]),int(rack_numbers_of_siemens_plc_respectively[index]),int(slot_numbers_of_siemens_plc_respectively[index]),int(plc)),daemon=True)
        client_thread_pro.start()
        print(f'MT: Siemens_snap7_thread started {plc}')
else:
    print(f'MT: No Siemens_snap7_thread started')

if not ipaddresses_of_omron_CS_or_CJ_or_CP_plc==['']:
    for index,ip in enumerate(ipaddresses_of_omron_CS_or_CJ_or_CP_plc):
        plc=filedic[ip+'.'+addresses_of_count_of_omron_CS_or_CJ_or_CP_plc_respectively[index]]
        client_thread_pro = threading.Thread(target=omron_CS_or_CJ_or_CP_fins_thread,args=(ip,int(addresses_of_count_of_omron_CS_or_CJ_or_CP_plc_respectively[index]),int(addresses_of_unique_no_of_omron_CS_or_CJ_or_CP_plc_respectively[index]),int(plc)),daemon=True)
        client_thread_pro.start()
        print(f'MT: Omron_CS_or_CJ_or_CP_fins_thread started {plc}')
else:
        print(f'MT: No Omron_CS_or_CJ_or_CP_fins_thread started')

if not ipaddresses_of_omron_NX_Series_plc==['']:
    for index,ip in enumerate(ipaddresses_of_omron_NX_Series_plc):
        plc=filedic[ip+'.'+count_variable_name_of_omron_NX_Series_plc_respectively[index]]
        client_thread_pro = threading.Thread(target=omron_NX_Series_aphyt_thread,args=(ip,count_variable_name_of_omron_NX_Series_plc_respectively[index],unique_no_variable_name_of_omron_NX_Series_plc_respectively[index],int(plc)),daemon=True)
        client_thread_pro.start()
        print(f'MT: Omron_NX_Series_aphyt_thread started {plc}')
else:
        print(f'MT: No Omron_NX_Series_aphyt_thread started')

server_data_mo = threading.Thread(target=server_data_move,daemon=True)
server_data_mo.start()
print(f'MT: Server_data_move thread started')
error_reg = threading.Thread(target=error_register,daemon=True)
error_reg.start()
print(f'MT: Error_register thread started')

while True:
    time.sleep(60)