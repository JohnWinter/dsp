import re
import csv
import pprint


f = open(r'/Users/jennilee09/ds/metis/prework/dsp/python/faculty.csv')


email_string= ""

for line in f:
    email_string+=line


findemails=re.findall(r"[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}",email_string) # took regex expression from http://code.activestate.com/recipes/138889-extract-email-addresses-from-files/


efile = open(r'/Users/jennilee09/ds/metis/prework/dsp/python/emails.csv','wb')
writer = csv.writer(efile)
for item in findemails:

    writer.writerow([item])

