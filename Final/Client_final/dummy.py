import queue,requests,json
h_chat_queue=queue.Queue()
mfg_space_url="https://chat.googleapis.com/v1/spaces/AAAAiv8Wo8o/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=B3XrZpw5XjaY7LWqAFB6-ap30QuXNl7Haehs5hnIFgE%3D"
h_chat_queue.put([1,"23:00-33:00",983,9000])
plc,h,pq,it=h_chat_queue.get()
line_color="#40E0D0"
line="ASSDD"
date="dd/mm/yyyy"
shift="S"
temp_data = f'<i><b><font color=\"{line_color}">Hourly Intimation!</b></i>\n'\
                        f'<b><font color=\"{line_color}">Production Line &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : {line}</b>\n'\
                        f'<b><font color=\"{line_color}">Date and Shift &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : {date} {shift}</b>\n'\
                        f'<b><font color=\"{line_color}">Hour Time &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : {h}</b>\n'\
                        f'<b><font color=\"{line_color}">Prodution Quantity &nbsp;&nbsp; : {pq}</b>\n'\
                        f'<b><font color=\"{line_color}">Machine Idle in mins : {round(it/60)}</b>\n'
data_dir = {"cards": [{"sections":[{"widgets":[{"textParagraph":{ 'text':f'{temp_data}'}}]}]}]}#,
r = requests.post(mfg_space_url, data=json.dumps(data_dir))