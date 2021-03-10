import requests
import re
#  爬虫部分，主要是请求头，url，获取文本
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}


def baidu(company, page):
    num = (page-1)*10
    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=' + company + \
          '&medium=0&x_bfe_rqs=03E80000001&x_bfe_tjscore=0.100000&tngroupname=organic_news&newV' \
          'ideo=12&rsv_dl=news_b_pn&pn='+str(num)
    res = requests.get(url, headers=headers, timeout=10).text
    #  正则表达式部分主要是筛选数据，清洗数据
    p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)" target.*?<!--s-text-->'
    p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    biaoti = []

    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        biaoti.append(title[i])

    # 数据储存
    file1 = open('E:\\数据挖掘报告.txt', 'a')
    file1.write(company+'数据挖掘completed'+'\n'+'\n')
    for i in range(len(title)):
        file1.write(str(i+1)+'.'+biaoti[i]+'\n')
        file1.write(href[i]+'\n')
    file1.write('------------------'+'\n'+'\n')
    file1.close()


companys = ['阿里巴巴', '百度集团', '茅台']
for company in companys:
    for i in range(2):
        try:
            baidu(company, i+1)
            print(company+'第'+str(i+1)+'页爬取成功')
        except exception:
            print(str(i) + '百度新闻爬取失败')
