from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in attrs:
                name , val = i
                print(f"-> {name} > {val}")
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in attrs:
                name , val = i
                print(f"-> {name} > {val}")
    
    def handle_comment(self, data):
        #dont do anything
        abc = data
        pass
    


text = ""

for i in range (int(input())):
    line = input()
    text = text +"\n" + line


parser = MyHTMLParser()
parser.feed(text)