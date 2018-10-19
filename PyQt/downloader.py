# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget,QApplication,QHBoxLayout,QVBoxLayout,QGridLayout,\
    QPushButton,QLabel,QCommandLinkButton,QTableView,QTextBrowser,QTextEdit,QLineEdit,\
    QComboBox,QGraphicsOpacityEffect,QSpacerItem,QCheckBox,QTabWidget,QScrollArea,QCheckBox,\
    QSpinBox,QDoubleSpinBox,QFileDialog,QFormLayout,QMessageBox,QAbstractScrollArea,QGroupBox,\
    QLayout,QDialog
from PyQt5.QtGui import QIcon,QFont,QDesktopServices,QImage,QPixmap
from PyQt5.QtCore import QSize,Qt,QRect,QUrl,QObject,pyqtSignal,QThread,QDateTime,QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEnginePage
# from PyQt5.QtWebEngine import QtWebEngine
# from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
import time
import configparser

# from . import utils
import utils



class url_valid(Exception):
    pass

# class

class downloader(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        self.signal_1=pyqtSignal()

        self.setWindowTitle('YouTube下载器')

        # # setting window background image
        # palette = QtGui.QPalette()
        # palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('components/preview.png')))
        # self.setPalette(palette)

        # # setting window auto-resize background image
        # # inorder to change the background image size immediately ,we reload the resizeevent method
        # print(self.width(), self.height(),'/n',self.geometry(),'/n',self.frameGeometry())
        # background_image=QImage(r'components/preview.png').scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # palette = QtGui.QPalette()
        # palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QPixmap.fromImage(background_image)))
        # self.setPalette(palette)


        # three tabwidget of QTabWidget
        self.main=QWidget()
        self.download=QWidget()
        self.setting=QWidget()

        self.tabwidget=QTabWidget()
        self.tabwidget.setObjectName('tabwidget')
        # self.tabwidget.setWindowFlag()

        # read software's config file
        f = open('downloader.ini', 'r+')
        self.conf=configparser.ConfigParser()
        self.conf.read_file(f)

        ###########main widget############
        # space=QSpacerItem(100,30)
        # space.setGeometry(QRect(10,10,100,30))
        lab_empty=QLabel('')
        lab_empty.setObjectName('lab_empty')
        self.video_url=QLineEdit()
        self.video_url.setPlaceholderText('请输入视频地址')
        self.video_url.setObjectName('video_url')
        self.tips=QPushButton('清空历史记录')
        self.tips.setObjectName('tips')
        self.join_us=QPushButton('加入我们')
        self.join_us.setObjectName('join_us')
        self.software_tip=QLabel('免费软件，谨防上当受骗')
        self.software_tip.setObjectName('software_tip')
        self.software_tip.setAlignment(Qt.AlignBottom)
        history_len=len(self.extract_top_five_history())

        self.btn_his_1=QPushButton()
        self.btn_his_2=QPushButton()
        self.btn_his_3=QPushButton()
        self.btn_his_4=QPushButton()
        self.btn_his_5=QPushButton()

        # qss style
        self.btn_his_1.setProperty('name','btn_his')
        self.btn_his_2.setProperty('name','btn_his')
        self.btn_his_3.setProperty('name','btn_his')
        self.btn_his_4.setProperty('name','btn_his')
        self.btn_his_5.setProperty('name','btn_his')


        self.lab_his_1=QLabel(self.extract_top_five_history()[0])
        self.lab_his_2 = QLabel(self.extract_top_five_history()[1])
        self.lab_his_3 = QLabel(self.extract_top_five_history()[2])
        self.lab_his_4 = QLabel(self.extract_top_five_history()[3])
        self.lab_his_5 = QLabel(self.extract_top_five_history()[4])

        # qss style
        self.lab_his_1.setProperty('name','lab_his')
        self.lab_his_2.setProperty('name','lab_his')
        self.lab_his_3.setProperty('name','lab_his')
        self.lab_his_4.setProperty('name','lab_his')
        self.lab_his_5.setProperty('name','lab_his')

        # setting search record
        for i,his in enumerate(self.extract_top_five_history()):
            # # method 1 not work
            # self.lab_his_[i]=QLabel()
            # self.lab_his_[i].setText(his)
            # method 2
            his_name = 'lab_his_' + str(i+1)
            self.__dict__[his_name].setText(his)
            self.his_num=str(i)



        # for i in range(0,history_len):
        #     his_name='his_'+str(i)
        #     setattr(self,his_name,QLineEdit(self.extract_top_five_history()[i])

        # main_layout=QVBoxLayout()
        # main_layout.addWidget(space)
        # main_layout.addWidget(self.video_url)
        # main_layout.addWidget(self.tips)
        self.main_layout=QGridLayout()
        # main_layout.minimumHeightForWidth(50)
        # main_layout.setSpacing()
        # main_layout.addWidget(space,3,0,1,2)
        self.main_layout.addWidget(lab_empty,1,0,2,4)
        self.main_layout.addWidget(self.join_us,0,4,1,2)
        self.main_layout.addWidget(self.video_url,3,1,1,3)
        self.main_layout.addWidget(self.tips,3,4,1,1)
        # main_layout.addWidget(self.his_1,4,3,1,4)
        his_form=QFormLayout()
        his_form.addRow(self.btn_his_1,self.lab_his_1)
        his_form.addRow(self.btn_his_2, self.lab_his_2)
        his_form.addRow(self.btn_his_3, self.lab_his_3)
        his_form.addRow(self.btn_his_4, self.lab_his_4)
        his_form.addRow(self.btn_his_5, self.lab_his_5)

        self.main_layout.addWidget(self.software_tip,10,0,2,1)

        self.main.setLayout(self.main_layout)

        self.video_url.editingFinished.connect(lambda :self.m_video_url(self.video_url.text()))
        self.tips.pressed.connect(self.m_tips)
        self.join_us.pressed.connect(self.m_join_us)

        for i, his in enumerate(self.extract_top_five_history()):
            his_name = 'btn_his_' + str(i+1)
            self.__dict__[his_name].pressed.connect(lambda : self.m_btn_his(i))
            # self.btn_his_[i]=QPushButton()
            # self.btn_his_[i].pressed.connect(lambda : self.m_btn_his(i))

        ########## download widget #############
        f=open('downloaded.csv','r')
        video_num=len(f.readlines())
        downloading=QScrollArea()
        # 读取下载多线程
        self.temp=[['1','1','1',r'C:\Users\lenovo\Desktop\project1\local-version\PyQt']]#
        self.temp_thread=0
        self.max_thread = self.conf['download']['max-download-thread']


        video_tip_temp=QVBoxLayout()
        # video_tips_temp.alignmentRect()
        video_tips_temp_widget=QWidget()
        for downloading_video in self.temp:
            # downloading_sub_widget=video_tip(downloading_video[0],False,downloading_video[1],downloading_video[2])
            # downloading.addScrollBarWidget(downloading_sub_widget)
            # downloading_sub_widget
            # downloading.setWidget(downloading_sub_widget)
            scroll1_width=downloading.width()
            video_tip_temp.addWidget(video_tip(downloading_video[0],False,downloading_video[2],downloading_video[3],scroll1_width),alignment=Qt.AlignTop)

        # downloading.setLayout(video_tip_temp)

        # video_tip_temp_widget.setFixedSize(downloading.width(),85*len(self.temp))
        video_tips_temp_widget.setLayout(video_tip_temp)
        video_tips_temp_widget.setMinimumWidth(750)
        # video_tip_temp_widget.setWindowOpacity(0.1)
        video_tips_temp_widget.setProperty('name', 'video_tips_widget')

        downloading.setWidget(video_tips_temp_widget)
        # downloading
        # downloading.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        downloading.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        downloading.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # downloading.setWindowOpacity(0.1)



        downloaded=QScrollArea()
        video_tips_group=QHBoxLayout()
        video_tips_group_widget=QWidget()
        print('perpar to add downloaded video tips')
        for item in f.readlines():
            print('read and create video tips')
            video_title=item.split(',')[1]
            video_path=item.split(',')[2]
            video_time=item.split(',')[3]
            # video_tip_group=QGroupBox()
            scroll2_width=downloaded.widget()
            video_tips_group.addWidget(video_tip(video_title, False,video_path, video_time,scroll2_width),alignment=Qt.AlignTop)
            # downloaded.addScrollBarWidget(video_tip(title,path,time))

        video_tips_group_widget.setLayout(video_tip_temp)
        # video_tip_temp_widget.setWindowOpacity(0.9)
        video_tips_group_widget.setProperty('name','video_tips_widget')

        downloading.setWidget(video_tips_group_widget)

        # downloaded.setWidget(video_tip(title,path,time))
        # downloaded.setLayout(video_tips_group)
        # downloaded.setAlignment()
        # downloaded.sizeAdjustPolicy()
        # downloaded.setHorizontalScrollBar()
        downloaded.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # downloaded.setVerticalScrollBar()
        downloaded.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # downloaded.setWindowOpacity(0.9)


        download_tab=QTabWidget()
        download_tab.addTab(downloading,'下载中{}'.format(len(self.temp)))
        download_tab.addTab(downloaded,'已完成{}'.format(video_num))
        download_layout=QVBoxLayout()
        download_layout.addWidget(download_tab)

        self.download.setLayout(download_layout)

        #############setting widget##############
        setting_layout=QVBoxLayout()

        setting_layout.addWidget(settingitem(self.conf))

        self.setting.setLayout(setting_layout)


        self.tabwidget.addTab(self.main,'首页')
        self.tabwidget.addTab(self.download,'下载管理')
        self.tabwidget.addTab(self.setting ,'设置')
        self.tab_num=3

        layout=QVBoxLayout()
        layout.addWidget(self.tabwidget)
        self.setLayout(layout)

    # @staticmethod
    # def check_config_datatype(data):
    #     try:
    #         test_int=int(data)
    #         return 'int'
    #     except:
    #         try:
    #             test_float=float(data)
    #             return 'float'
    #         except:
    #             return 'string'


    @staticmethod
    def extract_top_five_history():
        f = open('search_log.csv', 'r')
        length=len(f.readlines())
        history_search=[]
        for i in range(0, 5):
            if f.readline() is not None or f.readline() !='':
                history_search.append(f.readline())
            else:
                history_search.append('')

        return history_search



    #执行查询与下载，同时保存查询字段
    def m_video_url(self,url):

        print('add search log',time.time())
        f = open('search_log.csv', 'w')
        f.write(url)

        print('verificate:'.format(url), time.time())
        verification,title=utils.download_options(url)
        # 进入下载选项，否则打开网页
        if verification==True:

            sub_title=self.conf['download']['auto-download-subtitle']
            filepath=self.conf['download']['save-path']

            print('begain download',time.time())
            multi_download=multi_thread(url,sub_title,filepath)
            title=multi_download.start()

            system_time=QDateTime.currentDateTime()
            timeDisplay=system_time.toString("yyyy-MM-dd hh:mm:ss")
            self.temp.append([title,url,filepath,timeDisplay])

            self.download_page=QWidget()

            video_info=QGridLayout()
            download_option=QHBoxLayout()

            re_load=QPushButton('重新加载')
            close_tab=QPushButton('关闭此页面')
            goto_webpage=QPushButton('打开网页')
            video_title=QLabel(title)
            back_mainpage=QPushButton('返回主页')
            upload_time=QLabel(timeDisplay)

            video_info.addWidget(back_mainpage,0,0,1,1)
            video_info.addWidget(close_tab,0,1,1,1)
            video_info.addWidget(re_load,0,3,1,1)
            video_info.addWidget(goto_webpage,0,4,1,1)
            video_info.addWidget(video_title,1,2,2,5)
            video_info.addWidget(upload_time,2,3,1,3)
            video_info.setAlignment(Qt.AlignTop)

            flv_720=QPushButton('flv高清')
            mp4_1080=QPushButton('mp4超清')
            mp4_720=QPushButton('mp4高清')
            wav_720=QPushButton('wav高清')

            download_option.addWidget(flv_720)
            download_option.addWidget(mp4_720)
            download_option.addWidget(mp4_1080)
            download_option.addWidget(wav_720)

            video_download=QVBoxLayout()
            video_download.addLayout(video_info)
            video_download.addLayout(download_option)
            self.download_page.setLayout(video_download)


            self.tabwidget.addTab(self.download_page,'{}'.format(title))
            self.tab_num+=1

            self.tabwidget.setCurrentWidget(self.download_page)


            re_load.pressed.connect(self.relaod)
            close_tab.pressed.connect(self.closetab)
            goto_webpage.pressed.connect(lambda :self.gotowebpage(url))
            back_mainpage.pressed.connect(self.backmainpage)


            # self.signal_1(self.video_tabwidget_close)

            # self.temp_thread=self.temp_thread+1
            # while True:
            #     if self.max_thread == self.temp_thread-1:
            #         self.timer=QTimer()
            #         self.timer.start(5000)
            #     else:
            #         break


            # self.browser=QWebEngineView()
            # self.browser.load(url)

            print('method end',time.time())
            f = open('searched_log.csv', 'w')
            # video_title=title
            # save_path=filepath
            # cur_time=time.strftime('%Y%m%d%H%M%S')
            f.write('{0}{1}{2}{3}'.format(title,url,filepath,timeDisplay))

        else:
            self.browser_search = QWebEngineView()
            search_preview='https://www.youtube.com/results?search_query={}'.format(url)
            # search_preview ='www.bing.com'
            self.search_url=QUrl(search_preview)
            # self.browser_search.load(self.search_url)

            # self.browser=QWebEnginePage()
            # self.browser.load(self.search_url)

            # open system default browser
            open_system_browser=QDesktopServices()
            open_system_browser.openUrl(self.search_url)




    def relaod(self):
        pass

    def gotowebpage(self,url):
        browser_search = QWebEngineView()
        search_url = QUrl(url.replace('watch?v=','embed/'))
        browser_search.load(search_url)

    def backmainpage(self):
        self.tabwidget.setCurrentWidget(self.main)

    def closetab(self):
        self.tabwidget.removeTab(self.tabwidget.currentIndex())

    # when the video_tabwidget be closed
    def video_tabwidget_close(self):
        self.tabwidget.setCurrentWidget(self.main)

    # when the video has been download successfully
    def multithread_(self,title):

        self.temp_thread=self.temp_thread-1
        QMessageBox.information(QMessageBox,'{} 下载已完成'.format(title))


    def m_join_us(self):

        support=QDialog()
        layout=QHBoxLayout()
        join_lab_1=QLabel('支付宝转账或Paypal')
        join_lab_2=QLabel()
        # join_lab_2.setStyleSheet('''backgrround:image url(:components/zhifu.png)''')
        join_lab_3=QLabel('')
        join_lab_4=QLabel('开发不易，请多支持')

        layout.addWidget(join_lab_1)
        layout.addWidget(join_lab_2)
        layout.addWidget(join_lab_3)
        layout.addWidget(join_lab_4)

        support.setLayout(layout)

        support.setWindowTitle('support developer')
        support.exec_()


    #删除保存的查寻字段
    def m_tips(self):
        self.search_log_filepath=os.path.join(os.curdir,'/search_log.csv')
        if os.path.exists(self.search_log_filepath):
            os.remove(self.search_log_filepath)
        f=open('search_log.csv','w')

    def m_btn_his(self,i):

        name_btn='btn_his_'+str(i)
        name_lab='lab_his_'+str(i)
        delattr(self,name_btn)
        delattr(self,name_lab)

        # f = open('search_log.csv', 'r')
        # for line in f.readlines():
        #     if self.lab_his_[i].text() in line:

        import csv
        with open('search_log.csv', 'rb') as inp, open('first_edit.csv', 'wb') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if self.lab_his_[i].text() in row:
                    writer.writerow(row)



    ###############reload class method##############
    def resizeEvent(self, QResizeEvent):
        # super(QWidget, self).__init__()
        background_image=QImage(r'components/preview.png').scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QPixmap.fromImage(background_image)))
        self.setPalette(palette)


