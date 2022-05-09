from webbrowser import WindowsDefault
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from moviepy.editor import VideoFileClip
import sys, os

from pytube import YouTube

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        # Window
        self.show()
        self.setWindowTitle("YouTube Downloader xD")
        self.mainMenu()
        self.setGeometry(250,250,600,80)
        self.setMaximumSize(1000, 80)
        self.setMinimumSize(600,80)

    def mainMenu(self):
        # Box, button initialize
        widget = QWidget()
        hbox = QHBoxLayout()
        hint = QLabel("<b> Youtube Link </b>")

        self.link = QLineEdit()
        btn = QPushButton("Download!")

        hbox.addWidget(hint)
        hbox.addWidget(self.link)
        hbox.addWidget(btn)

        widget.setLayout(hbox)

        self.setCentralWidget(widget)

        # Connecting button with the download function
        btn.clicked.connect(self.download)

    def download(self):
        # Download mp4 file and convert it to mp3 file
        url = self.link.text()
        mp4 = YouTube(url).streams.get_highest_resolution().download()

        mp3 = mp4.split(".mp4", 1)[0] + ".mp3"
        video_clip = VideoFileClip(mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3)

        video_clip.close()
        audio_clip.close()
        # Remove the mp4 file (bcz it is a trash)
        os.remove(mp4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())