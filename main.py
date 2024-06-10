import dataprocessor

# Yeh group chat data ka file path hai
#file = 'data_chats\kaggle_api_data.txt'

# Yeh individual chat data ka file path hai
file = 'data_chats\_chat_2_data.txt'

# Chat data ko DataFrame mein convert karna
df = dataprocessor.generateDataFrame(file)

# DataFrame ke pehle kuch rows dekhne ke liye (commented out)
# print(df.head())

# User ke statistics nikalne kaa function call
dataprocessor.getStats(df)

# User activity count nikalne kaa function call
dataprocessor.getUsers(df)

# Emoji analysis - sabse zyada use hone wale emoji aur unki frequency dekhne ke liye funcall
dataprocessor.getEmoji(df)

# Sabse zyada use hone wale words nikalne ka  function call
dataprocessor.MostCommonWords(df)

# Monthly timeline nikalna
timeline = dataprocessor.getMonthlyTimeline(df)

# Daily timeline nikalne ka call
dataprocessor.dailytimeline(df)

# Sabse busy days nikalne call
dataprocessor.WeekAct(df)

# Sabse busy months nikalne funcall
dataprocessor.MonthAct(df)

# WordCloud  ka fun call
dataprocessor.create_wordcloud(df)

# Activity heatmap  kaa fun call
dataprocessor.activity_heatmap(df)
