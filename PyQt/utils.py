from pytube import YouTube
import os

# from .downloader import Message_1
# import downloader
# from . import downloader

class Filealreadyexit(Exception):

    def __init__(self):
        self.value='filealeadyexit'

class Urlnotvalid(Exception):
    def __init__(self):
        self.value='urlnotvalid'



def download_options(url):
    try:
        yt = YouTube(url)
        title=yt.title
        return True,title
    except:
        # self.browser.load('{}'.format(url))
        # Message_1()

        # raise Urlnotvalid
        return False,url

    # video_options= yt.streams

# os.path.curdir()
def sub_downloader(url,sub_title=False,filepath=''):

    yt = YouTube(url)

    title=yt.title
    mp4_1080=yt.streams.filter(file_extension='mp4').all()[0]
    if os.path.exists(r'{}/{}.mp4'.format(filepath,title)):
        raise Filealreadyexit
    else:
        mp4_1080.download(r'{}'.format(filepath))

    if sub_title:
        yt.captions.all()
        caption = yt.captions.get_by_language_code('en')

        if caption is not None:
            subtitle = caption.generate_srt_captions()

            if os.path.exists(r'{}/{}.srt'.format(filepath,title)):
                raise Filealreadyexit
            else:
                with open(r"{}/{}.srt".format(filepath,title), 'w') as f:
                    b_subtitle = subtitle.encode(encoding='utf_8')
                    f.write(b_subtitle)

    return title