class multi_thread(QThread):

    def __init__(self,url,sub_title,filepath):
        super(QThread,self).__init__()
        self.url=url
        self.sub_title=sub_title
        self.filepath=filepath

        signal_out=pyqtSignal()


    def run(self):
        title=utils.sub_downloader(self.url,self.sub_title,self.filepath)
        return title




class video_tip(QWidget):

    def __init__(self,title_info,sub_title_info,path_info,time_info,width):
        super(video_tip,self).__init__()


        layout=QHBoxLayout()
        sub_layout=QVBoxLayout()

        self.title_info=title_info
        self.path_info=path_info

        self.title=QLabel(title_info)
        self.path=QLabel(path_info)
        self.time=QLabel(time_info)
        # self.title.setFixedHeight()
        self.title.setObjectName('title')
        self.path.setObjectName('path')
        self.time.setObjectName('time')

        sub_layout.addWidget(self.title)
        sub_layout.addWidget(self.path)
        sub_layout.addWidget(self.time)
        # sub_layout

        self.video_icon=QLabel('video-icon')
        image=QImage(r'components/video.png').scaled(60,60,Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        image.save(r'components/video_.png')
        self.video_icon.setPixmap(QPixmap.fromImage(image))
        self.close_btn=QPushButton()
        # self.close_btn.setIcon(QIcon(r'component/close-4.png'))



        # self.close_btn.ba
        self.redownload_btn=QPushButton()
        self.video_icon.setObjectName('video_icon')
        self.close_btn.setObjectName('close_btn')
        self.redownload_btn.setObjectName('redownload_btn')
        self.video_icon.setFixedSize(60,60)
        self.redownload_btn.setFixedSize(60,60)
        self.close_btn.setFixedSize(60, 60)

        layout.addWidget(self.video_icon)
        layout.addLayout(sub_layout)
        layout.addWidget(self.redownload_btn)
        layout.addWidget(self.close_btn)

        self.redownload_btn.pressed.connect(lambda :self.redownload(title_info,sub_title_info,path_info))
        self.redownload_btn.pressed.connect(self.close)
        self.close_btn.pressed.connect(self.close)
        self.path.setOpenExternalLinks(True)
        self.path.linkActivated.connect(lambda :self.path_open)



        self.setLayout(layout)
        self.thread_num = 0

        self.setFixedSize(width,85)


    def redownload(self,title,sub_title,path):
        # 仅执行下载

        # multi_thread(title,sub_title,path)
        # self.thread_num=self.thread_num+1
        print('redownload pressed')


    def close_widget(self):
        print('close video tip')
        f = open('downloaded.csv', 'r+')
        lines=list(f)
        for line in lines:
            if self.title_info in line:

                # with open("textfile.txt", "r") as textobj:
                #     list = list(textobj)  # puts all lines in a list
                #
                # del list[del_line - 1]  # delete regarding element
                #
                # # rewrite the textfile from list contents/elements:
                # with open("textfile.txt", "w") as textobj:
                #     for n in list:
                #         textobj.write(n)
                lines.remove(line)

        ff=open('downloaded.csv','w')
        for line in lines:
            ff.write(line+'/n')

        # self.hide()
        self.close()

    def path_open(self):
        print('open video saved path')
        QDesktopServices.openUrl(QUrl(self.path_info))

# # setting item widget
# class setting_item(QWidget):
#
#     def __init__(self,item_label,settings={}):
#         super(setting_item,self).__init__()
#
#         # if len(settings)==0:
#         #     conf=open('/settings.conf','r')
#         #     for line in conf:
#         #         item=line.split(':')[0]
#         #         value=line.split(':')[1]
#         #         settings[item]=value
#
#         f = open('downloader.ini', 'r')
#         self.config = configparser.ConfigParser()
#         self.config.read_file(f)
#         section_num=len(self.config.sections())
#         for i,section in enumerate(self.config.sections()):
#
#             section_name='layout'+str(i)
#             # layout=QVBoxLayout()
#             setattr(self,section_name,QVBoxLayout)
#             lab_section_name='lab_section'+str(i)
#             # self.lab_setting=QLabel('{}'.format(section.__name__))
#             setattr(self,lab_section_name,QLabel('{}'.format(section.__name__))
#             self.__dict__[section_name].addWidget(self.__dict__[lab_section_name])
#
#             self.option_num = len(self.config.options(section))
#             for ii,option in enumerate(self.config.options(section)):
#
#                 value = self.config[section][option]
#
#                     datatype = self.check_config_datatype(value)
#                     option_name='option'+str(ii))
#                     # boolean
#                     if 'False' in value or 'True' in value:
#                         QCheckBox(option.__name__)
#                     # int
#                     elif datatype == 'int':
#                         QSpinBox()
#                     # float
#                     elif datatype == 'float':
#                         QDoubleSpinBox()
#                     # string
#                     else:
#                         QLineEdit()
#                 self.
#                 option_name='che_'+str(ii)
#                 # self.che_1=QCheckBox()
#                 # self.che_1.setChecked(True)
#                 setattr(self,option_name,QCheckBox(option.__name__))
#
#                 setting_default=settings[item]
#                 if setting_default==True:
#                     self.__dict__[item_name].setChecked(True)
#                 layout.addWidget(getattr(self,item_name))
#
#
#         self.che_1.stateChanged.connect(self.save_setting)
#         for setting in self.__dict__[1:]:
#             temp_conf={}
#             setting.stateChanged.connect(lambda :temp_conf[setting.__name__]=setting.checkState())
#
#
#
#
#         self.setLayout(layout)
#
#             # f = open('downloader.ini', 'r')
#             # self.config = configparser.ConfigParser()
#             # self.config.read_file(f)
#             # for section in self.config.sections():
#             #     setting_item()
#             #     for option in self.config.options(section):
#             #         value = self.config[section][option]
#             #         datatype = self.check_config_datatype(value)
#             #         # boolean
#             #         if 'False' in value or 'True' in value:
#             #             QCheckBox
#             #         # int
#             #         elif datatype == 'int':
#             #
#             #         # float
#             #         elif datatype == 'float':
#             #
#             #         # string
#             #         else:


class settingitem(QWidget):

    def __init__(self,conf):
        super(settingitem,self).__init__()

        f = open('downloader.ini', 'r')
        # self.config = configparser.ConfigParser()
        # self.config.read_file(f)
        self.config=conf

        layout=QVBoxLayout()

        # 常规
        self.lab_1=QLabel('常规')
        self.lab_1.setFixedSize(50,50)
        sub_layout1=QVBoxLayout()
        self.che_11=QCheckBox('建立任务后，继续停留在首页')
        self.che_11.setChecked(bool(self.config['common']['keep-main-page']))
        self.che_12=QCheckBox('最小化时自动隐藏')
        self.che_11.setChecked(bool(self.config['common']['auto-hide']))
        sub_layout1.addWidget(self.che_11)
        sub_layout1.addWidget(self.che_12)

        self.lab_1.setProperty('name','lab')
        self.che_11.setProperty('name','check')
        self.che_12.setProperty('name','check')

        sub_1=QHBoxLayout()
        sub_1.addWidget(self.lab_1)
        sub_1.addLayout(sub_layout1)


        #
        self.lab_2=QLabel('监控')
        self.lab_2.setFixedSize(50, 50)
        self.che_21 = QCheckBox('监控剪切板')
        self.che_11.setChecked(bool(self.config['monitor']['auto-jump']))
        sub_layout2=QVBoxLayout()
        sub_layout2.addWidget(self.che_21)

        self.lab_2.setProperty('name','lab')
        self.che_21.setProperty('name','check')

        sub_2 = QHBoxLayout()
        sub_2.addWidget(self.lab_2)
        sub_2.addLayout(sub_layout2)

        # 下载
        self.lab_3 = QLabel('下载')
        self.che_31 = QCheckBox('限制下载速度')
        self.che_31.setChecked(bool(self.config['download']['limit-speed']))
        self.max_thread=QSpinBox()
        self.max_thread.setValue(int(self.config['download']['max-download-thread']))
        self.choose_save_path=QPushButton('选择保存路径')
        self.line_3=QLineEdit('下载路径')
        self.che_11.setChecked(bool(self.config['download']['save-path']))
        # self.file_path=QFileDialog()
        # # self.file_path.getExistingDirectory()

        sub_layout3=QVBoxLayout()
        sub_layout3.addWidget(self.che_31)
        sub_layout3.addWidget(self.max_thread)
        sub_layout3.addWidget(self.choose_save_path)
        sub_layout3.addWidget(self.line_3)

        self.lab_3.setProperty('name','lab')
        self.che_31.setProperty('name','check')
        self.max_thread.setObjectName('max-thread')
        self.line_3.setObjectName('line_3')
        self.lab_3.setFixedSize(50, 50)
        # self.che_31.setFixedSize(120,20)
        self.max_thread.setFixedSize(150,30)
        self.choose_save_path.setFixedSize(100,30)
        self.line_3.setFixedSize(150,40)

        sub_3 = QHBoxLayout()
        sub_3.addWidget(self.lab_3)
        sub_3.addLayout(sub_layout3)
        sub_3.setAlignment(Qt.AlignLeft)

        self.save_setting=QPushButton('保存配置')
        self.back_default=QPushButton('恢复默认')
        self.save_setting.setProperty('name','btn')
        self.back_default.setProperty('name', 'btn')
        self.save_setting.setFixedSize(150,40)
        self.back_default.setFixedSize(150,40)
        sub_4=QHBoxLayout()
        sub_4.addWidget(self.save_setting)
        sub_4.addWidget(self.back_default)
        sub_4.setAlignment(Qt.AlignCenter)


        layout.addLayout(sub_1)
        layout.addSpacing(15)
        layout.addLayout(sub_2)
        layout.addSpacing(15)
        layout.addLayout(sub_3)
        layout.addSpacing(15)
        layout.addLayout(sub_4)


        self.setLayout(layout)

        self.che_11.stateChanged.connect(self.che11)
        self.che_12.stateChanged.connect(self.che12)
        self.che_21.stateChanged.connect(self.che21)
        self.che_31.stateChanged.connect(self.che31)
        # self.che_11.stateChanged.connect(self.che11)
        self.max_thread.valueChanged.connect(self.maxthread)
        self.choose_save_path.pressed.connect(self.choosesavepath)
        self.line_3.editingFinished.connect(self.line3)
        # self.file_path.urlSelected.connect(self.filepath)
        self.save_setting.pressed.connect(self.savesetting)
        self.back_default.pressed.connect(self.backdefault)


    def che11(self):
        # self.config['common']['keep-main-page']=self.che_11.checkState()
        self.config.set('common','keep-main-page',str(self.che_11.isChecked()))

    def che12(self):
        print('change the default setting')
        print(self.che_12.isChecked())
        # self.config['common']['auto-hide'] = self.che_12.checkState()
        self.config.set('common', 'auto-hide', str(self.che_12.isChecked()))

    def che21(self):
        # self.config['monitor']['auto-jump'] = self.che_21.checkState()
        self.config.set('monitor', 'auto-jump', str(self.che_21.isChecked()))

    def che31(self):
        # self.config['dowbload']['limit-speed'] = self.che_31.checkState()
        self.config.set('download', 'limit-speed', str(self.che_31.isChecked()))

    def maxthread(self):
        self.config.set('download', 'max-download-thread', str(self.max_thread.value()))

    def choosesavepath(self):
        file_path=QFileDialog()
        path=file_path.getExistingDirectory()

        self.line_3.setText(path)
        self.config.set('download', 'save-path', str(path))


    def line3(self):
        # self.config['download']['save-path']=self.line_3.text()
        self.config.set('download', 'save-path', str(self.line_3.text()))

    def filepath(self):
        self.config.set('download', 'save-path', str(self.file_path.getExistingDirectory()))

    def savesetting(self):
        with open('downloader.ini', 'w') as configfile:
            self.config.write(configfile)

    def backdefault(self):
        with open('downloader.ini', 'w') as configfile:
            self.config.write(configfile)
            configfile.write('# default settings')

    # def check(self,checkbox):
    #     if self.config['common']['keep-main-page']=='True':
    #         return True
    #     else:
    #         return False


def Message_1():
    message = QMessageBox('网址错误', '网址无法解析，请重新输入')
    message.show()




if __name__ =='__main__':
    app=QApplication(sys.argv)
    window=downloader()
    # window.setBaseSize(700,600)
    style_sheet=open(r'downloader.qss','r',encoding='utf-8')
    window.setStyleSheet(style_sheet.read())
    window.setGeometry(200,100,900,600)
    window.show()
    # setting=setting_item('常规',{'下载':1,'yincang':0})
    # setting.show()
    # setting=settingitem()
    # setting.show()
    sys.exit(app.exec_())
