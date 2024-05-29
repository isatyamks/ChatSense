#importing some basic useful libraries......


import re
import pandas as pd


# fetching data from the chat.txt with the help of file handling in python....


f=open('chatdata.txt','r',encoding='utf-8')

data=f.read()


pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'




#give the pattern and data to the re module to find the pattern in the data.....

message = re.split(pattern, data)[1:]


#print the message now

message
