import sys, time, threading
from PyQt5.QtWebEngineCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *








class EditScreen(QMainWindow):
    def __init__(self, screenSite):
        self.screenEdit = screenSite
        super().__init__()
        self.win = QWidget()

        #виджет отобр. срина
        self.scene = QGraphicsScene()
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.scene.setBackgroundBrush(QBrush(Qt.darkGray, Qt.SolidPattern))
        self.scene.addPixmap(QPixmap(screenSite))

        #тулбар
        tb = self.addToolBar('Menu') #
        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.saveImage)
        tb.addAction(saveAction)

        # сетка расположения виджетов
        hbox = QGridLayout(self)
        hbox.addWidget(tb,1,1)
        hbox.addWidget(self.view,2,2)

        # расположение сцены
        self.view.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.win.setLayout(hbox)
        self.win.show()



    def saveImage(self): #сохранение скриншота
        self.scene.clearSelection()
        self.scene.setSceneRect(self.scene.itemsBoundingRect())
        image = QImage(self.scene.sceneRect().size().toSize(), QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        painter = QPainter(image)
        self.scene.render(painter)


        fileName = QFileDialog.getSaveFileName(self, "Save Image", "","All Files (*);; PNG (*.png);; JPG (*.jpg)")
        if fileName:
            direct = fileName[0]
            formatimage = fileName[1]
            s, = formatimage.split('*',1)[1:]
            s = s[:-1]
            print(direct+s)
            image.save(direct)
            painter.end()





class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        tb = self.addToolBar('Menu')

        # виджет браузер

        self.web = QWebEngineView()
        self.web.load(QUrl('https://yandex.ru/'))
        self.setCentralWidget(self.web)
        self.web.urlChanged.connect(self.editUrl)



        # адрес. строка
        self.urlEdit = QLineEdit(self)
        self.urlEdit.move(200,5)
        self.urlEdit.resize(1000,24)
        self.urlEdit.setText(self.web.url().toString())

        # кнопка редактирования
        saveAction = QAction(QIcon('icon/icon_save.png'),'Save', self)
        saveAction.triggered.connect(self.showScrollBar)
        tb.addAction(saveAction)

        # кнопка выделение области
        editAction = QAction(QIcon('icon/icon_1'),'Edit', self)
        editAction.triggered.connect(self.editImage)
        tb.addAction(editAction)

        # кнопка назад
        backAction = QAction(QIcon('icon/back.png'),'Back', self)
        backAction.triggered.connect(self.backSite)
        tb.addAction(backAction)

        # кнопка вперд
        forwardAction = QAction(QIcon('icon/forward.png'),'Forward', self)
        forwardAction.triggered.connect(self.forwardSite)
        tb.addAction(forwardAction)

        # кнопка обновить
        reloadAction = QAction(QIcon('icon/reload.png'),'Back', self)
        reloadAction.triggered.connect(self.reloadSite)
        tb.addAction(reloadAction)

        self.setWindowTitle('Screen')
        self.show()

    def showScrollBar(self):
        self.saveImage()



    def saveImage(self): #сохранение скриншота
        self.pix = QPixmap(self.web.width(),self.web.height())
        self.painter = QPainter(self.pix)
        self.web.render(self.painter)

        self.openWindow = EditScreen(self.pix)

    def backSite(self): #функ. назад
        self.web.back()

    def forwardSite(self): #функ. вперед
        self.web.forward()

    def reloadSite(self): #функ. обновить
        self.web.reload()

    def editImage(self):
        self.web.setEnabled(False)

    def editUrl(self): #прорисовка адрес. строки
        self.urlEdit.setText(self.web.url().toString())
        self.urlEdit.home(False)
        self.urlEdit.clearFocus()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Browser()

    sys.exit(app.exec_())


