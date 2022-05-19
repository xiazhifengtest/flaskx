import requests
import config
import os


def base_dir():
    return os.path.join(os.path.dirname(__file__), 'token.md')


def login():
    url = config.address + 'uaa/oauth/token?ts=1'
    data = {'version': 'new',
            'grant_type': 'password',
            'entry_type': 'internal',
            'app': '302',
            'username': 'chenyukun',
            'password': 'A1NTf828+nkM9j2ueoVR8E8aVohfUuDDQVpWAa336mts1ApTpf14F8XrG5GbmAPiggCW7PuGG7pee5vzY+Tz/ynVMFoTWqZeew+8SOUTYygSq3IAyyHJmYfDh5Rex0M3qYPwHaVmXfVtxpdsSFTttLR2PW5/AbJDTr4lP7Nywl4='}
    r = requests.post(url=url, data=data)
    token = r.json()["data"]["access_token"]
    Authorization = 'Bearer ' + token
    # 获取到请求中的access_token加上bearer后写入到文件token.md中
    with open(base_dir(), 'w') as f:
        f.write(Authorization)
    # return Authorization

# token写入到token.md文件中，测试用例可在使用时获取到该文件，则每个case获取一次，不用每个接口调用
# 后续可能会不写入文件放在缓存中来使用

# TODO：配置文件管理修改为使用py文件，旧代码暂时不删
# 写入配置文件的方法---可用
# def Writerconfig():
#     # 需要借助os
#     os.chdir(r'C:\Users\DELL\Desktop\project\flaskx')
#     config = configparser.ConfigParser()
#     # 读取ini配置文件
#     config.read('config.ini')
#     # 将token配置信息呢写入到config文件
#     token = login()
#     config.set('common', 'Authorization', token)
#     # 写入成功后保存文件
#     with open('config.ini', 'w+') as  f:
#         config.write(f)

# if __name__ == '__main__':
#     login()
