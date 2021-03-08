import re
res = '''文本A
百度新闻文本B'''
p_source = '文本A(.*?)文本B'
source = re.findall(p_source, res, re.S)
a = source[0].strip('\n')
print(a)