import urllib.request
from urllib import parse
import base64,urllib,json
host = 'https://aip.baidubce.com/oauth/2.0/token'
grant_type='client_credentials'
client_id='wSPRWVUN3882GvfNXlV6lzOO'
client_secret='1hzy8Z8fF3l9pCQ0G0i18nW0QGMjzeIq'
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=wSPRWVUN3882GvfNXlV6lzOO&client_secret=1hzy8Z8fF3l9pCQ0G0i18nW0QGMjzeIq'
request = urllib.request.Request(url)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content=response.read()
# if content:
#     print(content)
picUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=24.35d71d840bc6893ce4e072b7ab823c58.2592000.1532312050.282335-11433952'
f = open(r'D:\爬虫\baidutest2.bmp','rb')
img= base64.b64encode(f.read())
data = {
    'image':img
}

data = parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(picUrl,data)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
content2 = response.read()
if content2:
    print(content2.decode('utf-8'))
content2= content2.decode('utf-8')
obj = json.loads(content2)
print(type(obj))
words_result = obj['words_result']
for i in words_result:
    print(i['words'])
