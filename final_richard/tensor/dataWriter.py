'''
This function is used by the main file to
write the output from the main to a txt file.
This text file will be sent out to the coap client
'''
def create_text(data):
    my_file=open("../aiocoap/data.txt","w+")
    my_file.write(data)
    my_file.close()
    
if __name__=="__main__":
    create_text(data)