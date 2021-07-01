from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWebKitWidgets import QtWebView,QWebPage
from PyQt5.QtWebKit import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebView()
        self.browser.setUrl(QUrl('https://google.com/search?q='))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #Navagation Menu
        navbar = QToolBar()
        self.addToolBar(navbar)

        #Home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        #Backpage button
        back_btn = QAction('<=', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        #Forwardpage button
        forward_btn = QAction('=>', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        #Refresh button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com/search?q='))

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Web")
window = MainWindow()
app.exec_()
