import requests
import re
url = 'https://weixin.sogou.com/weixin?type=2&s_from=input&query=思维导图ie=utf8&_sug_=y&_sug_type_' \
      '=&w=01019900&sut=4944&sst0=1615279959697&lkt=0%2C0%2C0'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
res = requests.get(url, headers=headers).text
biaoti = []
#  正则表达式提取数据，清洗数据
w_gzh = '<div class="s-p".*?data-isV="0" uigs=".*?">(.*?)</a>'
w_title = '<!--red_beg-->(.*?)</a>'
w_href = '<a target="_blank" href="(.*?) id="sogou'

gzh = re.findall(w_gzh, res, re.S)
title = re.findall(w_title, res, re.S)
href = re.findall(w_href, res, re.S)
for i in range(len(gzh)):
    title[i] = re.sub('<.*?>', '', title[i])
    biaoti.append(title[i])
    print(str(i+1)+'.'+biaoti[i]+'('+gzh[i]+')')
    print(href[i])
    print('-----------------')


