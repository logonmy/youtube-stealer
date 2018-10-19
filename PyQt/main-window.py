# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget,QApplication,QHBoxLayout,QVBoxLayout,QGridLayout,\
    QPushButton,QLabel,QCommandLinkButton,QTableView,QTextBrowser,QTextEdit,QLineEdit,\
    QComboBox,QGraphicsOpacityEffect,QSpacerItem,QCheckBox,QDialog,QInputDialog,QFileDialog,\
    QMessageBox,QSpinBox,QFormLayout,QAbstractItemView,QScrollArea,QLayout
from PyQt5.QtGui import QIcon,QFont,QImage,QPixmap,QStandardItem,QDesktopServices
from PyQt5.QtCore import QSize,Qt,QModelIndex,QUrl,QThread,pyqtSignal
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer,QMediaPlaylist
# from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
import time
import configparser

# from ..fabric_connect import download,upload
# from ...bilibili import *
# from ...dayuhao import *
# from ...baijiahao import *
# from ...qiehao import *
# from ..upload_class import *
# from ..local_version import fabric_connect


sys.path.append('..')
from fabric_connect import upload,download,remote_connect
from upload_class import main_upload

class main_win(QWidget):

    def __init__(self):
        super(main_win,self).__init__()

        self.setWindowTitle('uploader')
        self.setFont(QFont('微软雅黑'))
        # self.setFixedSize(1200,800)
        # self.setWindowFlag(Qt.FramelessWindowHint)


        globallayout=QVBoxLayout()
        toplayout=QHBoxLayout()
        middelelayout=QHBoxLayout()
        bottomlayout=QVBoxLayout()

        self.config=configparser.ConfigParser()
        self.config.read(r'main-setting.ini')

        ################# toplayout #################
        self.btn_user_info=QPushButton('用户信息')
        self.btn_remote=QPushButton('远程同步')
        self.btn_setting=QPushButton('设置')
        self.btn_upload=QPushButton('上传')
        self.btn_default=QPushButton('默认')
        # QCommandLinkButton
        self.btn_command=QCommandLinkButton()
        self.btn_minimize=QPushButton()
        self.btn_close=QPushButton()

        self.btn_user_info.setObjectName('user_info')
        self.btn_minimize.setObjectName('minimize')
        self.btn_close.setObjectName('close')

        toplayout.addWidget(self.btn_user_info)
        toplayout.addWidget(self.btn_remote)
        toplayout.addWidget(self.btn_setting)
        toplayout.addWidget(self.btn_upload)
        toplayout.addWidget(self.btn_default)
        toplayout.addWidget(self.btn_command)
        toplayout.addWidget(self.btn_minimize)
        toplayout.addWidget(self.btn_close)

        self.btn_user_info.pressed.connect(self.m_user_info)
        self.btn_remote.pressed.connect(self.m_remote)
        self.btn_setting.pressed.connect(self.m_setting)
        self.btn_upload.pressed.connect(self.m_upload)
        self.btn_default.pressed.connect(self.m_default)
        # self.btn_command.pressed.connect()
        self.btn_minimize.pressed.connect(self.m_minimize)
        self.btn_close.pressed.connect(self.m_close)


        ################## middellayout #################
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data.db')

        self.local=QSqlDatabase.addDatabase('QSQLITE')
        self.local.setDatabaseName('local.db')

        middle_inside=QGridLayout()
        self.tableview=QTableView()

        self.lab_title=QLabel('标题')
        self.line_title=QLineEdit()
        self.line_title.setWindowOpacity(0.5)
        self.lab_video_info=QLabel('视频描述')
        # self.text_video_info_en=QTextBrowser()
        self.text_video_info_ch=QTextBrowser()
        self.lab_labels=QLabel('视频标签')
        self.line_label1=QLineEdit()
        self.line_label2 = QLineEdit()
        self.line_label3 = QLineEdit()
        self.line_label4 = QLineEdit()
        self.line_label5 = QLineEdit()
        self.lab_header_choice=QLabel('片头选择')
        self.com_header_choice=QComboBox()
        self.lab_logo_choice=QLabel('logo选择')
        self.com_logo_choice=QComboBox()
        self.btn_save=QPushButton('保存编辑')
        self.btn_clear=QPushButton('清空编辑')
        self.btn_bilibili=QCheckBox('哔哩哔哩')
        self.btn_dayuhao = QCheckBox('大鱼号')
        self.btn_baijiahao = QCheckBox('百家号')
        self.btn_qiehao = QCheckBox('企鹅号')
        self.btn_other = QCheckBox('未完待续')
        self.btn_submit=QPushButton('上传')

        self.line_title.setObjectName('line_title')
        self.text_video_info_ch.setObjectName('video_info_ch')
        self.line_label1.setProperty('line','label')
        self.line_label2.setProperty('line', 'label')
        self.line_label3.setProperty('line', 'label')
        self.line_label4.setProperty('line', 'label')
        self.line_label5.setProperty('line', 'label')
        self.com_header_choice.setProperty('com','option')
        self.com_logo_choice.setProperty('com', 'option')
        self.btn_save.setProperty('btn','submit')
        self.btn_clear.setProperty('btn', 'submit')
        # self.btn_bilibili.setProperty('btn','upload')
        # self.btn_dayuhao.setProperty('btn','upload')
        # self.btn_baijiahao.setProperty('btn','upload')
        # self.btn_qiehao.setProperty('btn','upload')
        # self.btn_other.setProperty('btn','upload')


        middle_inside.addWidget(self.lab_title,0,0,1,1)
        middle_inside.addWidget(self.line_title,1,0,1,1)
        middle_inside.addWidget(self.lab_video_info,2,0,1,1)
        # middle_inside.addWidget(self.text_video_info_en,3,0,3,1)
        middle_inside.addWidget(self.text_video_info_ch,6,0,3,1)
        middle_inside.addWidget(self.lab_labels,0,1,1,1)
        middle_inside.addWidget(self.line_label1,1,1,1,1)
        middle_inside.addWidget(self.line_label2,2,1,1,1)
        middle_inside.addWidget(self.line_label3,3,1,1,1)
        middle_inside.addWidget(self.line_label4,4,1,1,1)
        middle_inside.addWidget(self.line_label5,5,1,1,1)
        middle_inside.addWidget(self.btn_save,6,1,1,1)
        middle_inside.addWidget(self.btn_clear,7,1,1,1)

        middelelayout.addWidget(self.tableview)
        middelelayout.addLayout(middle_inside)

        self.tabmodel=QSqlTableModel()
        self.tabmodel.setTable('temp_video_list')
        self.tabmodel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        # self.tabmodel.setFilter()
        self.tabmodel.select()
        self.tabmodel.setHeaderData(0,Qt.Horizontal,'title')
        self.tabmodel.setHeaderData(1,Qt.Horizontal,'length')
        self.tabmodel.setHeaderData(2,Qt.Horizontal,'url')
        self.tabmodel.setHeaderData(3,Qt.Horizontal,'views')
        self.tabmodel.setHeaderData(4, Qt.Horizontal, 'loaded')
        self.tableview.setModel(self.tabmodel)

        self.btn_save.pressed.connect(self.m_save)
        self.btn_clear.pressed.connect(self.m_clear)
        # self.item_video=QStandardItem()
        self.tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableview.setSelectionModel(QAbstractItemView.SingleSelection)

        # open video file
        # signals inherit from QAbstractItemView
        self.tableview.doubleClicked.connect(self.m_doubleclick)
        # self.tableview.clicked
        self.tableview.activated.connect(self.m_active)
        # self.tableview.pressed


        #######bottomlayout#######
        self.lab_local_info=QLabel('执行信息')
        self.textbrowser=QTextBrowser()
        # self.textbrowser

        self.textbrowser.setAlignment(Qt.AlignBottom)
        self.textbrowser.setObjectName('textbrowser')

        bottomlayout.addWidget(self.lab_local_info)
        bottomlayout.addWidget(self.textbrowser)


        # 界面全局
        globallayout.addLayout(toplayout)
        globallayout.addLayout(middelelayout)
        globallayout.addLayout(bottomlayout)

        self.setLayout(globallayout)


    def m_user_info(self):

        self.user_info=userinfo()
        self.user_info.exec_()


    def m_remote(self):

        # using fabric connect remote server and execute command

        ip=self.config['remote']['ip']
        port=self.config['remote']['port']
        username=self.config['remote']['username']
        password=self.config['remote']['password']
        remotepath=self.config['remote']['file-path']
        remotedb=self.config['remote']['remote-db-path']
        localpath=self.config['download']['save-path']
        localdb=self.config['download']['local-db-path']

        # connect
        remote_connect(username,ip,port,password)
        self.db.close()

        # execute sync the remote files, and return exective infomation
        # sync database
        # db file path
        db_path=os.path.join(localdb,'data.db')
        print(db_path)
        if os.path.exists(db_path):
            # os.remove(db_path)
            print(time.time(),'old db remove complete')
            download(localdb,remotedb)
            self.textbrowser.setPlaceholderText('sync db file')
            print(time.time(),'db download success')
        else:
            pass

        # sync videos
        if os.path.exists(localpath):
            self.textbrowser.setPlaceholderText('sync video files begin')
            print(time.time(),'begin sync videos')
            # downloading will spend a long time, using thread to keep
            multi_thread_download(localpath,remotepath)
            self.textbrowser.setPlaceholderText('sync video file complete')
        else:
            error=warning('file path not exit')
            error.exec_()

        print(time.time(),'upgrade db')
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data.db')


    def m_setting(self):

        setting=settinginfo(self.config)
        setting.exec_()

    def m_upload(self):

        for video in os.listdir(self.config['upload']['final-path']):

            if 'True'==self.config['upload']['bilibili']:

                multi_thread_1(self.config['upload']['bilibili_user'],self.config['upload']['bilibili_pass'],
                               video)

            if 'True'==self.config['upload']['dayuhao']:
                multi_thread_2(self.config['upload']['dayu_user'], self.config['upload']['dayu_pass'],
                               video)
            if 'True' == self.config['upload']['baijiahao']:
                multi_thread_3(self.config['upload']['baijia_user'], self.config['upload']['baijia_pass'],
                               video)
            if 'True' == self.config['upload']['qiehao']:
                multi_thread_4(self.config['upload']['qie_user'], self.config['upload']['qie_pass'],
                               video)
            if 'True' == self.config['upload']['others']:
                multi_thread_5(self.config['upload']['other_user'], self.config['upload']['other_pass'],
                               video)



    def m_default(self):
        pass


    def m_minimize(self):
        self.hide()

    def m_close(self):
        self.db.close()
        self.local.close()
        self.close()

    def m_save(self):
        self.localmodel=QSqlTableModel()
        self.localmodel.setTable('new')
        title=self.line_title.text()
        lab1=self.line_label1.text()
        lab2 = self.line_label2.text()
        lab3 = self.line_label3.text()
        lab4 = self.line_label4.text()
        lab5=self.line_label5.text()
        desc=self.text_video_info_ch.toPlainText()

        self.localmodel.insertRow(0,(title,lab1,lab2,lab3,lab4,lab5,desc,self.title,
                                     self.url,self.length,self.views,self.loaded))


    def m_clear(self):
        pass

    def m_selectRow(self):
        # self.line_title
        pass

    def m_doubleclick(self):
        # index=self.tableview.currentIndex() # just row index
        # index=self.tableview.selectedIndexes() # 5 cell index
        # item=self.tableview.selectRow(index)
        # item=self.tableview.itemDelegate(index[0])
        # self.tableview.model # return QAbstracItemView
        # !!!!!!!!!! pyqt5 have do a lot optimize for string !!!!!!!!!!!!
        # item=self.tableview.model().data(index[0])



        # using system default video player play the mp4
        filepath='{}{}.mp4'.format(self.config['download']['filepath'],self.title)
        QDesktopServices.openUrl(QUrl.fromLocalFile(filepath))

    def m_active(self):

        index = self.tableview.selectedIndexes()
        self.title = self.tableview.model().data(index[0])
        self.length = self.tableview.model().data(index[1])
        self.url = self.tableview.model().data(index[2])
        self.views = self.tableview.model().data(index[3])
        self.loaded = self.tableview.model().data(index[4])


    #################### reload class method ##################
    def resizeEvent(self, QResizeEvent):
        # super(QWidget, self).__init__()
        background_image = QImage(r'components/preview.png').scaled(self.width(), self.height(), Qt.IgnoreAspectRatio,
                                                                    Qt.SmoothTransformation)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QPixmap.fromImage(background_image)))
        self.setPalette(palette)

