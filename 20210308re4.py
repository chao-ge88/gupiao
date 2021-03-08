import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
           }
url = 'https://www.163.com/dy/article/G4IR0BSG0519EI0N.html'
res = requests.get(url, headers=headers).text

p_res2 = '<a.*?>(.*?)</a>'
b = re.findall(p_res2, res)
print(b)
for i in range(len(b)):
    b[i].strip()
    c = b[i].strip()
    print(c)