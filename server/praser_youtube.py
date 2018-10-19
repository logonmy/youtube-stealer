# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import time
#import datetime
import sqlite3
import requests


conn=sqlite3.connect('./data.db')
c=conn.cursor()
# if c.execute('''select * from sqlite_master where type='table' and name='temp_video_list' ''') is None:
c.execute('''CREATE TABLE  IF NOT EXISTS temp_video_list
       (title      text    NOT NULL,
       length      text    NOT NULL,
       url         text    NOT NULL,
       views       int     NOT NULL,
       loaded_time text    NOT NULL);''')


# mainpage of youtube channel
# channel_list={'Apple':'https://www.youtube.com/user/Apple/videos'}
#               # 'sony':'https://www.youtube.com/user/sonyelectronics/videos',
#               # 'xiaomiglobal':'https://www.youtube.com/user/XIAOMIGLOBAL/videos'}

channel_list = {}
with open('./channels.txt', 'r', encoding='utf-8') as f:
    for channel in f.readlines():
        if '#' not in channel:
            print(channel)
            channel_company = channel.split(';')[0]
            channel_content = channel.split(';')[1]
            print(channel_company,channel_content)
            channel_list[channel_company] = channel_content


def tag_parser(tag_group,attr):
    for tag in tag_group:
        return tag[attr]

for company,channel_url in zip(channel_list.keys(),channel_list.values()):
    # print(channel_url)
    #html=request.urlopen(channel_url)
    #!!!!!!!!!!!inorder to protect information youtube returned webpage was differnt to the browser!!!!!!!!
    html=requests.get(channel_url).content
    # f=open('html.html',mode='wb')
    # f.write(html)

    # using function open encoding parameter to avoid beautifulsoup decode error
    #soup = BeautifulSoup(open(html, encoding='utf-8'), 'html5lib')
    soup = BeautifulSoup(html , 'html.parser')

    # url_group=soup.find_all("a", attrs={'class':'yt-uix-sessionlink','aria-hidden':'true'})
    titles_and_urls=soup.find_all('a',attrs={'dir':'ltr','rel':'nofollow'})
    views_group = soup.find_all('ul',attrs={'class':'yt-lockup-meta-info'})
    length_group = soup.find_all('span',attrs={'class':'video-time'})
    # delay_group=soup.find_all('')        #no info on the webpage

    # print(titles_and_urls,views_group,length_group)

    #
    for num in range(0,5):
        title_and_url=titles_and_urls[num]
        title=title_and_url['title']
        url='https://www.youtube.com'+title_and_url['href']
        views=views_group[num].li.get_text().split(' ')[0].replace(',','')
        length=length_group[num].get_text()
        if int(length.split(':')[-2])>10:
            continue
        # time_delay=time_delay_group[num]

        loaded_time=str(time.time()).split('.')[0]
        # # c.execute('''INSERT INTO COMPANY (title,length,url,save_time) \
        # #       VALUES ('%s','%s','%s','%s')''',%title,%length,%url,%save_time);

        print( title , length , url , views , loaded_time )

        conn.text_factory=str
        title_record=c.execute('''SELECT title from temp_video_list''')
        # print((title_record.fetchone()[0]))

        title_record_list = []
        for title_item in title_record:
            title_item_string=str(title_item[0])# !!!using [0] to get text object
            title_record_list.append(title_item_string)

        # !!!!!!!!!!!!!!!error!!!!!!!!!!!!!!
        # !!!!!!!!!because title_record no item,title_record_list define do not execute
        # for title_item in title_record:
        #     title_item_string = str(title_item[0])  # !!!using [0] to get text object
        #     title_record_list = []
        #     title_record_list.append(title_item_string)
        # if title not in title_record_list:          #because title_record no item,title_record_list define do not execute
        #     print('111')


        if title not in title_record_list:
            print('good jop.')
            c.execute('''INSERT INTO temp_video_list (title,length,url,views,loaded_time) \
                  VALUES (?,?,?,?,?)''',(str(title),str(length),url,int(views),loaded_time))


        conn.commit()

#get system time,to compared with uploaded video time
#current_time=str(datetime.datetime.now())

# second=time.strftime("%S", time.localtime())
# minute=time.strftime("%M", time.localtime())
# hour=time.strftime("%H", time.localtime())


