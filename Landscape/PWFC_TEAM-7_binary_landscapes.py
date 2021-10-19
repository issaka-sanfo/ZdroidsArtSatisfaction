import pandas as pd
import numpy as np
import sys

if len( sys.argv ) == 1:
    print( "Python Week | TEAM 7" )
    print( "Please, give 2 arguments: 1-For input file name 2-For output file name" )
    exit()

file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
 
count = 0
for line in Lines:
    count += 1

array = []
ListOfArray = []
paintList = [0]
NumberofPainting = count-1
print(NumberofPainting)
print("***********")

for line in Lines:
    lineStr = line  
    array = lineStr.split()
    ListOfArray.append(array)

del ListOfArray[0]

newlist = []
length = len(ListOfArray)
for i in range(length):
    strArray = []
    strArray = ListOfArray[i][2:]
    strArray.sort()
    painting = {
                    'index' : i,
                    'typ' : ListOfArray[i][0],
                    'num' : ListOfArray[i][1],
                    'tags' : strArray
                }
    newlist.append(painting)

df = pd.DataFrame.from_dict(newlist)

result_Sorted = df.sort_values(by=['tags'], ascending=False)

list_of_paintings = result_Sorted['index'].to_list()

reversed_list = list_of_paintings[::-1]

a = len(list_of_paintings)
list_of_paintings.insert(0,a)

with open(sys.argv[2], 'w') as filehandle:
    for listitem in list_of_paintings:
        filehandle.write('%s\n' % listitem)



