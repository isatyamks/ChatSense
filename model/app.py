import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns
import dataprocessor

# Load your data file
file = 'b10chat.txt'






# Generate DataFrame
df = dataprocessor.generateDataFrame(file)







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

# Weekly Activity Map
dataprocessor.activity_heatmap(df)