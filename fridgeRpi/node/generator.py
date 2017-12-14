'''
This file generates the HTML file based on the data(dictionary)
'''




def generate_table(data):
    data_html=''' '''
    full_table =''' '''
    for key in data:
        data_html='''<tr>
            <td><strong>'''+key+'''</strong></td>
            <td>'''+ str(data[key]) +'''</td>
            </tr>'''
        full_table = full_table + data_html;
    return full_table

#print(full_table)
def create_HTML(data):
    theHTML = '''<HTML>
    <link rel="stylesheet" href="http://192.168.141.143:8001/data_in_fridge.css" />
    <table>
      <thead>
        <tr>
          <th>Name of item</th>
          <th>Number of items present</th>
        </tr>
      </thead>
      <tbody>''' + str(generate_table(data))+ '''
      </tbody>
    </table>
    </HTML>'''
    return theHTML
def create_HTML_file(data):
    my_file=open("../node/data_in_fridge.html","w+")
    my_file.write(create_HTML(data))
    my_file.close()
    
if __name__=="__main__":
    data = {'banana': 1, 'tomato': 5, "milk": 2}
    create_HTML_file(data)

