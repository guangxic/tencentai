
text = '今天深圳的天气怎么样？明天呢'
utf = text.encode('utf-8')

print(str(utf)[2:-1].replace('\\x', '%').upper())
print(text)

print(__name__)