from html.parser import HTMLParser
N = int(input())
html = ""
for i in range(0,N):
    html += input()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start : {}".format(tag))
#        print("Attributes : {}".format(attrs))
        if(len(attrs)):
            for a,b in attrs:
                print("-> {} > {}".format(a,b))
    def handle_endtag(self, tag):
        print ("End   : {}".format(tag))
    def handle_startendtag(self, tag, attrs):
        print ("Empty : {}".format(tag))
        if(len(attrs)):
#           print("Came in attrs")
            for a,b in attrs:
                print("-> {} > {}".format(a,b))

parser = MyHTMLParser()
parser.feed(html)
