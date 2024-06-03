import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns
import functions

# Load your data file
file = 'D:\whatsapp-chat-analysis\chat.txt'

# Generate DataFrame
df = functions.generateDataFrame(file)

# Choose date format
dayfirst = True  # Set to True for 'dd-mm-yy' format, False for 'mm-dd-yy' format

# Preprocess the DataFrame
df = functions.PreProcess(df, dayfirst)

# Get users
users = functions.getUsers(df)
selected_user = "Everyone"  # Set to a specific user if needed

# Filter for the selected user
if selected_user != "Everyone":
    df = df[df['User'] == selected_user]

# Get statistics
df, media_cnt, deleted_msgs_cnt, links_cnt, word_count, msg_count = functions.getStats(df)


stats_labels = ['Total Messages', 'Total Words', 'Media Shared', 'Links Shared', 'Messages Deleted']
stats_values = [msg_count, word_count, media_cnt, links_cnt, deleted_msgs_cnt]

plt.figure(figsize=(10, 6))
plt.bar(stats_labels, stats_values, color=['blue', 'green', 'orange', 'red', 'purple'])
plt.xlabel("Statistic")
plt.ylabel("Count")
plt.title("Chat Statistics")
plt.xticks(rotation=45)
plt.show()





# Emoji Analysis
emojiDF = functions.getEmoji(df)

plt.figure(figsize=(8, 8))
plt.pie(emojiDF[1].head(), labels=emojiDF[0].head(), autopct="%0.2f", shadow=True)
plt.legend()
plt.title("Emoji Analysis")
plt.show()



# Print Chat Statistics
print("Chat Statistics")
print(f"Total Messages: {msg_count}")
print(f"Total Words: {word_count}")
print(f"Media Shared: {media_cnt}")
print(f"Links Shared: {links_cnt}")
print(f"Messages Deleted: {deleted_msgs_cnt}")

# User Activity Count
if selected_user == 'Everyone':
    x = df['User'].value_counts().head()
    name = x.index
    count = x.values

    print("Messaging Frequency")
    print("Messaging Percentage Count of Users")
    print(round((df['User'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'User': 'name', 'count': 'percent'}))

    plt.bar(name, count)
    plt.xlabel("Users")
    plt.ylabel("Message Sent")
    plt.xticks(rotation='vertical')
    plt.show()

# Emoji Analysis
emojiDF = functions.getEmoji(df)
print("Emoji Analysis")
print(emojiDF)

plt.pie(emojiDF[1].head(), labels=emojiDF[0].head(), autopct="%0.2f", shadow=True)
plt.legend()
plt.show()

# Common Words
commonWord = functions.MostCommonWords(df)
plt.bar(commonWord[0], commonWord[1])
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation='vertical')
plt.title('Most Frequent Words Used In Chat')
plt.show()

# Monthly Timeline
timeline = functions.getMonthlyTimeline(df)
plt.plot(timeline['time'], timeline['Message'])
plt.xlabel("Month")
plt.ylabel("Messages Sent")
plt.xticks(rotation='vertical')
plt.title('Monthly Timeline')
plt.show()

# Daily Timeline
functions.dailytimeline(df)

# Weekly and Monthly Activity
print('Most Busy Days')
functions.WeekAct(df)
print('Most Busy Months')
functions.MonthAct(df)

# WordCloud
df_wc = functions.create_wordcloud(df)
plt.imshow(df_wc)
plt.title("Wordcloud")
plt.show()

# Weekly Activity Map
user_heatmap = functions.activity_heatmap(df)
sns.heatmap(user_heatmap)
plt.title("Weekly Activity Map")
plt.show()
