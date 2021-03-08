import re
res = '文本A百度新闻文本B,文本A新浪新闻文本B,文本A守护新闻文本B'
p_source = '文本A(.*?)文本B'
source = re.findall(p_source, res)
print(source)