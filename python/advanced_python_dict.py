

f = open(r'/Users/jennilee09/ds/metis/prework/dsp/python/faculty.csv')

mylist=[]
last_keys=[]
last_dic={}

for line in f: #convert string into a list of lists
    mylist.append(line.split(","))

i=1
while i<len(mylist): #isolatae the unique last names as keys and append data to keys
    mylist[i][0] =mylist[i][0].split(" ")
    if len(mylist[i][0])>2:
        last_name = mylist[i][0][2]
    else:
        last_name = mylist[i][0][1]
    mylist[i][2] = mylist[i][2].split(" ")
    if mylist[i][2][0] == "Professor":
        title = "Professor"
    else:
        title = str(mylist[i][2][0]+" "+mylist[i][2][1])
    try:

        last_dic[last_name].append(str(mylist[i][1]+","+title+","+mylist[i][3]).replace("\n","").split(","))
    except KeyError:
        last_dic[last_name] = []
        last_dic[last_name].append(str(mylist[i][1]+","+title+","+mylist[i][3]).replace("\n","").split(","))
    i +=1




#pprint.pprint(last_dic)
#####
f = open(r'/Users/jennilee09/ds/metis/prework/dsp/python/faculty.csv')

mylist=[]
last_keys=[]
first_dic={}

for line in f: #convert string into a list of lists
    mylist.append(line.split(","))

i=1
while i<len(mylist): #isolatae the unique last names as keys and append data to keys
    mylist[i][0] =mylist[i][0].split(" ")
    if len(mylist[i][0])>2:
        name = tuple(str(mylist[i][0][0]+","+mylist[i][0][2]).split(","))
    else:
        name = tuple(str(mylist[i][0][0]+","+mylist[i][0][1]).split(","))
    mylist[i][2] = mylist[i][2].split(" ")
    if mylist[i][2][0] == "Professor":
        title = "Professor"
    else:
        title = str(mylist[i][2][0]+" "+mylist[i][2][1])
    try:

        first_dic[name].append(str(mylist[i][1]+","+title+","+mylist[i][3]).replace("\n","").split(","))
    except KeyError:

        first_dic[name] = str(mylist[i][1]+","+title+","+mylist[i][3]).replace("\n","").split(",")
    i +=1




pprint.pprint(first_dic)

#####

f = open(r'/Users/jennilee09/ds/metis/prework/dsp/python/faculty.csv')

mylist=[]
last_keys=[]
last_dic={}

for line in f: #convert string into a list of lists
    mylist.append(line.split(","))

i=1
while i<len(mylist): #isolatae the unique last names as keys and append data to keys
    mylist[i][0] =mylist[i][0].split(" ")
    if len(mylist[i][0])>2:
        name = tuple(str(mylist[i][0][2]+","+mylist[i][0][0]).split(","))
    else:
        name = tuple(str(mylist[i][0][1]+","+mylist[i][0][0]).split(","))
    mylist[i][2] = mylist[i][2].split(" ")
    if mylist[i][2][0] == "Professor":
        title = "Professor"
    else:
        title = str(mylist[i][2][0]+" "+mylist[i][2][1])
    try:

        last_dic[name].append(str(mylist[i][1]+","+title+","+mylist[i][3]).replace("\n","").split(","))
    except KeyError:

        last_dic[name] = str(mylist[i][1]+","+title+","+mylist[i][3]).replace("\n","").split(",")
    i +=1




pprint.pprint(last_dic)