class multi_thread_download(QThread):

    def __init__(self,localpath,remotepath):
        super(QThread, self).__init__()
        self.localpath=localpath
        self.remotepath=remotepath

    def run(self):
        download(self.localpath, self.remotepath)


class multi_thread_1(QThread):

    def __init__(self,username,password,file):
        super(QThread,self).__init__()
        self.username=username
        self.passord=password
        self.file=file

        signal_out=pyqtSignal()


    def run(self):
        upload_class.bilibili(self.username,self.passord,self.file)
        print('upload video to bilibili complete')

class multi_thread_2(QThread):

    def __init__(self,username,password,file):
        super(QThread,self).__init__()
        self.username=username
        self.passord=password
        self.file=file

        signal_out=pyqtSignal()


    def run(self):
        upload_class.dayuhao(self.username,self.passord,self.file)
        print('upload video to dayuhao complete')

class multi_thread_3(QThread):

    def __init__(self,username,password,file):
        super(QThread,self).__init__()
        self.username=username
        self.passord=password
        self.file=file

        signal_out=pyqtSignal()


    def run(self):
        upload_class.baijiahao(self.username,self.passord,self.file)
        print('upload video to baijiahao complete')

class multi_thread_4(QThread):

    def __init__(self,username,password,file):
        super(QThread,self).__init__()
        self.username=username
        self.passord=password
        self.file=file

        signal_out=pyqtSignal()


    def run(self):
        upload_class.qiehao(self.username,self.passord,self.file)
        print('upload video to qiehao complete')

