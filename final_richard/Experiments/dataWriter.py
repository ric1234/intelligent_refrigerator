def create_text(data):
    my_file=open("/home/pi/Desktop/final/aiocoap/data.txt","w+")
    my_file.write(data)
    my_file.close()
    
if __name__=="__main__":
    create_text(data)