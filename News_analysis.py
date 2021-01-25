import requests
import re
from bs4 import BeautifulSoup
import tornado.web
import tornado.ioloop



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('news.html',x="",longhu="",longhu1="",hangye="",jigou="")

    def post(self):
        header={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'cmsad_170_0=0; searchGuide=sg; cmsad_171_0=0; cmsad_172_0=0; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1611035533,1611041181,1611043393,1611110051; Hm_lvt_22a3c65fd214b0d5fd3a923be29458c7=1611110052; spversion=20130314; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1611110057; historystock=603799%7C*%7C300595; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1611112751; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1611112751; Hm_lpvt_22a3c65fd214b0d5fd3a923be29458c7=1611112751; v=A5UXQQnsWdMdtn0vJAqbQWQMpJpMkkmiE0Yt-Rc6UYxbbrvM3-JZdKOWPdGk',
        'Host': 'stockpage.10jqka.com.cn',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://stockpage.10jqka.com.cn/000001/news/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
               } 
        
        header1={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}

        announcement=requests.get('http://guba.eastmoney.com/list,'+self.get_argument("StockNumber")+',3,f.html')
        #公告信息
        Longhudata=requests.get("http://data.eastmoney.com/stock/lhb/"+self.get_argument("StockNumber")+'.html')
        #龙虎榜单
        hangye=requests.get("http://stockpage.10jqka.com.cn/ajax/code/"+self.get_argument("StockNumber")+"/type/news/",headers=header)
        #行业新闻
        jigou=requests.get("http://basic.10jqka.com.cn/"+self.get_argument("StockNumber")+"/position.html",headers=header1)
        #机构持仓

        y=""
        z=""
        hangye1=""
        if announcement.status_code==200 and Longhudata.status_code==200 and hangye.status_code==200 and jigou.status_code==200:
            soup1=BeautifulSoup(announcement.content,'html.parser',from_encoding='gb18030')
            soup2=BeautifulSoup(Longhudata.content,'html.parser',from_encoding='gb18030')
            soup3=BeautifulSoup(hangye.content,'html.parser',from_encoding='gb18030')
            soup4=BeautifulSoup(jigou.content,'html.parser',from_encoding='gb18030')
            data=""
            data1=""
            n=0
            y=soup2.find_all(id="tab-2")
            z=soup2.find_all(id="tab-4")
            hangye1=soup3.find_all('div',id="news")
            jigou1=soup4.find_all(id="organ_1")
            for table1 in jigou1:
                if table1!=None:
                    jigou2=table1.table
            """ for i in soup.find_all(class_='l3 a3'):
                a=i.a
                if a!=None:
                    con=a.get("title")
                    add="http://guba.eastmoney.com/"+a.get("href")
                    data1=con+add
                data=data+data1
                n=n+1 """
            self.render('news.html',x=soup1.find_all(class_='l3 a3'),longhu=y,longhu1=z,hangye=hangye1,jigou=jigou2)
        else: 
            self.render('news.html',x="查询失败")
        



#hygy=requests.get('http://guba.eastmoney.com/list,603799,3,f.html')
#soup=BeautifulSoup(hygy.content,'html.parser',from_encoding='gb18030')
#for x in soup.find_all('a',string=re.compile('603799')):
    #print(x)
#print(soup.find_all(class_='l3 a3'))
#print(type(soup.find_all(class_='l3 a3')))

application=tornado.web.Application([(r'/',MainHandler)])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8888)
tornado.ioloop.IOLoop.instance().start()
