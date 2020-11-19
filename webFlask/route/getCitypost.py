# -*- coding: utf-8 -*-
from urllib import  request
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
           'cookie':"cookie_val = 'lastCity=101280600; __zp_seo_uuid__=d59649f5-bc8a-4263-b4e1-d5fb1526ebbe; __c=1592469667; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1592469673; __l=l=%2Fwww.zhipin.com%2Fshenzhen%2F&r=https%3A%2F%2Fwww.google.com%2F&friend_source=0&friend_source=0; toUrl=https%3A%2F%2Fwww.zhipin.com%2F%2Fjob_detail%2F3f35305467e161991nJ429i4GA%7E%7E.html; __a=43955211.1592469667..1592469667.39.1.39.39; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592530438; __zp_stoken__=7f3aaPCVBFktLe0xkP21%2BJSFCLWILSwx7NEw4bVJkRx8pdBE3JGNmWjVwdx5PXC8rHmN%2BJB0hX1UvTz5VPyMmOhIVHBglVzoxJQIdLQtKR3ZFBFIeazwOByVndHwXBAN%2FXFo7W2BffFxtXSU%3D; __zp_sseed__=Ykg0aQ3ow1dZqyi9KmeVnWrqZXcZ32a4psiagwqme3M=; __zp_sname__=93bf4835; __zp_sts__=1592530514188'"}
# 代理IP地址
proxy="http://58.220.95.30:10174"

proxy_support=request.ProxyHandler({'http':proxy})
opener = request.build_opener(proxy_support)
request.install_opener(opener)

def getcc(citynumber,position):
    url = "https://www.zhipin.com/" + citynumber + "/?query="+position+"&page=1&ka=page-1"
    resp = request.Request(url, headers=headers)
    html = request.urlopen(resp)
    html=html.read().decode('utf-8')
    print(html)

    soup = BeautifulSoup(html,"html.parser")
    joblist = soup.select_one('.job-list')

    for li in joblist.select('li'):

        jobName = li.select_one('.job-name a').get_text()
        joblimit = li.select_one('.job-limit')
        jobSalary = joblimit.select_one('.red').get_text()
        condition = joblimit.select_one('p').get_text()
        technology = li.select('.tag-item')
        welfare = li.select_one('.info-desc').get_text()
        techlist = []
        for t in technology:
           con =  t.get_text()
           techlist.append(con)
        print(jobName)
        print(joblimit)
        print(jobSalary)
        print(condition)
        print(welfare)
        print(techlist)

if __name__ == '__main__':
    getcc('c101020100','python')