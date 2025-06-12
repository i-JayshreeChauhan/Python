from html.parser import HTMLParser


pattern1 = "<!--"
pattern2 = "-->"

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        #find '\n'
        in2 = data.find("\n")

        if(in2==-1):
            print(">>> Single-line Comment")
            print(data)
        else:
            print(">>> Multi-line Comment")
            print(data)


    def handle_data(self, data):
        if data.strip() :   #non whitespace char
            print(">>> Data")
            print(data)



  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()