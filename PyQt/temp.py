################configparser function test###############
# import configparser
#
# class temp():
#     def __init__(self):
#         item='che'
#         # self.vars()[item]='666'
#         # self.item.__name__='666'
#         setattr(self,item,'666')
#         print(self.__dict__[item])
#         print(self.__dict__)
#         print(type(getattr(self,item)))
#
#
# config=configparser.ConfigParser()
# f=open('downloader.ini','r')
# config.read_file(f)
# for section in config.sections():
#     for option in config.options(section):
#         # print(config.getboolean(section,option))
#         # print(config.getint(section,option))
#         # print(config.getfloat(section, option))
#         # print(type(config[section][option]))
#         # print(eval(config[section][option]))
#         pass
# int_instance=config.getint('download','max-download-sametime')
# print(type(int_instance))
# # print(temp().che)



##############csv delete one line###############
# f = open("downloaded.csv","r+")
# d = f.readlines()
# # f.seek(0)
# for i in d:
#     if i == '666':
#         del i
#         # pass
#     # print(i)
#         # f.write(None)
# # f.truncate()
# # f.close()

# #############test for QScrollArea##############
# from PyQt5.QtWidgets import QApplication,QScrollArea,QLabel,QWidget,QVBoxLayout,QScrollBar
# from PyQt5.QtCore import QSize,Qt
# import sys
#
# class win(QWidget):
#
#     def __init__(self):
#         super(win, self).__init__()
#         self.setGeometry(200,100,900,600)
#
#         layout=QVBoxLayout()
#         area=QScrollArea()
#         # area.setWidget(QLabel('hello'))
#         # area.addScrollBarWidget(QScrollBar(),Qt.AlignRight)
#         # Qt.RightToolBarArea
#
#         layout.addWidget(QLabel('hello world'))
#         layout.addWidget(QLabel('hello python'))
#         layout.addWidget(QLabel('hello pyqt'))
#
#         # layout.addWidget(area)
#
#         self.setLayout(layout)
#
# if __name__ =='__main__':
#     app=QApplication(sys.argv)
#     window=win()
#     window.show()
#     sys.exit(app.exec_())


################configparser update setting##############
# import configparser
#
#
# config=configparser.ConfigParser()
# # f=open('downloader.ini','r+')
# # config.read_file(f)
# config.read(r"C:\Users\lenovo\Desktop\project1\local-version\PyQt\downloader.ini")
#
# # print(config['common']['auto-hide'])
# # config.set('common','auto-hide','123')
# # config.update()
#
# with open('downloader.ini', 'w') as configfile:
#     # config.write('123456789')
#     configfile.write('123456789')



###############Using QFileDialog to choose filepath###############
# from PyQt5.QtWidgets import QFileDialog,QApplication,QWidget,QPushButton,QHBoxLayout
# import sys
#
# class win(QWidget):
#
    # def __init__(self):
    #     super(win, self).__init__()
    #     self.setGeometry(200,100,300,200)
#
#         layout=QHBoxLayout()
#         btn=QPushButton('open file choose dialog')
#         layout.addWidget(btn)
#
#         self.setLayout(layout)
#
#         btn.pressed.connect(self.open_file_choosing)
#
#     def open_file_choosing(self):
#         file_dialog=QFileDialog()
#         url_1=file_dialog.getExistingDirectoryUrl()
#         url_2=file_dialog.getExistingDirectory()
#         print(url_1,url_2)# url_2 return pure file-path
#         # PyQt5.QtCore.QUrl('file:///C:/Users/lenovo/Desktop/project1') C:/Users/lenovo/Desktop/project1/code
#
# if __name__ =='__main__':
#     app=QApplication(sys.argv)
#     window=win()
#     window.setGeometry(200,100,300,200)
#     window.show()
#     sys.exit(app.exec_())



############## test for playing video in Qt ################
# from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtMultimedia import QMediaPlayer,QMediaPlaylist,QMediaContent
# from PyQt5.QtCore import QUrl
# import sys
#
# class win(QWidget):
#
#     def __init__(self):
#         super(win, self).__init__()
#
#         layout=QHBoxLayout()
#
#         video_widget=QVideoWidget()
#         video=QMediaPlayer()
#         video.setVideoOutput(video_widget)
#
#         video_list=QMediaPlaylist()
#         video_list.addMedia(QMediaContent(QUrl.fromLocalFile('Festo.mp4')))
#         video.setPlaylist(video_list)
#         video_list.setCurrentIndex(0)
#         # video_list.setPlaybackMode()
#         # video.stateChanged.connect(video.mediaStatusChanged())
#
#         # video.setMedia(QMediaContent(QUrl.fromLocalFile("Festo.mp4")))
#         # video.positionChanged.connect.
#
#         video.play()
#
#         layout.addWidget(video_widget)
#         self.setLayout(layout)


############## open widows default video player ################
# from PyQt5.QtWidgets import QFileDialog,QApplication,QWidget,QPushButton,QHBoxLayout,\
#     QLabel
# from PyQt5.QtCore import QUrl,Qt
# from PyQt5.QtGui import QDesktopServices
# from PyQt5 import QtCore
# import sys
#
# class win(QWidget):
#
#     def __init__(self):
#         super(win, self).__init__()
#
#         layout=QHBoxLayout()
#         btn=QPushButton('play video')
#         layout.addWidget(btn)
#         self.file=r'Festo.mp4'
#
#         self.setLayout(layout)
#
#         btn.pressed.connect(self.open_file_choosing)
#
#     def open_file_choosing(self):
#         QDesktopServices.openUrl(QUrl.fromLocalFile(self.file))
#
# if __name__ =='__main__':
#     app=QApplication(sys.argv)
#     window=win()
#     window.show()
#     sys.exit(app.exec_


##################
import os

for video in os.listdir('../material'):
    if video[-3:] in ['mp4', 'flv', 'wav']:
        print(video[:-4])