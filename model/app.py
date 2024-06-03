import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns
import dataprocessor

# Load your data file
# file = 'D:\whatsapp-chat-analysis\chat.txt'
file = 'b10chat.txt'
# Generate DataFrame
df = dataprocessor.generateDataFrame(file)

# # Choose date format
dayfirst = True  # Set to True for 'dd-mm-yy' format, False for 'mm-dd-yy' format



















# Preprocess the DataFrame
df = dataprocessor.PreProcess(df,dayfirst)

















# Get statistics

dataprocessor.getStats(df)




# User Activity Count

dataprocessor.getUsers(df)



# Emoji Analysis ---> It will show the most used emoji with its frequencies

dataprocessor.getEmoji(df)


# Most used words

dataprocessor.MostCommonWords(df)

# Monthly Timeline
timeline = dataprocessor.getMonthlyTimeline(df)


# Daily Timeline
dataprocessor.dailytimeline(df)



# print('Most Busy Days')
dataprocessor.WeekAct(df)


# print('Most Busy Months')
dataprocessor.MonthAct(df)



# WordCloud
dataprocessor.create_wordcloud(df)


# Weekly Activity Map

dataprocessor.activity_heatmap(df)