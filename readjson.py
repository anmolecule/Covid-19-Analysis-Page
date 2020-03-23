import os,sys
import urllib,json
import urllib.request
cci={}
with open(sys.argv[1],"r") as txt_file:
    data = txt_file.readlines()
    key = data[0].strip().split(';')
    for d in data[1:]:
        val = d.strip().split(';')
        for i in range(len(val)):
            val[i]=val[i].strip('"')
        if val[0] in cci.keys():
            cci[val[0]].append([val[1],val[2]])
        else:
            cci.update({val[0]:[]})
            cci[val[0]].append([val[1],val[2]])
m=0
for key,val in cci.items():
    n=0
    m=m+1
    print ("Collecting ",key,"'s temperature info")
    jancountry=0
    febcountry=0
    for i in range(len(val)):
        url="https://worldweather.wmo.int/en/json/"+str(val[i][1])+"_en.json"
        urldata = urllib.request.urlopen(url)
        jsondata = json.loads(urldata.read())
        try:
            jantempmax= jsondata["city"]["climate"]["climateMonth"][0]['maxTemp']
            jantempmin= jsondata["city"]["climate"]["climateMonth"][0]['minTemp']
            febtempmax= jsondata["city"]["climate"]["climateMonth"][1]['maxTemp']
            febtempmin= jsondata["city"]["climate"]["climateMonth"][1]['minTemp']
            try:
               jantemp=round((round(float(jantempmax),1)+round(float(jantempmin),1))/2,1)
               febtemp=round((round(float(febtempmax),1)+round(float(febtempmin),1))/2,1)
               jancountry=jancountry+jantemp
               febcountry=febcountry+febtemp
               n=n+1
               print ("    City: ",val[i][0]," Avg Temp.: ",jantemp)
            except (TypeError,ValueError):
               jantemp=febtemp="NA"
               n=n
               pass
        except (KeyError,IndexError):
            n=n
            jantemp=febtemp="NA"
        cci[key][i].append(jantemp)
        cci[key][i].append(febtemp)
    if n==0:
        jancountry=febcountry="NA"
    else:
       jancountry=round(jancountry/n,1)
       febcountry=round(febcountry/n,1)
       print ("Country: ",key," Avg Temp.: ",jancountry)

    cci[key].append([jancountry,febcountry])

json.dump(cci, open("temperature.json",'w'))
#d2 = json.load(open("text.txt"))
#m=0
#for key,val in cci.items():
#    print (key,val)
#    m=m+1
#    if m==10:break


