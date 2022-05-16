import os
import requests
import config
import unittest
import login


def getoken():
    with open(login.base_dir(), 'r') as f:
        return f.read()


class hfTest(unittest.TestCase):
    def setup(self):
        print('获取后扶项目列表')

    def teardown(self):
        print('用例执行成功')

    def testgethflist(self):
        url = config.address + 'wb/hf/project/page'
        params = {'status': 'p1000', 'pageNum': '1', 'pageSize': '20'}
        Authorization = getoken()
        headers = {'Authorization': Authorization}
        r = requests.get(url=url, params=params, headers=headers)
        # 断言方法1验证回参是否为空
        self.assertIsNotNone(r.text, msg='json回传不为空')
        # 断言2验证回参是否带字符串十三五
        self.assertIn('十三五', r.text, msg='%s没有包含%s' % ('r', '十三五'))

        # print(r.json())


if __name__ == "__main__":
    # gettest=hfTest()
    # gettest.gethflist()
    unittest.main()
