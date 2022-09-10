# from aphyt import omron
# # from aphyt import omron
# # 
# eip_instance = omron.
# eip_instance.connect_explicit('192.168.250.13')
# import sys
# import time

# import fins.udp
# import time

# fins_instance = fins.udp.UDPFinsConnection()
# fins_instance.connect('192.168.250.30')
# # mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x00\x00')
# # print(mem_area)
# mem_area_dm_word = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,b'\x00\x06\x00')
# print(mem_area_dm_word)
# import time

import fins.udp,time

fins_instance1 = fins.udp.UDPFinsConnection()
fins_instance1.connect('192.168.250.30',9604,9600)
fins_instance1.dest_node_add=1
fins_instance1.srce_node_add=25
fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.250.30',9600,9601)
fins_instance.dest_node_add=1
fins_instance.srce_node_add=25
while True:

    mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,b'\x00\x00\x00',2)
    mem_area = fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,b'\x00\x07\x00',b'\x00\x09',1)
    mem_area1 = fins_instance1.memory_area_read(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,b'\x00\x01\x00',2)
    mem_area1 = fins_instance1.memory_area_write(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,b'\x00\x00\x00',b'\x00\x09',1)
    
    # mem_area[]
    if mem_area=='':
        print("Tine out 123")
    else:
        
        # print(mem_area[14:])
        count=int.from_bytes(mem_area[14:16],'big')
        unique_no=int.from_bytes(mem_area[16:18],'big')
        print("Data Received : ",mem_area, "count : ",count,"unique_no : ",unique_no)
    time.sleep(1)