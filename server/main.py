# -*- coding:utf-8 -*-

import sys
import importlib
# import imp
# imp.reload(sys)
# importlib.reload(sys)
# sys.setdefaultencoding("utf-8")

import time
import sched
import sqlite3
# from ..praser_youtube import tag_parser
# from . import praser_youtube
import praser_youtube.tag_youtube





hour=time.strftime("%H", time.localtime())
# if int(hour)%6 == 0:
if True:

    with open('praser_youtube.py', 'r',encoding='utf-8') as f:
        # 使用exec时，字符串中不要使用中文!!!
        exec(f.read())


    conn = sqlite3.connect('./data.db')
    c = conn.cursor()

    #search temp table
    temp_info=c.execute('''SELECT title,length,url,views,loaded_time from temp_video_list''')
    temp_info_title =[]
    temp_info_length =[]
    temp_info_url =[]
    temp_info_views =[]
    temp_info_loaded_time =[]
    temp_titl_and_url={}
    temp_titl_and_length = {}
    temp_titl_and_views = {}
    temp_titl_and_loaded_time = {}
    for row in temp_info:
        temp_info_title.append(row[0])
        temp_info_url.append(row[2])
        temp_titl_and_url[row[0]]=row[2]
        temp_titl_and_length[row[0]] = row[1]
        temp_titl_and_views[row[0]] = row[3]
        temp_titl_and_loaded_time[row[0]] = row[4]

        # print(temp_titl_and_url)
        # temp_info_length.append(row[1])
        # temp_info_views.append(row[3])
        # temp_info_loaded_time.append(row[4])


    #search main table
    c.execute('''CREATE TABLE  IF NOT EXISTS full_video_list
       (title      text    NOT NULL,
       length      text    NOT NULL,
       url         text    NOT NULL,
       views       int     NOT NULL,
       loaded_time text    NOT NULL);''')
    full_list_title=c.execute('''SELECT title from full_video_list''')
    full_list_title_list=[]
    for item in full_list_title:
        full_list_title_list.append(item[0])


    temp_download=[]
    for item in temp_info_title:
        if item not in full_list_title_list:
            full_list_title_list.append(item)
            temp_download.append(item)



    #create a table to save the real needed downloaded
    c.execute('''CREATE TABLE  IF NOT EXISTS temp_download_list
       (title      text    NOT NULL,
       url         text    NOT NULL);''')

    for title in temp_download:
        url=temp_titl_and_url[title]
        length=temp_titl_and_length[title]
        views=temp_titl_and_views[title]
        loaded_time=temp_titl_and_loaded_time[title]

        c.execute('''INSERT INTO temp_download_list (title,url) \
                      VALUES (?,?)''', (title,url))

        c.execute('''INSERT INTO full_video_list (title,length,url,views,loaded_time) \
              VALUES (?,?,?,?,?)''', (title,length,url,views,loaded_time))


    conn.commit()


    with open('pytube_main.py', 'r') as f:
        exec(f.read().encode('gb2312'))

    # with open('video-editor.py', 'rb') as f:
    #     exec(f.read())
# else:
#     time.sleep()



# if __name__=="__main__":
#     main()
