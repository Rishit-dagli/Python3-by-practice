#This will cover scarping for tables and XML  
import bs4 as bs 
import urllib.request
import pandas as pd

sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = bs.BeautifulSoup(sauce, "lxml") 

#different ways of getting tables text
#table = soup.table 
table = soup.find('table')
#print(table)
    #This will print out all the tables with tr and th tags

table_rows = table.find_all('tr')

#for tr in table_rows:
 #   td = tr.find_all('td')
  #  row = [i.text for i in td]
   # print(row)
#This code will print out all the content in a table 

#pandas verision of doing this process 
#dfs = pd.read_html("https://pythonprogramming.net/parsememcparseface/", header =0)
#contains dataframes for the website
#for df in dfs:
 #   print(df)

#This part is about XML Documents
#XML -> human and machine readale 
#Used on news websites 

sauce1 = urllib.request.urlopen("https://pythonprogramming.net/sitemap.xml").read()
soup1 = bs.BeautifulSoup(sauce, "xml") 
for url in soup1.find_all('loc'):
    print(url.text)

