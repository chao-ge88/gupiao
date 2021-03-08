import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
           }
url = 'https://www.baidu.com/s?tn=news&rtt=lbsst=1&c1=2&wd=阿里巴巴'
res = requests.get(url, headers=headers).text
print(res)


