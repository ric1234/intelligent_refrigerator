'''This file has the method of making the dictionary'''

#How to use the datastructure
'''
import data_present as dat
foodItems = []
foodItems.append(itemDetected)
dat.addToDictionary(foodItems)
'''

exampleFoodItems = ['egg', 'banana', 'tomato', 'egg']

def addToDictionary(foods):
    counter = dict()
    for k in foods:
        if not k in counter:
            counter[k] = 1
        else:
            counter[k] += 1
            
    #counter['soy']+=10
    #print(str(counter))
    return (counter)
    #Write counter to a file
    #print(foods)

if __name__ == "__main__":
    addToDictionary(exampleFoodItems)
