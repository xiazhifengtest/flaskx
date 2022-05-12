import textwrap

import requests
import configparser
import os
import json
import jsonpath


# 获取token1的方法
def login():
    url = 'http://yunnan.skyimin-pre.com/uaa/oauth/token?ts=1'

    # hearers = {'Content-Type': 'application/json;charset=UTF-8'}
    data = {'version': 'new',
            'grant_type': 'password',
            'entry_type': 'internal',
            'app': '302',
            'username': 'chenyukun',
            'password': 'A1NTf828+nkM9j2ueoVR8E8aVohfUuDDQVpWAa336mts1ApTpf14F8XrG5GbmAPiggCW7PuGG7pee5vzY+Tz/ynVMFoTWqZeew+8SOUTYygSq3IAyyHJmYfDh5Rex0M3qYPwHaVmXfVtxpdsSFTttLR2PW5/AbJDTr4lP7Nywl4='}
    r = requests.post(url=url, data=data)
    token = r.json()["data"]["access_token"]
    Authorization = 'Bearer ' + token
    return Authorization



'''旧方法暂时不用因为是写入ini文件所以比较麻烦'''

# 写入配置文件的方法---可用

def Writerconfig():
    #需要借助os
    os.chdir(r'C:\Users\DELL\Desktop\project\flaskx')
    config = configparser.ConfigParser()
    #读取ini配置文件
    config.read('config.ini')
    # 将token配置信息呢写入到config文件
    token = login()
    config.set('common', 'Authorization', token)
    #写入成功后保存文件
    with open('config.ini', 'w+') as  f:
        config.write(f)


Writerconfig()
# TODO：配置文件管理修改为使用py文件，旧代码暂时不删待,使用旧代码

# TODO:待写入一个定时器，间隔一段时间获取一次token

# if __name__ == '__main__':
#     Writerconfig()
