# -*- coding:utf-8 -*-

import sys
import importlib
importlib.reload(sys)


class editor(object):

    def __init__(self):
        self.name='youtube hacker'

    def func_main(self):
        import sys
        import importlib
        # import imp
        # imp.reload(sys)
        # importlib.reload(sys)
        # sys.setdefaultencoding("utf-8")

        import time
        import sched
        import sqlite3

        hour = time.strftime("%H", time.localtime())
        # if int(hour)%6 == 0:
        if True:
            self.func_praser()

            # with open('praser_youtube.py', 'r', encoding='utf-8') as f:
            #     # 使用exec时，字符串中不要使用中文!!!
            #     exec(f.read())

            conn = sqlite3.connect('./data.db')
            c = conn.cursor()

            # search temp table
            temp_info = c.execute('''SELECT title,length,url,views,loaded_time from temp_video_list''')
            temp_info_title = []
            temp_info_length = []
            temp_info_url = []
            temp_info_views = []
            temp_info_loaded_time = []
            temp_titl_and_url = {}
            temp_titl_and_length = {}
            temp_titl_and_views = {}
            temp_titl_and_loaded_time = {}
            for row in temp_info:
                temp_info_title.append(row[0])
                temp_info_url.append(row[2])
                temp_titl_and_url[row[0]] = row[2]
                temp_titl_and_length[row[0]] = row[1]
                temp_titl_and_views[row[0]] = row[3]
                temp_titl_and_loaded_time[row[0]] = row[4]

                # print(temp_titl_and_url)
                # temp_info_length.append(row[1])
                # temp_info_views.append(row[3])
                # temp_info_loaded_time.append(row[4])

            # search main table
            c.execute('''CREATE TABLE  IF NOT EXISTS full_video_list
               (title      text    NOT NULL,
               length      text    NOT NULL,
               url         text    NOT NULL,
               views       int     NOT NULL,
               loaded_time text    NOT NULL);''')
            full_list_title = c.execute('''SELECT title from full_video_list''')
            full_list_title_list = []
            for item in full_list_title:
                full_list_title_list.append(item[0])

            temp_download = []
            for item in temp_info_title:
                if item not in full_list_title_list:
                    full_list_title_list.append(item)
                    temp_download.append(item)

            # create a table to save the real needed downloaded
            c.execute('''CREATE TABLE  IF NOT EXISTS temp_download_list
               (title      text    NOT NULL,
               url         text    NOT NULL);''')

            for title in temp_download:
                url = temp_titl_and_url[title]
                length = temp_titl_and_length[title]
                views = temp_titl_and_views[title]
                loaded_time = temp_titl_and_loaded_time[title]

                c.execute('''INSERT INTO temp_download_list (title,url) \
                              VALUES (?,?)''', (title, url))

                c.execute('''INSERT INTO full_video_list (title,length,url,views,loaded_time) \
                      VALUES (?,?,?,?,?)''', (title, length, url, views, loaded_time))

                c.execute('''drop table temp_video_list''')

            conn.commit()

            self.func_download()
            # with open('pytube_main.py', 'r') as f:
            #     exec(f.read().encode('gb2312'))

            self.func_edit()
            # with open('video-editor.py', 'rb') as f:
            #     exec(f.read())


    def func_praser(self):
        from bs4 import BeautifulSoup
        import time
        import sqlite3
        import requests

        conn = sqlite3.connect('./data.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE  IF NOT EXISTS temp_video_list
               (title      text    NOT NULL,
               length      text    NOT NULL,
               url         text    NOT NULL,
               views       int     NOT NULL,
               loaded_time text    NOT NULL);''')

        # # mainpage of youtube channel
        # channel_list = {'sony':'https://www.youtube.com/user/sonyelectronics/videos'}
        # # 'Apple': 'https://www.youtube.com/user/Apple/videos',
        # # 'xiaomiglobal':'https://www.youtube.com/user/XIAOMIGLOBAL/videos'}
        channel_list={}
        with open('./channels.txt','r',encoding='utf-8') as f:
            for channel in f.readlines():
                if '#' not in channel:
                    channel_company=channel.split(';')[0]
                    channel_content=channel.split(';')[1]
                    print(channel_company,channel_content)
                    channel_list[channel_company]=channel_content

        def tag_parser(tag_group, attr):
            for tag in tag_group:
                return tag[attr]

        for company, channel_url in zip(channel_list.keys(), channel_list.values()):
            # html=request.urlopen(channel_url)
            html = requests.get(channel_url).content
            # f = open('html.html', mode='wb')
            # f.write(html)

            soup = BeautifulSoup(html, 'html.parser')

            titles_and_urls = soup.find_all('a', attrs={'dir': 'ltr', 'rel': 'nofollow'})
            views_group = soup.find_all('ul', attrs={'class': 'yt-lockup-meta-info'})
            length_group = soup.find_all('span', attrs={'class': 'video-time'})

            #
            for num in range(0, 3):
                title_and_url = titles_and_urls[num]
                title = title_and_url['title']
                url = 'https://www.youtube.com' + title_and_url['href']
                views = views_group[num].li.get_text().split(' ')[0].replace(',', '')
                length = length_group[num].get_text()
                if int(length.split(':')[-2]) > 10:
                    continue

                loaded_time = str(time.time()).split('.')[0]

                # print(str(title,encoding='utf-8'), str(length,encoding='utf-8'), str(url,encoding='utf-8'),
                #       int(views), loaded_time.encode('utf-8'))

                conn.text_factory = str
                title_record = c.execute('''SELECT title from temp_video_list''')

                title_record_list = []
                for title_item in title_record:
                    title_item_string = str(title_item[0])  # !!!using [0] to get text object
                    title_record_list.append(title_item_string)

                # print(title_record_list)

                if title not in title_record_list:
                    print('find new video.')
                    c.execute('''INSERT INTO temp_video_list (title,length,url,views,loaded_time) \
                          VALUES (?,?,?,?,?)''', (str(title), str(length), url, int(views), loaded_time))

                conn.commit()


    def func_download(self):
        import os
        import sqlite3

        from pytube import YouTube

        conn = sqlite3.connect(r'./data.db')
        c = conn.cursor()
        cursor = c.execute('''SELECT title,url from temp_download_list''')

        download_url_list = []
        download_title_list = []
        for row in cursor:
            download_title_list.append(row[0])
            download_url_list.append(row[1])

        # print(download_url_list)

        for i, url in enumerate(download_url_list):
            print(url)
            yt = YouTube(url)

            # !!!!!!!yt.title compatible with title prasered from beautifulsoup
            # print(yt.title+'\n'+download_title_list[i])

            # slash\backslash\colon\asterisk\question mark\quotation mark\greaterthan\less than\shuxian

            title = yt.title.replace(':', '').replace('/','')   #linux recognize the / as part of file address
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
            mp4_1080 = yt.streams.filter(file_extension='mp4').all()[0]
            # yt.streams.get_by_itag('22')

            if os.path.exists(r'/home/master/unvideos/{}.mp4'.format(title).encode('utf-8')):
                pass
            else:
                mp4_1080.download(r'/home/master/unvideos/')

            # yt.streams.filter(only_audio=True).all()#be used just downlaod audio file

            # downlaod subttitle

            yt.captions.all()
            caption = yt.captions.get_by_language_code('en')

            if caption is not None:
                subtitle = caption.generate_srt_captions()

                if os.path.exists(r'/home/master/subtitle/{}.srt'.format(title)):
                    pass
                else:
                    with open(r"/home/master/subtitle/{}.srt".format(title), 'wb') as f:
                        b_subtitle = subtitle.encode(encoding='utf_8')
                        f.write(b_subtitle)


    def func_edit(self):
        import os
        import os.path

        from moviepy.video import VideoClip
        from moviepy.editor import VideoFileClip, vfx, concatenate_videoclips, CompositeVideoClip, \
            ImageClip, TextClip
        # from moviepy.video.compositing import CompositeVideoClip
        from moviepy.video.tools.subtitles import SubtitlesClip

        from googletrans import Translator

        def translat(text='no text is passed'):
            trans = Translator()
            result = trans.translate(text, dest='zh-CN', src='en').text
            # Translated(src=en, dest=zh-cn, text=你好, pronunciation=Nǐ hǎo, extra_data="{'translat...")
            # print(result.text)

            return result

        def translat_subtitle(file):

            for i, line in enumerate(file.readline()):
                print(i, line)
                translated_sub = open(r'/home/master/subtitle/translated/{}.srt'.format(en_title), 'w',encoding='utf-8')

                if i % 4 == 2 or i == 2:
                    # doc=''
                    # doc=doc+str(line)
                    translated_line = translat(line)
                    translated_sub.write(translated_line)
                else:
                    translated_sub.write(line)

            return translated_sub

        for mp4 in os.listdir(r'/home/master/unvideos'):

            en_title = os.path.basename(mp4).split('.')[0]
            zh_title = translat(str(en_title))
            print(zh_title)

            main_clip = VideoFileClip(r'/home/master/unvideos/{}'.format(mp4))

            leader = VideoFileClip(r'./material/leader.mp4')
            main_clip=main_clip.resize(leader.size)

            # leader.duration=3
            # clip1=clip.fx(vfx.mirror_x)
            # clip2=clip.fx(vfx.mirror_y)
            # clip2=clip.resize(0.5)

            concatenate = concatenate_videoclips([leader, main_clip])

            logo = ImageClip(r'./material/logo.png')
            logo.duration = main_clip.duration
            logo.resize((350,150))
            # logo_end_gif=


            if os.path.exists(r'/home/master/subtitle/{}.srt'.format(en_title)):

                with open(r'/home/master/subtitle/{}.srt'.format(en_title), 'rb') as f:
                    pass
                    # print(f.read())
                    # en_sub=f.read()
                    # zh_sub=translat(en_sub)
                    # zh_srt=open(r'./subtitle/translated/{}.srt'.format(en_title),'wb')
                    # zh_srt.write(zh_sub)

                    # zh_srt=translat_subtitle(f)

                font = "ArialUnicode"
                color = 'white'
                generator = lambda txt: TextClip(txt, font=font, fontsize=40, color=color)
                # sub=SubtitlesClip(r'./subtitle/translated/{}.srt'.format(en_title),'rb')
                sub = SubtitlesClip(r'/home/master/subtitle/{}.srt'.format(en_title), generator)

                # final=clips_array([[clip1,clip2]])

                final = CompositeVideoClip([concatenate,
                                            sub.set_start(3).set_pos('bottom'),
                                            logo.set_start(3).set_pos((1400,100)).crossfadein(2)])

                # final.write_videofile('add_subtitle.mp4',fps=clip.fps)

                final.write_videofile('/home/master/edited/{}.mp4'.format(en_title), fps=main_clip.fps)

            else:
                final = CompositeVideoClip([concatenate,
                                            logo.set_start(3).set_pos((1400,100)).crossfadein(2)])
                final.write_videofile('/home/master/edited/{}.mp4'.format(en_title), fps=main_clip.fps,audio=True,verbose=True)


a=editor()
a.func_main()