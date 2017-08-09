# -*- coding: UTF-8 -*-
# Kevin Yen-Kuan Lee
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = open('JsonResult.txt','r')
Adict = dict()
while True:
    line = f.readline()
    if not line:
        break
    Adict = json.loads(line)
    break

def GotYou(person):
    Psum = 0
    Bsum = 0
    Nsum = 0
    global Adict
    for x in Adict:
        if person in Adict[x]:
            for y in Adict[x][person]:
                if y == "推":
                    Psum += Adict[x][person][y]
                elif y== "噓":
                    Bsum += Adict[x][person][y]
                else:
                    Nsum += Adict[x][person][y]
    return Psum,Bsum,Nsum

def SortPersonByPushArticles():
    global Adict
    PersonDict = dict()
    for x in Adict:
        for y in Adict[x]:
            if y not in PersonDict:
                PersonDict[y] = 1
            else:
                PersonDict[y] += 1

    import operator
    sorted_x = sorted(PersonDict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_x
    #for i in range(10):
    #    print sorted_x[i],GotYou(sorted_x[i][0])

SPBPA = SortPersonByPushArticles()
for i in range(10):
    SSS = GotYou(SPBPA[i][0])
    print SPBPA[i],SSS


for x in Adict:
    Pmax = 0
    Who = ""
    for y in Adict[x]:
        for z in Adict[x][y]:
            if z=="推":
                if Adict[x][y][z] > Pmax:
                    Pmax = Adict[x][y][z]
                    Who = y
    if Pmax > 10:
        print x,Who,Pmax
'''
Mset = set()
FA = ""
SA = ""
for x in Adict:
    for y in Adict:
        if x==y:
            continue
        tmpX = set(Adict[x].keys())
        tmpY = set(Adict[y].keys())
        Intersection = tmpX & tmpY
        if len(Intersection) > len(Mset):
            Mset = Intersection
            FA = x
            SA = y
print Mset
print FA
print SA
'''


'''
Pset = set()
for x in Adict:
    for y in Adict[x]:
        Pset.add(y)
print len(Pset)

cnt = 0
for x in Pset:
    print x
    if cnt>10:
        break
    cnt += 1
'''
