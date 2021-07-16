from lxml import etree
import requests
import re
import os
import time
import datetime

if not os.path.exists('文件/微博热点'):
    os.mkdir('微博热点')
for flag in range(10):
    now_time = datetime.datetime.now().strftime('%F_%H-%M')
    j=160303014771714
    for i in range(1,8):
        url='https://d.weibo.com/231650?pids=Pl_Discover_Pt6Rank__3&cfs=920&Pl_Discover_Pt6Rank__3_filter=&Pl_Discover_Pt6Rank__3_page=%d&ajaxpagelet=1&__ref=/231650&_t=FM_%d'%(i,j+(i-1)*4)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
                   "Cookie":'SUB=_2AkMX4SkMf8NxqwJRmP4TzGngbot_zQjEieKhvdjXJRMxHRl-yT8XqlAdtRB6PGEH42j78DXMbm5ljPXI66NGSG00aeVr; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFuPCkoOrOe7Gha7Tqx1pOG; _s_tentry=passport.weibo.com; Apache=6760606874465.538.1623041594762; SINAGLOBAL=6760606874465.538.1623041594762; ULV=1623041594896:1:1:1:6760606874465.538.1623041594762:',
                    'X-Requested-With': 'XMLHttpRequest'
                   }
        #s=requests.Session()
        html=requests.get(url=url,headers=headers)
        text=html.text
        #a=list()
        #text = re.sub('#[\u4e00-\u9fa5]*#'', '', text)
        #ex1='<span class=\"DSC_topicon\">(.*?)<\/span>'
        ranking=re.findall('\">\d{1,3}<',text,re.S)
        reading=re.findall('(>\d+\.?\d?\w{1} <)',text)
        category=re.findall('<\\\\/span>\\\\n\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\w{2,4}\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t\\\\t<\\\\/a>',text)
        k=0
        for z in category:
            #category[k]=re.sub(r'[^\u4e00-\u9fa5null]','',z)
            category[k]=re.sub('[^\u4e00-\u9fa5]','',z)
            if category[k]=='':
                category[k]='无'
            k+=1
        k=0
        for m in ranking:
            ranking[k]=re.sub('[^\d]+','',m)
            k+=1
        if i==1:
            list1=ranking[12:15]
            ranking=list1+ranking
            ranking = ranking[:15]
        else:
            ranking = ranking[:15]
        k=0
        for n in reading:
            reading[k]=re.sub('[^\w.]+','',n)
            k+=1
        #b = re.findall('#.{1,11}\d{0,8}\w{0,8}\d{0,3}\w+#', text)
        b = re.findall('#.{1,20}(?<!\.\.\.)#', text) #.*(?<!123)不匹配123结尾的字符串  (?!123).*不匹配123开头的字符串*
        topics = list(dict.fromkeys(b))
        with open('微博热点/'+str(now_time)+'.txt', 'a',encoding='gbk') as fp:
            for y in range(0,15):
                fp.write('排名：'+ranking[y]+' '*(8-len(ranking[y])))
                fp.write('类别：' + category[y]+' '*2*(5-len(category[y])))
                fp.write('话题：'+topics[y]+' '*2*(20-len(topics[y])))
                fp.write('阅读量：'+reading[y]+'\n')
            print(i,'爬取成功')

        time.sleep(2)
    time.sleep(600)


