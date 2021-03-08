import re
content = 'Hello 123 World 456 jintian  789  jichu   852  jint '
result = re.findall('\d\d\d', content)
print(result)
a = result[0]
print(a)