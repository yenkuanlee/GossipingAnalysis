# -*- coding: UTF-8 -*-
# Kevin Yen-Kuan Lee
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getLastPage(board):
        content = requests.get(
            url= 'https://www.ptt.cc/bbs/' + board + '/index.html',
            cookies={'over18': '1'}
        ).content.decode('utf-8')
        first_page = re.search(r'href="/bbs/' + board + '/index(\d+).html">&lsaquo;', content)
        if first_page is None:
            return content,1
        return content,int(first_page.group(1)) + 1

def getPage(board,index):
        content = requests.get(
            url= 'https://www.ptt.cc/bbs/' + board + '/index'+str(index)+'.html',
            cookies={'over18': '1'}
        ).content.decode('utf-8')
        #content = content.replace("\n","")
        return content
content0,pid = getLastPage("Gossiping")

#print content0

for k in range(1000):
    content = getPage("Gossiping",pid-k)
    tmp = content.split("<div class=\"r-ent\">")
    #tmp = content.split("<div class=\"title\">")
    for i in range(1,len(tmp),1):
        try:
            tmpp = tmp[i].split("<a href=\"")[1].split("</a>")[0].split("\">")
            lower_name = tmpp[1].lower()
            OO = tmp[i].split("<a href=\"")[1].split("</a>")[0].split("\">")
            date = tmp[i].split("<div class=\"date\"> ")[1].split("<")[0]
            author = tmp[i].split("<div class=\"author\">")[1].split("<")[0]
            comment = tmp[i].split("\">")[2].split("<")[0]
            if comment == "爆":
                comment = "100"
            if int(comment) < 50 :
                continue
            print "https://www.ptt.cc"+OO[0]+"\t"+date+"\t"+author+"\t"+comment+"\t"+OO[1]
        except:
            pass
