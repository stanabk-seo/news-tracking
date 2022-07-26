import feedparser
import pandas as pd
import streamlit as st

st.title("News Tracking System")

feed_list = ['https://www.google.com/alerts/feeds/00792317380303969091/2929705248926595588','https://www.google.com/alerts/feeds/00792317380303969091/15884301842139880462','https://www.google.com/alerts/feeds/00792317380303969091/15884301842139880048','https://www.google.com/alerts/feeds/00792317380303969091/4674860433124049255','https://www.google.com/alerts/feeds/00792317380303969091/15884301842139879516','https://www.google.com/alerts/feeds/00792317380303969091/15884301842139879399','https://www.google.com/alerts/feeds/00792317380303969091/15884301842139877561','https://www.google.com/alerts/feeds/00792317380303969091/13893430399699051728','https://www.google.com/alerts/feeds/00792317380303969091/1760640052522458223','https://www.google.com/alerts/feeds/00792317380303969091/1760640052522459009']

topic_menu = ['All','Fruit market news','vegetable market news','food market news','cotton market news','nuts market news','oil market news','pulses market news','rice market news','lemon market news','onion market news']
# print(feed_list)
# print(type(feed_list))

user_input = st.selectbox('Choose Any One Topic:', topic_menu)

news_title = []
news_link = []
news_date = []
news_topic = []

k = 1

for i in feed_list:
    newsfeed = feedparser.parse(i)
    try:
        for j in range(0,20):
            # print(newsfeed.entries[j].title)
            entry = newsfeed.entries[j]
            news_title.append(entry.title)
            news_link.append(entry.link)
            news_date.append(entry.date)
            news_topic.append(topic_menu[k])
    except:
        news_title.append('No News')
        news_link.append('No News')
        news_date.append('No News')
        news_topic.append('No News')
    k = k + 1    


news_df = pd.DataFrame(list(zip(news_topic, news_title, news_link, news_date)),  columns=['Topic','Title','Link','Date'])

filtered_df = news_df[news_df['Topic'] == user_input]

if user_input == 'All':
    print(news_df)
    st.write(news_df)
    csv2 = news_df.to_csv(index=False)
    st.download_button('Download CSV', csv2, 'news1.csv', 'text/csv')
else:
    print(filtered_df)
    st.write(filtered_df)
    csv1 = filtered_df.to_csv(index=False)
    st.download_button('Download CSV', csv1, 'news.csv', 'text/csv')


