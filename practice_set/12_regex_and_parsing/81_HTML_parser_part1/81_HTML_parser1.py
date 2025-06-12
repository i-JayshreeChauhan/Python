from html.parser import HTMLParser

"""
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html

"""

text = ""

for i in range (int(input())):
    line = input()
    text = text +"\n" + line

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        #attributes are (name,value) in a list form
        for i in attrs:
            name , value = i
            print(f"-> {name} > {value}")
            

    def handle_endtag(self, tag):
        print("End   :", tag)

    #def handle_data(self, data):
       # print("Encountered some data  :", data)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        #attributes are (name,value) in a list form
        for i in attrs:
            name , value = i
            print(f"-> {name} > {value}")

parser = MyHTMLParser()
parser.feed(text)