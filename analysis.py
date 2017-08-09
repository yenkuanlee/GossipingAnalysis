# -*- coding: UTF-8 -*-
# Kevin Yen-Kuan Lee
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
Adict = dict()

def getPage(Gurl):
        content = requests.get(
            #url= 'https://www.ptt.cc/bbs/' + board + '/index'+str(index)+'.html',
            url=Gurl,
            cookies={'over18': '1'}
        ).content.decode('utf-8')
        #content = content.replace("\n","")
        return content

def AnalysisOnePage(Gurl):
    global Adict
    owo = Gurl.split("/")
    Aid = owo[len(owo)-1]
    Adict[Aid] = dict()
    content = getPage(Gurl)
    tmp = content.split("push-tag\">")
    p = 0
    b = 0
    for i in range(1,len(tmp),1):
        method = tmp[i].split(" ")[0]
        if method == "推":
            p += 1
        elif method == "噓":
            b += 1
        if p-b>50:
            break
        person = tmp[i].split("push-userid\">")[1].split("<")[0]
        if person not in Adict[Aid]:
            Adict[Aid][person]= dict()
        if method not in Adict[Aid][person]:
            Adict[Aid][person][method] = 1
        else:
            Adict[Aid][person][method] += 1
        #print method+"\t"+person

f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    tmp = line.split("\t")
    AnalysisOnePage(tmp[0])

import json
print json.dumps(Adict)
'''
PersonDict = dict()
for x in Adict:
    for y in Adict[x]:
        if y not in PersonDict:
            PersonDict[y] = 1
        else:
            PersonDict[y] += 1
#for x in PersonDict:
#    print x,PersonDict[x]

import operator
sorted_x = sorted(PersonDict.items(), key=operator.itemgetter(1))
for x in sorted_x:
    print x
'''
