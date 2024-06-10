import dataprocessor




#this is group chat data

#file = 'data_chats\_chat_group_data.txt'




#this is individual chat data

file = 'data_chats\_chat_2_data.txt'





df = dataprocessor.generateDataFrame(file)




#print(df.head())


#user statistics

dataprocessor.getStats(df)
# User Activity Count
dataprocessor.getUsers(df)

# Emoji Analysis - It will show the most used emoji with its frequencies
dataprocessor.getEmoji(df)
# Most used words
dataprocessor.MostCommonWords(df)
# Monthly Timeline
timeline = dataprocessor.getMonthlyTimeline(df)
# Daily Timeline
dataprocessor.dailytimeline(df)


# Most Busy Days
dataprocessor.WeekAct(df)

# Most Busy Months
dataprocessor.MonthAct(df)
# WordCloud
dataprocessor.create_wordcloud(df)

dataprocessor.activity_heatmap(df)



