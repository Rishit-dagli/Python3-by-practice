#This will cover more advanced techiques 
import bs4 as bs 
import urllib.request

sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = bs.BeautifulSoup(sauce, "lxml") 

#just navigate just the nav bar 
nav = soup.nav 
#print(nav)
    #Print out all of the nav
for url in nav.find_all('a'):
    print(url.get('href'))
    #This will print all of the urls found in the navigation bar

#Finds double links for the mobile version and desktop nav bar 
print('-------------------------------------------------')
print('-------------------------------------------------')
body = soup
#for paragraph in body.find_all('p'):
    #print(paragraph.text)

#Looking for basic text paragraph data and this will do really well 

#for div in soup.find_all('div'):
    #print(div.text)
    #This will print out all of the div present in the code

for div in soup.find_all('div', class_= 'body'):
    print(div.text)
    #This will find all the text between div text 