class multi_thread_5(QThread):

    def __init__(self,username,password,file):
        super(QThread,self).__init__()
        self.username=username
        self.passord=password
        self.file=file

        signal_out=pyqtSignal()


    def run(self):
        upload_class.others(self.username,self.passord,self.file)
        print('upload video to others complete')


class multi_thread_upload(QThread):

    def __init__(self,localpath,remotepath):
        super(QThread,self).__init__()
        self.localpath=localpath
        self.remotepath=remotepath

        signal_out=pyqtSignal()


    def run(self):
        upload(self.localpath,self.remotepath)
        print('upload files to server complete')

class multi_thread_sync(QThread):

    def __init__(self,localpath,remotepath):
        super(QThread,self).__init__()
        self.localpath=localpath
        self.remotepath=remotepath

        signal_out=pyqtSignal()


    def run(self):
        sync(self.localpath,self.remotepath)
        print('sync files to server complete')


class userinfo(QDialog):

    def __init__(self):
        super(userinfo,self).__init__()

        layout=QGridLayout()
        self.lab_zhifu=QLabel()
        layout.addWidget(self.lab_zhifu,0,0,1,1)

        self.setLayout(layout)



class remoteinfo(QDialog):

    def __init__(self,conf):
        super(remoteinfo, self).__init__()


    def m_setting_save(self):
        pass

    def m_setting_clear(self):
        pass


