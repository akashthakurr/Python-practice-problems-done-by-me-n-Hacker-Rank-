from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        for i in attr:
            print(f'-> {i[0]} > {i[1]}')
   
html=""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
                
parser = MyHTMLParser()
parser.feed(html)
parser.close()