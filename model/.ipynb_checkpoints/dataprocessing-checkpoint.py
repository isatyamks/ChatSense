<<<<<<< HEAD
#importing some basic useful libraries......


=======
>>>>>>> d12373bdda13b05bd417aa606f60bb2926def8ab
import re
import pandas as pd


<<<<<<< HEAD
# fetching data from the chat.txt with the help of file handling in python....


f=open('chatdata.txt','r',encoding='utf-8')

data=f.read()



pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

messages = re.split(pattern, data)[1:]
messages


dates = re.findall(pattern, data)

dates
print(len(messages),len(dates))
=======
f=open('chatdata.txt','r',encoding='utf-8')
data =f.read()
#print(data)

pattern = r'\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}\u202F[ap]m - '

messages = re.split(pattern,data)[1:]



messages




dates =re.findall(pattern,data)
#dates
df = pd.DataFrame({'user_message': messages, 'message_date': dates})
df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M\u202F%p - ')

df.rename(columns={'message_date': 'date'}, inplace=True)
df.head()
df.shape
>>>>>>> d12373bdda13b05bd417aa606f60bb2926def8ab
