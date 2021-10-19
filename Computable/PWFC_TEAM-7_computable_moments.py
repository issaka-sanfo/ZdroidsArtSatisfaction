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

newlistPortrait = []
newlistLandscape = []
arrayPortrait = []
length = len(ListOfArray)
for i in range(length):
    if ListOfArray[i][0] == "L":
        strArray = []
        strArray = ListOfArray[i][2:]
        strArray.sort()
        paintingLanscape = {
                        'index' : i,
                        'tags' : strArray
                    }
        newlistLandscape.append(paintingLanscape)

    else:
        tempArray = ['','','','']
        tempArray[0] = i
        tempArray[1] = ListOfArray[i][0]
        tempArray[2] = ListOfArray[i][2]
        tempArray[3] = ListOfArray[i][2:]
        arrayPortrait.append(tempArray)
sortedPortraits = sorted(arrayPortrait, key=lambda x: x[3])
        

for i in range(0, len(sortedPortraits)-1, 2):
    strTagsArrays = []
    setTagsArray = []
    strTagsArrays = (str(sortedPortraits[i][3])+" "+str(sortedPortraits[i+1][3])).split()
    setTagsArray = list(set(strTagsArrays))
    setTagsArray.sort()
    paintingPortrait = {
                        'index' : str(sortedPortraits[i][0])+" "+str(sortedPortraits[i+1][0]),
                        'tags' : setTagsArray
                    }
    newlistPortrait.append(paintingPortrait)

listMerged = newlistPortrait + newlistLandscape
df = pd.DataFrame.from_dict(listMerged)

result_Sorted = df.sort_values(by=['tags'], ascending=False)

list_of_paintings = result_Sorted['index'].to_list()

reversed_list = list_of_paintings[::-1]

a = NumberofPainting
list_of_paintings.insert(0,a)

increment = 0
with open(sys.argv[2], 'w') as filehandle:
    for listitem in list_of_paintings:
        filehandle.write('%s\n' % listitem)