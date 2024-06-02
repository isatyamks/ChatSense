import re
import pandas as pd


f=open('chat.txt','r',encoding='utf-8')
data =f.read()
#print(data)

pattern = r'\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}\u202F[ap]m - '

messages = re.split(pattern,data)[1:]



#print(messages)




dates =re.findall(pattern,data)
# print(dates)
df = pd.DataFrame({'user_message': messages, 'message_date': dates})
df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M\u202F%p - ')

df.rename(columns={'message_date': 'date'}, inplace=True)

print(df.head())
#print(df.shape)
