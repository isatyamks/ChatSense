import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns
import functions


# Load your data file
file = 'b10chat.txt'

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


if selected_user == 'Everyone':
    x = df['User'].value_counts()  
    name = x.index
    count = x.values

    
    plt.bar(name, count)
    plt.xlabel("Users")
    plt.ylabel("Message Sent")
    plt.xticks(rotation='vertical')
    plt.show()

# Emoji Analysis
emojiDF = functions.getEmoji(df)


plt.pie(emojiDF[1].head(), labels=emojiDF[0].head(), autopct="%0.2f", shadow=True)
plt.legend()
plt.show()


emoji_unicode = emojiDF[0].head()
counts = emojiDF[1].head()

# Create a bar plot
plt.bar(range(len(emoji_unicode)), counts, align='center', alpha=0.7)
plt.xticks(range(len(emoji_unicode)), emoji_unicode, rotation='vertical')

plt.xlabel('Emoji')
plt.ylabel('Count')
plt.title('Emoji Counts')

plt.show()






# # Common Words
# commonWord = functions.MostCommonWords(df)
# plt.bar(commonWord[0], commonWord[1])
# plt.xlabel("Words")
# plt.ylabel("Frequency")
# plt.xticks(rotation='vertical')
# plt.title('Most Frequent Words Used In Chat ' )
# plt.show()

# # Monthly Timeline
# timeline = functions.getMonthlyTimeline(df)
# plt.plot(timeline['time'], timeline['Message'])
# plt.xlabel("Month")
# plt.ylabel("Messages Sent")
# plt.xticks(rotation='vertical')
# plt.title('Monthly Timeline')
# plt.show()

# # Daily Timeline
# functions.dailytimeline(df)

# # Weekly and Monthly Activity
# print('Most Busy Days')
# functions.WeekAct(df)
# print('Most Busy Months')
# functions.MonthAct(df)

# # WordCloud
# df_wc = functions.create_wordcloud(df)
# plt.imshow(df_wc)
# plt.title("Wordcloud")
# plt.show()

# # Weekly Activity Map
# user_heatmap = functions.activity_heatmap(df)
# sns.heatmap(user_heatmap)
# plt.title("Weekly Activity Map")
# plt.show()
