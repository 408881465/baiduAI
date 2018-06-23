import urllib.request
from urllib import parse
import base64,urllib,json
class AnimalRecognizer():
    def __init__(self,API_Key,Secret_Key):
        self.API_Key = API_Key
        self.Secret_Key = Secret_Key
    def get_access_token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token'
        grant_type='client_credentials'
        client_id=self.API_Key
        client_secret=self.Secret_Key
        url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(self.API_Key,self.Secret_Key)
        request = urllib.request.Request(url)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        obj = json.loads(content.decode('utf-8'))
        access_token = obj["access_token"]
        return access_token
    def get_check_url(self):
        access_token = self.get_access_token()
        check_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/animal?access_token={}'.format(access_token)
        return check_url

    def get_result(self,data):
        check_url = self.get_check_url()
        data = parse.urlencode(data).encode('utf-8')
        request = urllib.request.Request(check_url,data)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content2 = response.read()
        if content2:
            print(content2.decode('utf-8'))
        content2= content2.decode('utf-8')

        obj = json.loads(content2)
        print(type(obj['result']))
        for i in obj['result']:
            print(i['name'],":",i['score'])

    def check(self,img_path):
        f = open(img_path, 'rb')
        img_str = base64.b64encode(f.read())
        data = {
            'image': img_str
        }
        self.get_result(data)


if __name__ == '__main__':
    recognizer = AnimalRecognizer(API_Key='AHf8MrfNLGhV01tysE9hjFVO',Secret_Key='2O1P9F9Eoq2MrwY4hSFAcCAGlLblFeDn')
    img_path = r'D:\爬虫\denkey.jpg'
    recognizer.check(img_path)


