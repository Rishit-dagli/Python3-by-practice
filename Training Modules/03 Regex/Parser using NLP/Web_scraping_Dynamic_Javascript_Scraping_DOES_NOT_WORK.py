import sys 
#QT is system arguments 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage

import bs4 as bs 
import urllib.request

class Client(QWebPage):

    def __init__(self,url):
        self.app = QApplication(sys.argv)
        #starting the application
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        #connecting method when method is finished -> Could work directly with webpage object
        self.mainFrame().load(QUrl(url))
        self.app.exec_() 

    def on_page_load(self):
        self.app.quit()
        #just want it to load and nothing else

    

url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
#get main frame and convert it to HTML 

soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p',class_='jstest')
#This lets parse paragraph tags with the class that contains jstest
print(js_test.text)
#This will print out the starting text 
#sometime parsing a table will present no data 
#The reason for this is that you are not a client so you will not get anything 
# Need to download this pip3 install PyQt5


#I tried fixing the code that guy has. but it does not work any more