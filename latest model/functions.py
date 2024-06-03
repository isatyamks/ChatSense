import re
from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import urlextract
import emoji
from wordcloud import WordCloud

# Function to generate DataFrame from file
def generateDataFrame(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    
    data = data.replace('\u202f', ' ')
    data = data.replace('\n', ' ')
    dt_format = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?(?:AM\s|PM\s|am\s|pm\s)?-\s'
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
    
    df = pd.DataFrame(list(zip(date, time, users, message)), columns=["Date", "Time(U)", "User", "Message"])
    return df

# Function to get unique users
def getUsers(df):
    users = df['User'].unique().tolist()
    users.sort()
    users.remove('Notifications')
    users.insert(0, 'Everyone')
    return users

# Function to preprocess the DataFrame
def PreProcess(df, dayfirst):
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=dayfirst)
    df['Time'] = pd.to_datetime(df['Time(U)']).dt.time
    df['year'] = df['Date'].apply(lambda x: int(str(x)[:4]))
    df['month'] = df['Date'].apply(lambda x: int(str(x)[5:7]))
    df['date'] = df['Date'].apply(lambda x: int(str(x)[8:10]))
    df['day'] = df['Date'].apply(lambda x: x.day_name())
    df['hour'] = df['Time'].apply(lambda x: int(str(x)[:2]))
    df['month_name'] = df['Date'].apply(lambda x: x.month_name())
    return df

# Function to get chat statistics
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
    
    return df, media_cnt, deleted_msgs_cnt, links_cnt, word_count, msg_count

# Function to get emoji analysis
def getEmoji(df):
    emojis = []
    for message in df['Message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    return pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

# Function to get monthly timeline
def getMonthlyTimeline(df):
    df.columns = df.columns.str.strip()
    df = df.reset_index()
    timeline = df.groupby(['year', 'month']).count()['Message'].reset_index()
    time = [str(timeline['month'][i]) + "-" + str(timeline['year'][i]) for i in range(timeline.shape[0])]
    timeline['time'] = time
    return timeline

# Function to get most common words
def MostCommonWords(df):
    with open('stop_hinglish.txt') as f:
        stop_words = f.read()
    
    words = []
    for message in df['Message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    return pd.DataFrame(Counter(words).most_common(20))

# Function to create daily timeline plot
def dailytimeline(df):
    df['taarek'] = df['Date']
    daily_timeline = df.groupby('taarek').count()['Message'].reset_index()
    fig, ax = plt.subplots()
    ax.plot(daily_timeline['taarek'], daily_timeline['Message'])
    ax.set_ylabel("Messages Sent")
    plt.title('Daily Timeline')
    plt.show()

# Function to create week activity plot
def WeekAct(df):
    x = df['day'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(x.index, x.values)
    ax.set_xlabel("Days")
    ax.set_ylabel("Message Sent")
    plt.xticks(rotation='vertical')
    plt.show()

# Function to create month activity plot
def MonthAct(df):
    x = df['month_name'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(x.index, x.values)
    ax.set_xlabel("Months")
    ax.set_ylabel("Message Sent")
    plt.xticks(rotation='vertical')
    plt.show()

# Function to create activity heatmap
def activity_heatmap(df):
    period = []
    for hour in df[['day', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period
    user_heatmap = df.pivot_table(index='day', columns='period', values='Message', aggfunc='count').fillna(0)
    return user_heatmap

# Function to create word cloud
def create_wordcloud(df):
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read()
    
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df['Message'] = df['Message'].apply(remove_stop_words)
    df_wc = wc.generate(df['Message'].str.cat(sep=" "))
    return df_wc

# Example usage of the functions
if __name__ == "__main__":
    file = 'path_to_your_file.txt'  # Replace with your file path
    df = generateDataFrame(file)
    dayfirst = True  # Set to True for 'dd-mm-yy' format, False for 'mm-dd-yy' format

    users = getUsers(df)
    selected_user = "Everyone"  # Set to a specific user if needed

    df = PreProcess(df, dayfirst)

    if selected_user != "Everyone":
        df = df[df['User'] == selected_user]

    df, media_cnt, deleted_msgs_cnt, links_cnt, word_count, msg_count = getStats(df)

    print("Chat Statistics")
    print(f"Total Messages: {msg_count}")
    print(f"Total Words: {word_count}")
    print(f"Media Shared: {media_cnt}")
    print(f"Links Shared: {links_cnt}")
    print(f"Messages Deleted: {deleted_msgs_cnt}")

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

    emojiDF = getEmoji(df)
    print("Emoji Analysis")
    print(emojiDF)

    plt.pie(emojiDF[1].head(), labels=emojiDF[0].head(), autopct="%0.2f", shadow=True)
    plt.legend()
    plt.show()

    commonWord = MostCommonWords(df)
    plt.bar(commonWord[0], commonWord[1])
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation='vertical')
    plt.title('Most Frequent Words Used In Chat')
    plt.show()

    timeline = getMonthlyTimeline(df)
    plt.plot(timeline['time'], timeline['Message'])
    plt.xlabel