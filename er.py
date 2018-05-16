import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
app = QApplication(sys.argv)
view = QWebEngineView()
url = QUrl(sys.argv[1] if len(sys.argv) > 1 else 'https://yandex.ru/')
view.setUrl(url)
view.resize(1024, 750)
view.show()
sys.exit(app.exec())