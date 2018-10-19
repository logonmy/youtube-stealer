################Using QImage to resize icons##################
from PyQt5.QtWidgets import QFileDialog,QApplication,QWidget,QPushButton,QHBoxLayout,QLineEdit
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QSize,Qt
import sys

class win(QWidget):

    def __init__(self):
        super(win, self).__init__()

        layout=QHBoxLayout()
        btn=QPushButton('open file choose dialog')
        self.line=QLineEdit()
        save=QPushButton('save resized image')

        layout.addWidget(btn)
        layout.addWidget(self.line)
        layout.addWidget(save)

        self.setLayout(layout)

        btn.pressed.connect(self.open_file_choosing)
        self.line.editingFinished.connect(self.image_resize)
        save.pressed.connect(self.save_image)

    def open_file_choosing(self):
        file_dialog=QFileDialog()
        self.choosed_image=file_dialog.getOpenFileName()
        self.filename=self.choosed_image[0].split('/')[-1].split('.')[0]
        print(self.choosed_image,self.filename)
        # ('C:/Users/lenovo/Desktop/project1/local-version/PyQt/components/redo.png', 'All Files (*)')

    def image_resize(self):
        text=self.line.text()
        self.width = int(text.split(' ')[0])
        self.height=int(text.split(' ')[1])
        self.resized_image=QImage(self.choosed_image[0]).scaled(self.width,self.height,Qt.IgnoreAspectRatio,Qt.SmoothTransformation)

    def save_image(self):
        file_dialog=QFileDialog()
        self.save_path=file_dialog.getExistingDirectory()
        self.resized_image.save(r'{0}/{1}{2}-{3}.png'.format(self.save_path,self.filename,self.width,self.height))
        print('complete')



if __name__ =='__main__':
    app=QApplication(sys.argv)
    window=win()
    window.setGeometry(200,100,80,40)
    window.show()
    sys.exit(app.exec_())