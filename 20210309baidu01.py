import requests
import re
#  爬虫部分，主要是请求头，url，获取文本
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
keywords = '茅台'
url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=阿里巴巴'
res = requests.get(url, headers=headers).text
print(res)
#  正则表达式部分主要是筛选数据，清洗数据
p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)" target.*?<!--s-text-->'
p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
href = re.findall(p_href, res, re.S)
title = re.findall(p_title, res, re.S)
biaoti = []

for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    biaoti.append(title[i])
    print(str(i+1)+'.'+biaoti[i])
    print(href[i])

