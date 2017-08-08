# -*- coding: UTF-8 -*-
# Kevin Yen-Kuan Lee
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getPage(Gurl):
        content = requests.get(
            #url= 'https://www.ptt.cc/bbs/' + board + '/index'+str(index)+'.html',
            url=Gurl,
            cookies={'over18': '1'}
        ).content.decode('utf-8')
        #content = content.replace("\n","")
        return content

print getPage("https://www.ptt.cc/bbs/Gossiping/M.1502180327.A.01A.html")