class settinginfo(QDialog):

    def __init__(self,conf):
        super(settinginfo,self).__init__()

        self.conf=conf

        layout=QVBoxLayout()

        # 常规
        self.lab_1=QLabel('常规')
        self.lab_1.setFixedSize(50,50)
        sub_layout1=QFormLayout()
        self.btn_back_image=QPushButton()
        self.line_back_image=QLineEdit()
        self.line_back_image.setText(self.conf['common']['background-image'])
        self.lab_style=QLabel()
        self.com_style=QComboBox()
        self.com_style.addItem('default')
        self.com_style.addItem('classical')
        # self.com_style.setCurrentIndex(int(self.conf['common']['style']))
        # self.che_11=QCheckBox('')
        # self.che_11.setChecked(bool(self.config['common']['']))
        sub_layout1.addRow(self.btn_back_image,self.line_back_image)
        sub_layout1.addRow(self.lab_style,self.com_style)

        self.lab_1.setProperty('lab','main')
        self.lab_style.setProperty('lab','sub')
        self.btn_back_image.setProperty('btn','sub')
        self.line_back_image.setProperty('line','sub')
        self.com_style.setProperty('com','sub')

        sub_1=QHBoxLayout()
        sub_1.addWidget(self.lab_1)
        sub_1.addLayout(sub_layout1)

        self.btn_back_image.pressed.connect(self.back_image)


        # upload
        self.lab_2=QLabel('上传')
        self.lab_2.setFixedSize(50, 50)
        sub_layout2=QFormLayout()
        self.che_21 = QCheckBox('哔哩哔哩')
        self.che_21.setChecked(bool(self.conf['upload']['bilibili']))
        self.line_211=QLineEdit()
        self.line_211.setPlaceholderText('哔哩哔哩用户名')
        self.line_211.setText(self.conf['upload']['bilibili_user'])
        self.line_212 = QLineEdit()
        self.line_212.setPlaceholderText('哔哩哔哩账户密码')
        self.line_212.setText(self.conf['upload']['bilibili_user'])
        self.che_22 = QCheckBox('大鱼号')
        self.che_22.setChecked(bool(self.conf['upload']['dayuhao']))
        self.line_221=QLineEdit()
        self.line_221.setText(self.conf['upload']['dayu_user'])
        self.line_222= QLineEdit()
        self.line_222.setText(self.conf['upload']['dayu_user'])
        self.che_23 = QCheckBox('百家号')
        self.che_23.setChecked(bool(self.conf['upload']['baijiahao']))
        self.line_231=QLineEdit()
        self.line_231.setText(self.conf['upload']['baijia_user'])
        self.line_232 = QLineEdit()
        self.line_232.setText(self.conf['upload']['baijia_user'])
        self.che_24 = QCheckBox('企鹅号')
        self.che_24.setChecked(bool(self.conf['upload']['qiehao']))
        self.line_241=QLineEdit()
        self.line_241.setText(self.conf['upload']['qie_user'])
        self.line_242 = QLineEdit()
        self.line_242.setText(self.conf['upload']['qie_user'])
        self.che_25 = QCheckBox('未完待续')
        self.che_25.setChecked(bool(self.conf['upload']['others']))
        self.line_251=QLineEdit()
        self.line_251.setText(self.conf['upload']['other_user'])
        self.line_252= QLineEdit()
        self.line_252.setText(self.conf['upload']['other_user'])

        sub_layout2.addWidget(self.che_21)
        sub_layout2.addRow(self.line_211,self.line_212)
        # sub_layout2.addWidget(self.line_211)
        # sub_layout2.addWidget(self.line_212)
        sub_layout2.addWidget(self.che_22)
        sub_layout2.addRow(self.line_231,self.line_232)
        # sub_layout2.addWidget(self.line_221)
        # sub_layout2.addWidget(self.line_222)
        sub_layout2.addWidget(self.che_23)
        sub_layout2.addRow(self.line_231,self.line_232)
        # sub_layout2.addWidget(self.line_231)
        # sub_layout2.addWidget(self.line_232)
        sub_layout2.addWidget(self.che_24)
        sub_layout2.addRow(self.line_241,self.line_242)
        # sub_layout2.addWidget(self.line_241)
        # sub_layout2.addWidget(self.line_242)
        sub_layout2.addWidget(self.che_25)
        sub_layout2.addRow(self.line_251,self.line_252)
        # sub_layout2.addWidget(self.line_251)
        # sub_layout2.addWidget(self.line_252)
        # sub_layout2
        # sub_layout2.setSizeConstraint(QLayout.SetMinimumSize)


        self.lab_2.setProperty('lab','main')
        self.che_21.setProperty('che','sub')
        self.line_211.setProperty('line','account')
        self.line_212.setProperty('line', 'account')
        self.che_22.setProperty('che', 'sub')
        self.line_221.setProperty('line', 'account')
        self.line_222.setProperty('line', 'account')
        self.che_23.setProperty('che', 'sub')
        self.line_231.setProperty('line', 'account')
        self.line_232.setProperty('line', 'account')
        self.che_24.setProperty('che','sub')
        self.line_241.setProperty('line', 'account')
        self.line_242.setProperty('line', 'account')
        self.che_25.setProperty('che', 'sub')
        self.line_251.setProperty('line', 'account')
        self.line_252.setProperty('line', 'account')

        sub_2 = QHBoxLayout()
        sub_2.addWidget(self.lab_2)
        sub_2.addLayout(sub_layout2)


        # 下载
        self.lab_3 = QLabel('下载')
        sub_layout3=QFormLayout()
        self.lab_speed=QLabel('限制下载速度')
        self.line_speed = QLineEdit()
        #
        self.lab_threadnum=QLabel('最大线程数')
        self.spin_threadnum=QSpinBox()
        self.spin_threadnum.setValue(int(self.conf['download']['threadnum']))
        self.btn_save_path = QPushButton('选择保存路径')
        self.line_save_path=QLineEdit(self.conf['download']['save-path'])
        self.btn_db_path=QPushButton('数据库路径')
        self.line_db_path = QLineEdit(self.conf['download']['local-db-path'])

        sub_layout3.addRow(self.lab_speed,self.line_speed)
        sub_layout3.addRow(self.lab_threadnum,self.spin_threadnum)
        sub_layout3.addRow(self.btn_save_path,self.line_save_path)
        sub_layout3.addRow(self.btn_db_path,self.line_db_path)

        self.lab_3.setProperty('lab','main')
        self.lab_speed.setProperty('lab','sub')
        self.line_speed.setProperty('line','sub')
        self.lab_threadnum.setProperty('lab','sub')
        self.spin_threadnum.setProperty('spin', 'sub')
        self.btn_save_path.setProperty('btn', 'sub')
        self.line_save_path.setProperty('line', 'sub')
        self.btn_db_path.setProperty('btn', 'sub')
        self.line_db_path.setProperty('line', 'sub')
        self.lab_3.setFixedSize(50, 50)
        self.line_speed.setFixedSize(100,30)

        sub_3 = QHBoxLayout()
        sub_3.addWidget(self.lab_3)
        sub_3.addLayout(sub_layout3)
        # sub_3.setAlignment(Qt.AlignLeft)

        self.btn_save_path.pressed.connect(self.save_path)
        self.btn_db_path.pressed.connect(self.db_path)


        #远程
        self.lab_4 = QLabel('远程')
        sub_layout4=QFormLayout()
        self.lab_ip = QLabel('服务器ip地址')
        self.line_ip = QLineEdit()
        self.line_ip.setPlaceholderText('例如：')
        self.line_ip.setText(self.conf['remote']['ip'])
        self.lab_port = QLabel('服务器端口')
        self.line_port = QLineEdit()
        self.line_port.setPlaceholderText('例如：')
        self.line_port.setText(self.conf['remote']['port'])
        self.lab_username = QLabel('用户名')
        self.line_username = QLineEdit()
        self.line_username.setText(self.conf['remote']['username'])
        self.lab_password = QLabel('密码')
        self.line_password = QLineEdit()
        self.line_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.line_password.setText(self.conf['remote']['password'])
        self.lab_connect = QLabel('连接方式')
        self.che_connect = QComboBox()
        self.che_connect.addItem('SSL')
        self.che_connect.setCurrentIndex(0)
        self.lab_db_remote=QLabel('远程数据库路径')
        self.line_db_remote=QLineEdit()
        self.line_db_remote.setText(self.conf['remote']['remote-db-path'])

        sub_layout4.addRow(self.lab_ip, self.line_ip)
        sub_layout4.addRow(self.lab_port, self.line_port)
        sub_layout4.addRow(self.lab_username, self.line_username)
        sub_layout4.addRow(self.lab_password, self.line_password)
        sub_layout4.addRow(self.lab_connect, self.che_connect)
        sub_layout4.addRow(self.lab_db_remote, self.line_db_remote)


        self.lab_4.setProperty('lab','main')
        self.lab_ip.setProperty('lab','sub')
        self.line_ip.setProperty('line', 'sub')
        self.lab_port.setProperty('lab', 'sub')
        self.line_port.setProperty('line', 'sub')
        self.lab_username.setProperty('lab', 'sub')
        self.line_username.setProperty('line','sub')
        self.lab_password.setProperty('lab', 'sub')
        self.line_password.setProperty('line', 'sub')
        self.lab_connect.setProperty('lab', 'sub')
        self.che_connect.setProperty('che', 'sub')
        self.lab_db_remote.setProperty('lab', 'sub')
        self.line_db_remote.setProperty('line', 'sub')


        sub_4=QHBoxLayout()
        sub_4.addWidget(self.lab_4)
        sub_4.addLayout(sub_layout4)


        # 预置
        self.lab_5 = QLabel('远程')
        sub_layout5=QHBoxLayout()
        self.che_preset=QCheckBox('是否保存为预置')
        self.che_preset.setChecked(bool(self.conf['label']['preset']))
        self.lab_labels=QLabel('标签')
        self.line_lab_1=QLineEdit()
        self.line_lab_1.setText(self.conf['label']['lab1'])
        self.line_lab_2 = QLineEdit()
        self.line_lab_2.setText(self.conf['label']['lab2'])
        self.line_lab_3 = QLineEdit()
        self.line_lab_3.setText(self.conf['label']['lab3'])
        self.line_lab_4 = QLineEdit()
        self.line_lab_4.setText(self.conf['label']['lab4'])
        self.line_lab_5 = QLineEdit()
        self.line_lab_5.setText(self.conf['label']['lab5'])

        self.lab_5.setProperty('lab','main')
        self.che_preset.setProperty('che','sub')
        self.line_lab_1.setProperty('line', 'sub')
        self.line_lab_2.setProperty('line', 'sub')
        self.line_lab_3.setProperty('line', 'sub')
        self.line_lab_4.setProperty('line', 'sub')
        self.line_lab_5.setProperty('line', 'sub')

        sub_5 = QHBoxLayout()
        sub_5.addWidget(self.lab_5)
        sub_5.addLayout(sub_layout5)


        # 视频合成 本地or服务器
        self.lab_6 = QLabel('本地or服务器')
        sub_layout6 = QFormLayout()
        self.lab_choose=QLabel('使用本地合成视频还是使用远程')
        self.che_choose=QCheckBox()
        self.che_choose.setChecked(bool(self.conf['video']['choose']))
        self.btn_material=QPushButton('添加新的logo或片头')
        self.line_material=QLineEdit()
        # 远程和本地默认
        self.com_header=QComboBox()
        for video in os.listdir('../material'):
            if video[-3:] in ['mp4','flv','wav']:
                self.com_header.addItem(video[:-4])
        self.com_header.setCurrentText(self.conf['video']['header'])
        self.com_logo=QComboBox()
        for image in os.listdir('../material'):
            if image[-3:] in ['jpg','png','gif']:
                self.com_logo.addItem(image[:-4])
        self.com_logo.setCurrentText(self.conf['video']['logo'])


        sub_layout6.addRow(self.lab_choose,self.che_choose)
        sub_layout6.addRow(self.btn_material,self.line_material)
        sub_layout6.addRow(self.com_header,self.com_logo)

        sub_7 = QHBoxLayout()
        sub_7.addWidget(self.lab_6)
        sub_7.addLayout(sub_layout6)

        self.che_choose.stateChanged.connect(self.choose)
        self.btn_material.pressed.connect(self.material)

        # 保存
        self.btn_save=QPushButton('保存配置')
        self.btn_default=QPushButton('恢复默认')
        self.btn_save.setProperty('btn','main')
        self.btn_default.setProperty('name', 'main')
        # self.save_setting.setFixedSize(150,40)
        # self.back_default.setFixedSize(150,40)

        sub_6=QHBoxLayout()
        sub_6.addWidget(self.btn_save)
        sub_6.addWidget(self.btn_default)
        # sub_4.setAlignment(Qt.AlignCenter)

        self.btn_save.pressed.connect(self.save)
        self.btn_default.pressed.connect(self.default)

        # 全局
        layout.addLayout(sub_1)
        layout.addSpacing(15)
        layout.addLayout(sub_2)
        layout.addSpacing(15)
        layout.addLayout(sub_3)
        layout.addSpacing(15)
        layout.addLayout(sub_4)
        layout.addSpacing(15)
        layout.addLayout(sub_5)
        layout.addSpacing(15)
        layout.addLayout(sub_7)
        layout.addSpacing(15)
        layout.addLayout(sub_6)

        main_inside=QScrollArea()
        main_inside.setLayout(layout)
        main_inside.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        main_inside.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        main_top=QHBoxLayout()
        main_top.addWidget(main_inside)
        self.setLayout(main_top)
        self.setFixedSize(700,700)

        # self.btn_back_image.pressed.connect()
        # self.com_style.
        #
        # self.che_21.stateChanged.connect()
        # self.che_22.stateChanged.connect()
        # self.che_23.stateChanged.connect()
        # self.che_24.stateChanged.connect()
        # self.che_25.stateChanged.connect()
        #
        # self.line_speed.editingFinished.connect()
        # self.spin_threadnum.
        # self.line_save_path.editingFinished.connect()
        # self.line_db_path.editingFinished.connect()
        #
        # self.line_ip.editingFinished.connect()
        # self.line_port.editingFinished.connect()
        # self.line_username.editingFinished.connect()
        # self.line_password.editingFinished.connect()
        # # self.remote
        # self.line_db_remote.editingFinished.connect()
        #
        # self.che_preset.stateChanged.connect()
        # self.line_lab_1.editingFinished.connect()
        # self.line_lab_2.editingFinished.connect()
        # self.line_lab_3.editingFinished.connect()
        # self.line_lab_4.editingFinished.connect()
        # self.line_lab_5.editingFinished.connect()


    def back_image(self):
        file_path=QFileDialog()
        path=file_path.getExistingDirectory()

        self.line_back_image.setText(path)
        self.config.set('common', 'background-image', str(path))

    def save_path(self):
        file_path=QFileDialog()
        path=file_path.getExistingDirectory()

        self.line_save_path.setText(path)
        self.config.set('download', 'save-path', str(path))

    def db_path(self):
        file_path=QFileDialog()
        path=file_path.getExistingDirectory()

        self.line_db_path.setText(path)
        self.config.set('download', 'local-db-path', str(path))

    def choose(self):
        pass

    def material(self):
        file_path=QFileDialog()
        path=file_path.getExistingDirectory()
        time.sleep(1)
        self.line_material.setText(path)
        import shutil
        shutil.copyfile(path,'./material')

    def save(self):
        # common

        if self.che_choose.isChecked() == 'True':
            multi_thread_sync(self.conf[''][''],self.conf[''][''])

        self.conf.set('common','background-image',self.line_back_image.text())
        self.conf.set('common','background-image',)

        # upload
        self.conf.set('upload','bilibili',self.che_21.isChecked())
        self.conf.set('upload','dayuhao',self.che_22.isChecked())
        self.conf.set('upload','baijiahao',self.che_23.isChecked())
        self.conf.set('upload','qiehao',self.che_24.isChecked())
        self.conf.set('upload','others',self.che_25.isChecked())

        # download
        self.conf.set('download','speed-limit',self.line_speed.text())
        self.conf.set('download','speed-limit',)
        self.conf.set('download','save-path',self.line_save_path.text())
        self.conf.set('download','local-db-path',self.line_db_path.text())

        # remote
        self.conf.set('remote','ip',self.line_ip.text())
        self.conf.set('remote','port',self.line_port.text())
        self.conf.set('remote','username',self.line_username.text())
        self.conf.set('remote','password',self.line_password.text())
        # self.conf.set('remote','file-path',self.line_.text())
        self.conf.set('remote','remote-db-path',self.line_db_remote.text())

        # label
        self.conf.set('label','preset',self.che_preset.isChecked())
        self.conf.set('label','lab1',self.line_lab_1.text())
        self.conf.set('label','lab2',self.line_lab_2.text())
        self.conf.set('label','lab3',self.line_lab_3.text())
        self.conf.set('label','lab4',self.line_lab_4.text())
        self.conf.set('label','lab5',self.line_lab_5.text())

        with open('main-ui.ini', 'w') as configfile:
            self.config.write(configfile)



    def default(self):
        with open('main-default.ini', 'w') as configfile:
            self.config.write(configfile)
            configfile.write('# default settings')


# warning dialog
class warning(QMessageBox):

    def __init__(self,message=''):
        super(warning, self).__init__()

        self.setText(message)


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=main_win()
    style_sheet=open(r'main-win.qss','r',encoding='utf-8')
    window.setStyleSheet(style_sheet.read())
    window.setFixedSize(1080,720)
    # window.setWindowFlag(Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())