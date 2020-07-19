import json
import requests

def login(s, user="test1",psw="123456"):
    '''实现登录'''
    url = "http://49.235.92.12:6009/api/v1/login"

    body = {
        "username":user,
        "password":"123456"
    }


    r = s.post(url,json=body)
  #  print(r.text)

    #提取token
    token = r.json()["token"]
   # print(token)
    return token

def get_info(s, token):
    url2 = "http://49.235.92.12:6009/api/v1/userinfo"
    h = {
        "Authorization": "Token "+token
    }

    r2 = requests.get(url2,headers=h)
    #print(r2.text)
    return r2


if __name__ == '__main__':
    s = requests.session()
    token = login(s, user="test2") # 可以换个账号
    r2 = get_info(s,token)
    print(r2.json()) # <Response [200]>





