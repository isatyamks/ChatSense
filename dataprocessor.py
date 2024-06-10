import re
from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import urlextract
import emoji
from wordcloud import WordCloud

# File se DataFrame generate karne ka function
def generateDataFrame(file):
    # File ko read karna
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    
    # Unnecessary spaces ko replace karna
    data = data.replace('\u202f', ' ')
    data = data.replace('\n', ' ')
    
    # Date-time format define karna
    dt_format = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?(?:AM\s|PM\s|am\s|pm\s)?-\s'
    
    # Messages aur date-times ko alag karna
    msgs = re.split(dt_format, data)[1:]
    date_times = re.findall(dt_format, data)
    
    date, time = [], []
    for dt in date_times:
        date.append(re.search(r'\d{1,2}/\d{1,2}/\d{2,4}', dt).group())
        time.append(re.search(r'\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)?', dt).group())
    
    users, message = [], []
    for m in msgs:
        s = re.split(r'([\w\W]+?):\s', m)
        if len(s) < 3:
            users.append("Notifications")
            message.append(s[0])
        else:
            users.append(s[1])
            message.append(s[2])
    
    # DataFrame create karna
    df = pd.DataFrame(list(zip(date, time, users, message)), columns=["Date", "Time(U)", "User", "Message"])
    
    # Date aur time ko appropriate format mein convert karna
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Time(U)']).dt.time
    
    # Additional columns add karna
    df['year'] = df['Date'].apply(lambda x: int(str(x)[:4]))
    df['month'] = df['Date'].apply(lambda x: int(str(x)[5:7]))
    df['date'] = df['Date'].apply(lambda x: int(str(x)[8:10]))
    df['day'] = df['Date'].apply(lambda x: x.day_name())
    df['hour'] = df['Time'].apply(lambda x: int(str(x)[:2]))
    df['month_name'] = df['Date'].apply(lambda x: x.month_name())
    
    return df

# Unique users ko retrieve karne ka function
def getUsers(df):
    users = df['User'].unique().tolist()
    users.sort()
    
    if 'Notifications' in users:
        users.remove('Notifications')
    
    users.insert(0, 'Everyone')
    
    # User activity count plot karna
    x = df['User'].value_counts()  
    name = x.index
    count = x.values
    
    plt.bar(name, count)
    plt.xlabel("Users")
    plt.ylabel("Message Sent")
    plt.xticks(rotation='vertical')
    plt.show()

# Chat statistics ko retrieve karne ka function
def getStats(df):
    media = df[df['Message'] == "<Media omitted> "]
    media_cnt = media.shape[0]
    df.drop(media.index, inplace=True)
    
    deleted_msgs = df[df['Message'] == "This message was deleted "]
    deleted_msgs_cnt = deleted_msgs.shape[0]
    df.drop(deleted_msgs.index, inplace=True)
    
    temp = df[df['User'] == 'Notifications']
    df.drop(temp.index, inplace=True)
    
    extractor = urlextract.URLExtract()
    links = []
    for msg in df['Message']:
        x = extractor.find_urls(msg)
        if x:
            links.extend(x)
    links_cnt = len(links)
    
    word_list = []
    for msg in df['Message']:
        word_list.extend(msg.split())
    word_count = len(word_list)
    msg_count = df.shape[0]
    
    # Statistics ko plot karna
    stats_labels = ['Total Messages', 'Total Words', 'Media Shared', 'Links Shared', 'Messages Deleted']
    stats_values = [msg_count, word_count, media_cnt, links_cnt, deleted_msgs_cnt]

    plt.figure(figsize=(10, 6))
    plt.bar(stats_labels, stats_values, color=['blue', 'green', 'orange', 'red', 'purple'])
    plt.xlabel("Statistic")
    plt.ylabel("Count")
    plt.title("Chat Statistics")
    plt.xticks(rotation=45)
    plt.show()

# Emoji analysis karne ka function
def getEmoji(df):
    emojis = []
    for message in df['Message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    
    emojiDF = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    plt.title('Emoji Analysis')
    print("Emoji Analysis")
    print(emojiDF)

    plt.pie(emojiDF[1].head(), labels=emojiDF[0].head(), autopct="%0.2f", shadow=True)
    plt.legend()
    plt.show()

# Most common words retrieve karne ka function
def MostCommonWords(df):
    with open('miscellaneous files\stop_hinglish.txt') as f:
        stop_words = f.read().splitlines()

    words = []
    for message in df['Message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    commonWord = pd.DataFrame(Counter(words).most_common(20))

    plt.bar(commonWord[0], commonWord[1])
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation='vertical')
    plt.title('Most Frequent Words Used In Chat')
    plt.show()

# Monthly timeline retrieve karne ka function
def getMonthlyTimeline(df):
    df.columns = df.columns.str.strip()
    df = df.reset_index()
    
    timeline = df.groupby(['year', 'month']).count()['Message'].reset_index()
    time = [str(timeline['month'][i]) + "-" + str(timeline['year'][i]) for i in range(timeline.shape[0])]
    timeline['time'] = time
    
    plt.plot(timeline['time'], timeline['Message'])
    plt.xlabel("Month")
    plt.ylabel("Messages Sent")
    plt.xticks(rotation='vertical')
    plt.title('Monthly Timeline')
    plt.show()
    
    return timeline

# Daily timeline plot create karne ka function
def dailytimeline(df):
    df['taarek'] = df['Date']
    daily_timeline = df.groupby('taarek').count()['Message'].reset_index()
    
    fig, ax = plt.subplots()
    ax.plot(daily_timeline['taarek'], daily_timeline['Message'])
    ax.set_ylabel("Messages Sent")
    plt.title('Daily Timeline')
    plt.show()

# Week activity plot create karne ka function
def WeekAct(df):
    x = df['day'].value_counts()
    
    fig, ax = plt.subplots()
    ax.bar(x.index, x.values)
    ax.set_xlabel("Days")
    ax.set_ylabel("Message Sent")
    plt.xticks(rotation='vertical')
    plt.show()

# Month activity plot create karne ka function
def MonthAct(df):
    x = df['month_name'].value_counts()
    
    fig, ax = plt.subplots()
    ax.bar(x.index, x.values)
    ax.set_xlabel("Months")
    ax.set_ylabel("Message Sent")
    plt.xticks(rotation='vertical')
    plt.show()

# Wordcloud create karne ka function
def create_wordcloud(df):
    with open('miscellaneous files\stop_hinglish.txt', 'r') as f:
        stop_words = f.read().splitlines()

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    df['Filtered_Message'] = df['Message'].apply(remove_stop_words)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(df['Filtered_Message'].str.cat(sep=" "))

    plt.imshow(df_wc, interpolation='bilinear')
    plt.axis('off')  
    plt.title("Wordcloud")
    plt.show()

# Activity heatmap create karne ka function
def activity_heatmap(df):
    period = []
    for hour in df[['day', 'hour']]['hour']:
        if hour == 0:
            period.append('12 AM - 1 AM')
        elif hour == 12:
            period.append('12 PM - 1 PM')
        elif hour < 12:
            period.append(f'{hour} AM - {hour + 1} AM')
        else:
            period.append(f'{hour - 12} PM - {hour - 11} PM')

    df['period'] = period
    
    user_heatmap = df.pivot_table(index='day', columns='period', values='Message', aggfunc='count').fillna(0)
    sns.heatmap(user_heatmap)
    plt.title("Weekly Activity Map")
    plt.show()
