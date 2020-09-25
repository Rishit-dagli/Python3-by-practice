from html.parser import HTMLParser

class PythonParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print('->', attr, '>', value)

parser = PythonParser()
for _ in range(int(input())):
    parser.feed(input())
parser.close()
