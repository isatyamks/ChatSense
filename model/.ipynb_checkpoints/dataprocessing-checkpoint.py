#importing some basic useful libraries......


import re
import pandas as pd


# fetching data from the chat.txt with the help of file handling in python....


f=open('chatdata.txt','r',encoding='utf-8')

data=f.read()



pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

messages = re.split(pattern, data)[1:]
messages


dates = re.findall(pattern, data)

dates
print(len(messages),len(dates))