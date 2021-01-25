import requests
import re
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import tornado.web
import tornado.ioloop
cookies='searchGuide=sg; usersurvey=1; log=; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1611035085,1611035533,1611041181; reviewJump=nojump; v=Azy-yiiLcMmCf0SVVm2iahXDDdHtNeBfYtn0Ixa9SCcK4dLHPkWw77LpxLdl'

header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
               } 
        

hygy=requests.get('http://basic.10jqka.com.cn/603882/position.html',headers=header)
hygy.encoding='utf-8'
print(hygy.status_code)
soup=BeautifulSoup(hygy.content,'html.parser',from_encoding='gb18030')
#print("data:"+str(data))

#print(hygy.text)
#print(soup.contents)
for x in soup.find_all(id="organ_1"):
    if x!=None:
        print(x.table)
    #print(type(x.a))

#print(soup.find_all(class_='l3 a3'))
#print(type(soup.find_all(class_='l3 a3')))
#print(str(soup.find_all('a',string=re.compile('603799'))))