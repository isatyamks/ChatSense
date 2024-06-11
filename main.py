import dataprocessor




file = 'data_chats\_chat_4_data.txt'




df = dataprocessor.generateDataFrame(file)

# DataFrame 
# print(df.head())

# User ke statistics 
dataprocessor.getStats(df)

# User activity count 
dataprocessor.getUsers(df)

# Emoji analysis 
dataprocessor.getEmoji(df)

# Sabse zyada used words
dataprocessor.MostCommonWords(df)

# Monthly timeline 
timeline = dataprocessor.getMonthlyTimeline(df)


# # if selected_user != "Everyone":
#     x = df['User'].value_counts()  
#     name = x.index
#     count = x.values
#     plt.bar(name, count)
#     plt.xlabel("Users")
#     plt.ylabel("Message Sent")
#     plt.xticks(rotation='vertical')
#     plt.show()


# Daily timeline 
dataprocessor.dailytimeline(df)

# Sabse busy days 
dataprocessor.WeekAct(df)

# Sabse busy months 
dataprocessor.MonthAct(df)

# WordCloud  
dataprocessor.create_wordcloud(df)

# Activity heatmap 
dataprocessor.activity_heatmap(df)
