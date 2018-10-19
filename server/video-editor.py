# -*- coding:utf-8 -*-

import os
import os.path

from moviepy.video import VideoClip
from moviepy.editor import VideoFileClip,vfx,concatenate_videoclips,CompositeVideoClip,\
    ImageClip,TextClip
# from moviepy.video.compositing import CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip

from googletrans import Translator

def translat(text='no text is passed'):
    trans=Translator()
    result=trans.translate(text,dest='zh-CN',src='en').text
    #Translated(src=en, dest=zh-cn, text=你好, pronunciation=Nǐ hǎo, extra_data="{'translat...")
    #print(result.text)

    return result

def translat_subtitle(file):

    for i,line in enumerate(file.readline()):
        print(i,line)
        translated_sub = open(r'./subtitle/translated/{}.srt'.format(en_title), 'wb')

        if i%4==2 or i==2:
            # doc=''
            # doc=doc+str(line)
            translated_line=translat(line)
            translated_sub.write(translated_line)
        else:
            translated_sub.write(line)

    return translated_sub

for mp4 in os.listdir(r'./videos'):

    en_title=os.path.basename(mp4).split('.')[0]
    # zh_title=translat(str(en_title))
    # print(zh_title)

    main_clip=VideoFileClip(r'./videos/{}'.format(mp4))


    leader=VideoFileClip(r'./material/leader.mp4')
    leader=leader.resize(main_clip.size)
    # main_clip=main_clip.resize(leader.size)

    # leader.duration=3
    # clip1=clip.fx(vfx.mirror_x)
    # clip2=clip.fx(vfx.mirror_y)
    # clip2=clip.resize(0.5)

    logo=ImageClip(r'./material/logo.png')
    logo.duration=main_clip.duration
    logo.resize((350,150))
    # logo_end_gif=


    concatenate=concatenate_videoclips([leader,main_clip])

    if os.path.exists(r'./subtitle/{}.srt'.format(en_title)):

        with open(r'./subtitle/{}.srt'.format(en_title),'rb') as f:
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
        sub = SubtitlesClip(r'./subtitle/{}.srt'.format(en_title),generator)

        # final=clips_array([[clip1,clip2]])

        final=CompositeVideoClip([concatenate,
                                  sub.set_start(3).set_pos('center'),
                                  # logo.set_start(3).set_pos('right','top').crossfadein(1)
                                  logo.set_start(3).set_pos((1000,100)).crossfadein(2)])

        # final.write_videofile('add_subtitle.mp4',fps=clip.fps)

        final.write_videofile('./videos/edited/{}.mp4'.format(en_title),fps=main_clip.fps)

    else:
        final = CompositeVideoClip([concatenate,
                                    logo.set_start(3).set_pos((1400,100)).crossfadein(2)])
        final.write_videofile('./videos/edited/2{}.mp4'.format(en_title), fps=main_clip.fps,audio=True,verbose=True)
