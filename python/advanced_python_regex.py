###
import re

f = open(r'/Users/jennilee09/ds/metis/prework/dsp/python/faculty.csv')


mylist=[]
degree_list=[]
degree_dic={}
degree_dic["PHD"]=0
degree_dic["SCD"]=0
degree_dic["MD"]=0
degree_dic["MPH"]=0
degree_dic["BSED"]=0



for line in f: #convert string into a list of lists
    mylist.append(line.split(","))


i=1
while i<len(mylist): #isolatae the degree entries
    mylist[i][1] =mylist[i][1].strip()
    degree_list.append(mylist[i][1].split(" "))


    i +=1

for item in degree_list:
    if len(item)>1:
        for subitem in item:
            if re.search("[P][Hh][\.D]",subitem):
                degree_dic["PHD"]+=1
            if re.search("[Ss][\.cC][\.Dd]",subitem):
                degree_dic["SCD"]+=1
            if re.search("[Mm][\.dD]",subitem):
                degree_dic["MD"]+=1
            if re.search("[Mm][\.Pp][\.Hh]",subitem):
                degree_dic["MPH"]+=1
            if re.search("[Bb][\.Ss][\.SsEe][\.EeDd]",subitem):
                degree_dic["BSED"]+=1
    else:
        if re.search("[P][Hh][\.D]",str(item)):
            degree_dic["PHD"]+=1
        if re.search("[Ss][\.cC][\.Dd]",str(item)):
            degree_dic["SCD"]+=1
        if re.search("[Mm][\.dD]",str(item)):
            degree_dic["MD"]+=1
        if re.search("[Mm][\.Pp][\.PpHh][\.Hh]",str(item)):
            degree_dic["MPH"]+=1
        if re.search("[Bb][\.Ss][\.SsEe][\.EeDd]",str(item)):
            degree_dic["BSED"]+=1



print(degree_dic)

###

import re

f = open(r'/Users/jennilee09/ds/metis/prework/dsp/python/faculty.csv')


mylist=[]
title_list=[]
title_dic={}
title_dic["Professor"]=0
title_dic["Assistant Professor"]=0
title_dic["Assocaite Professor"]=0




for line in f: #convert string into a list of lists
    mylist.append(line.split(","))


i=1
while i<len(mylist): #isolatae the degree entries
    mylist[i][2] =mylist[i][2].split(" ")
    title_list.append(mylist[i][2][0])


    i +=1

for item in title_list:
    if re.search("Professor",item):
        title_dic["Professor"]+=1
    if re.search("Assistant",item):
        title_dic["Assistant Professor"]+=1
    if re.search("Associate", item):
        title_dic["Assocaite Professor"]+=1





print(title_dic)

###

import pprint
import re

f = open(r'/Users/jennilee09/ds/metis/prework/dsp/python/faculty.csv')

email_string= ""

for line in f:
    email_string+=line


findemails=re.findall(r"[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}",email_string) # took regex expression from http://code.activestate.com/recipes/138889-extract-email-addresses-from-files/

pprint.pprint(findemails)
###


import re

f = open(r'/Users/jennilee09/ds/metis/prework/dsp/python/faculty.csv')

email_string= ""

uniques=[]
for line in f:
    email_string+=line


findemails=re.findall(r"@[\w\-][\w\-\.]+[a-zA-Z]{1,4}",email_string) # took regex expression from http://code.activestate.com/recipes/138889-extract-email-addresses-from-files/

for item in findemails:
    if item not in uniques:
        uniques.append(item)

pprint.pprint(uniques)