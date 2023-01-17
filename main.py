from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_main_window import Ui_MainWindow

import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.link_edit.textChanged.connect(self.normalize_url)
        self.download_button.clicked.connect(self.download_video)
    
    def normalize_url(self):
        url = self.link_edit.text()
        updated_url = url.split('?')[0]
        
        self.link_edit.setText(updated_url)
        
    def download_video(self):
        link_tiktok = self.link_edit.text()
        
        if link_tiktok:
            
            os.system('python3 -m tiktok_downloader --snaptik --url {} --save video.mp4'.format(link_tiktok))
            
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a link')
        
    

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()