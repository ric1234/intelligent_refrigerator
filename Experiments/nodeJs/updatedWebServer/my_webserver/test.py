count=1
theHTML = '''<!DOCTYPE html>
<html>
<body>

<h1>Success</h1>


</body>
</html> 
'''
def create_HTML():
    my_file=open("index.html","w+")
    my_file.write(theHTML)
    my_file.close()
    
if __name__=="__main__":
    create_HTML()