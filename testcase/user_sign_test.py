# -*- coding: utf-8 -*-
'''
@author: liudinglong

@software: pycharm

@file:  user_sign_test.py

@time: 2020/2/23 0023 13:44

'''

import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_init import data_init
from common.logger import Log
logger = Log()

class UserSignTest(unittest.TestCase):
    ''' 用户签到 '''

    def setUp(self):
        logger.info("开始执行测试".center(60, '#'))
        self.base_url = "http://127.0.0.1:8000/api/user_sign/"

    def tearDown(self):
        logger.info(("接口返回数据:%s" % self.result).center(60, '#'))
        print(self.result)
        logger.info("测试执行结束".center(60, '#'))

    def test_user_sign_all_null(self):
        ''' 参数为空 '''
        payload = {'eid':'','phone':''}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], '参数错误')

    def test_user_sign_eid_error(self):
        ''' eid=901 查询结果不存在 '''
        payload = {'eid':901,'phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], '发布会id不存在')

    def test_user_sign_status_close(self):
        ''' eid=3 发布会状态关闭 '''
        payload = {'eid':3,'phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], '发布会未开启')

    def test_user_sign_time_start(self):
        ''' eid=4 发布会已开始 '''
        payload = {'eid':4,'phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], '发布会时间已过')

    def test_user_sign_phone_error(self):
        ''' phone=10100001111 手机号不存在 '''
        payload = {'eid':1,'phone':10100001111}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], '手机号码不存在')

    def test_user_sign_eid_phone_error(self):
        '''eid=1, phone=13511001102 手机号与发布会不匹配 '''
        payload = {'eid':1,'phone':13511001102}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], '嘉宾不属于该发布会')

    def test_user_sign_has_sign_in(self):
        ''' 已签到 '''
        payload = {'eid':1,'phone':13511001101}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10027)
        self.assertEqual(self.result['message'], '嘉宾已签到')

    def test_user_sign_success(self):
        ''' 签到成功 '''
        payload = {'eid':1,'phone':13511001100}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], '签到成功')


if __name__ == '__main__':
    data_init.init_data() # 初始化接口测试数据
    unittest.main()
