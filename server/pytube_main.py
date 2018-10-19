# -*- coding:utf-8 -*-

import os
import sqlite3

from pytube import YouTube

conn = sqlite3.connect(r'./data.db')
c = conn.cursor()
cursor=c.execute('''SELECT title,url from temp_download_list''')


download_url_list=[]
download_title_list=[]
for row in cursor:
    download_title_list.append(row[0])
    download_url_list.append(row[1])

# print(download_url_list)


for i,url in enumerate(download_url_list):
    print(url)
    yt=YouTube(url)


    #!!!!!!!yt.title compatible with title prasered from beautifulsoup
    # print(yt.title+'\n'+download_title_list[i])

    # slash\backslash\colon\asterisk\question mark\quotation mark\greaterthan\less than\shuxian

    title=yt.title.replace(':','')
    # title=yt.title.replace('\\',"'slash'").replace('/',"'backslash'").replace(':',"'colon'").replace('*',"'asterisk'")
    # title=title.replace('?',"'quest'").replace('"',"'quotat'").replace('>',"'greater'")
    # title=title.replace('<',"'less'").replace('|',"'shuxian'")


    # if download_title_list[i]==yt.title:


    # all the video info getted from beautifulsoup
    # title=yt.title
    # views=yt.views
    # length=yt.lengthw
    # thumbnail_url=yt.thumbnail_url
    # rating=yt.rating
    # descrption=yt.description

    # allowed_format=yt.streams.all()

    # mp4_1080=yt.streams.filter(adaptive=True).all()[0]
    mp4_1080=yt.streams.filter(file_extension='mp4').all()[0]
    # yt.streams.get_by_itag('22')

    if os.path.exists(r'./video/{}.mp4'.format(title)):
        pass
    else:
        mp4_1080.download(r'./videos')

    #yt.streams.filter(only_audio=True).all()#be used just downlaod audio file

    #downlaod subttitle

    yt.captions.all()
    caption = yt.captions.get_by_language_code('en')

    if caption is not None:
        subtitle=caption.generate_srt_captions()

        if os.path.exists(r'./subtitle/{}.srt'.format(title)):
            pass
        else:
            with open(r"./subtitle/{}.srt".format(title),'wb') as f:
                b_subtitle=subtitle.encode(encoding='utf_8')
                f.write(b_subtitle)


    # print(caption.generate_srt_captions())
