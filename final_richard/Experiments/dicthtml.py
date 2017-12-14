count=1
theHTML = '''<HTML> <H1>
	'''+count+'''
</HTML>'''
def create_HTML():
    my_file=open("index.html","w+")
    my_file.write(theHTML)
    my_file.close()
    
if __name__=="__main__":
    create_HTML()