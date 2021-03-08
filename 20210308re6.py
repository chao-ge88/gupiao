import re
title = ['<em>阿里巴巴</em>代码竞赛现全球首位AI评委 能为代码质量打分']
title[0] = re.sub('<em>', '', title[0])
title[0] = re.sub('</em>', '', title[0])
# 下面这一行代码等同于上面两行代码，也就是大概相同的两句话可以用一个正则表达式表示出来 这样更简洁
title[0] = re.sub('<.*?>', '', title[0])
print(title[0])

company = '*华能信托'
company1 = re.sub('[*]', '', company)
print(company1)