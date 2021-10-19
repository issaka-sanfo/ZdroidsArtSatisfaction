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
#    print("{}: {}".format(count, line.strip()))

array = []
ListOfArray = []
paintList = [0]
NumberofPainting = count-1
print(NumberofPainting)

a_file = open("110_oily_portraits.txt", "r")

list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)

a_file.close()

a_file = open("110_oily_portraits.txt", "r")
list_of_lists = [(line.strip()).split() for line in a_file]
#list_of_lists
print("***********")

for line in Lines:
    lineStr = line  
    array = lineStr.split()
    ListOfArray.append(array)
#print(ListOfArray)

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

newlistPortrait = []
for i in range(0, len(newlist)-1, 2):
    strTagsArrays = []
    strTagsArrays = (str(newlist[i].get('tags'))+" "+str(newlist[i+1].get('tags'))).split()
    setTagsArray = list(set(strTagsArrays))
    setTagsArray.sort()
    paintingPortrait = {
                        'index' : str(newlist[i].get('index'))+" "+str(newlist[i+1].get('index')),
                        'tags' : setTagsArray
                    }
    newlistPortrait.append(paintingPortrait)


df = pd.DataFrame.from_dict(newlistPortrait)

result_Sorted = df.sort_values(by=['tags'], ascending=False)

list_of_paintings = result_Sorted['index'].to_list()

reversed_list = list_of_paintings[::-1]

with open(sys.argv[2], 'w') as filehandle:
    filehandle.write('%s\n' % NumberofPainting)
    for listitem in list_of_paintings:
        filehandle.write('%s\n' % listitem)




