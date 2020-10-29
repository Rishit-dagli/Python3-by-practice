import bs4 as bs 
    #bs4 is beautiful soap which pulls data drom HTML and XML files 
    #Also used for navigating, searching. and modifying code
import urllib.request
    # ALlows for request to be sent to HTTP websites and so on 
sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
    #this will return all of the source code and very messy

soup = bs.BeautifulSoup(sauce, "lxml") 
    #can be use lxml or httplib5
    #used to make BS object 
#print(soup)
    #This part of the code will only print out source code of the website
    #A little neater than sauce 
#print(soup.title)
    #will give you the title of the website
#print(soup.title.name)
    #give you the title tage 
#print(soup.title.string)
    # Gives you the title as a string and not object
#print(soup.p)
    #Will first out the first paragraph element 
#print(soup.find_all('p'))
    #This will print all of the paragraphs in the website
#Good for our project
#for paragraph in soup.find_all('p'):
    #print(paragraph.string)
        #This will look for paragraphs in a website and from there it will only print out string from the paragraph
        #Will return None because there are children tags 
        #children tags are things within HTML code 
#print(soup.get_text())
    #This will print the whole webpage 
    #Pick up other elements that are not paragraphs and other HTML elements 
    #Good techinque to get all of the text present on a one webpage

#Finding URL 
for url in soup.find_all('a'):
    print(url.get('href'))
        #This will print out just the links that you will need

#This is more advance techiques 