#importing some basic useful libraries......


import re
import pandas as pd


# fetching data from the chat.txt with the help of file handling in python....


f=open('chatdata.txt','r',encoding='utf-8')

data=f.read()


<<<<<<< HEAD


pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

messages = re.split(pattern, data)[1:]


messages



dates = re.findall(pattern, data)
=======
pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'


>>>>>>> d12373bdda13b05bd417aa606f60bb2926def8ab


#give the pattern and data to the re module to find the pattern in the data.....

message = re.split(pattern, data)[1:]


#print the message now

message
