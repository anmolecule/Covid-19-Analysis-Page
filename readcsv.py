import os,sys
import pandas
import re
import numpy
dframe = pandas.read_csv(sys.argv[1])
with open(sys.argv[2],"r") as cap:
    capitals=cap.readlines()
with open(sys.argv[3],"r") as temp:
    temps=temp.readlines()
caseframe = pandas.read_csv(sys.argv[4])
capital=[]
for capname in capitals:
    capital.append(re.sub('\W+','',capname))
temperature=[]
for t in temps:
    tp = t.split()[0]
    try:
        tp=int(tp)
    except ValueError:
        tp=tp
    temperature.append(tp)
#print (temperature)

inserttemp = []
for i in range(len(dframe['country'])):
    csvcapname = dframe['capital'][i]
    csvcapname = re.sub('\W+','',csvcapname)
    if csvcapname in capital:
        inserttemp.append(temperature[capital.index(csvcapname)])
    else:
        inserttemp.append('N/A')
cntlist= (list(caseframe['Country/Region']))
whocntlist = []
for c in cntlist:
    cname = '-'.join(c.split())
    cname = re.sub('\W+','',cname)
    cname = cname.upper()
    whocntlist.append(cname)

cases=(list(caseframe['3/5/2020']))

insertcase = []
for i in range(len(dframe['country'])):
    cname = "-".join(dframe['country'][i].split())
    cname = re.sub('\W+','',cname)
    cname = cname.upper()
    if cname in whocntlist:
        insertcase.append(cases[whocntlist.index(cname)])
    else:
        insertcase.append('N/A')

dframe.insert(3, "Temperature", inserttemp, True)
dframe.insert(4, "Cases", insertcase, True)

dframe.to_csv(r'final.csv', index = False,header=True)
for i in range(len(dframe.index)):
    if dframe['Temperature'][i] == 'N/A' or dframe['Cases'][i] =='N/A':
        dframe.drop(dframe.index[i])
print (dframe)
x = list(dframe['Temperature'])
y = list(dframe['Cases'])
fo=open("final_sort.csv","w")
fo.write("Temp,Case\n")

for i in range(len(x)):
    try:
        n=int(x[i])
        m=int(y[i])
        fo.write("%s,%s\n"%(n,m))
    except ValueError:
        continue
    #if x[i]== 0 or y
    #print (i)
#import matplotlib.pyplot as plt
#plt.plot(x,y)
##print (dframe)
