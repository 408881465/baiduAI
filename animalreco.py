import urllib.request
from urllib import parse
import base64,urllib,json
# host = 'https://aip.baidubce.com/oauth/2.0/token'
# grant_type='client_credentials'
# client_id='AHf8MrfNLGhV01tysE9hjFVO'
# client_secret='2O1P9F9Eoq2MrwY4hSFAcCAGlLblFeDn'
# url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=AHf8MrfNLGhV01tysE9hjFVO&client_secret=2O1P9F9Eoq2MrwY4hSFAcCAGlLblFeDn'
# request = urllib.request.Request(url)
# request.add_header('Content-Type', 'application/json; charset=UTF-8')
# response = urllib.request.urlopen(request)
# content=response.read()
# if content:
#     print(content)
# picUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=24.391bf9494dbf123a2e7158fae8708e33.2592000.1532330886.282335-11433952'
animal ='https://aip.baidubce.com/rest/2.0/image-classify/v1/animal?access_token=24.243bdf0612f3024af9cd254aba3ea0ec.2592000.1532331073.282335-11435025'
f = open(r'D:\爬虫\me.jpg','rb')
img= base64.b64encode(f.read())
data = {
    'image':img
}
data = parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(animal,data)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
content2 = response.read()
if content2:
    print(content2.decode('utf-8'))
# content2= content2.decode('utf-8')
# obj = json.loads(content2)
# print(type(obj))
# words_result = obj['words_result']
# for i in words_result:
#     print(i['words'])
