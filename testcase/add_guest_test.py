# -*- coding: utf-8 -*-
'''
@author: liudinglong

@software: pycharm

@file:  add_guest_test.py

@time: 2020/2/23 0023 13:44

'''

import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_init import data_init


class AddGuessTest(unittest.TestCase):
    ''' 添加嘉宾 '''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_guest/"

    def tearDown(self):
        print(self.result)

    def test_add_guest_all_null(self):
        ''' 参数为空 '''
        payload = {'eid':'','realname':'','phone':''}
        r = requests.get(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], '参数错误')

    def test_add_guest_eid_null(self):
        ''' eid=901 查询为空 '''
        payload = {'eid':901,'realname':'tom','phone':13711001100}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], '发布会id不存在')

    def test_add_guest_status_close(self):
        ''' eid=2 状态未开启 '''
        payload = {'eid':3,'realname':'tom','phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], '发布会状态无效')

    def test_add_guest_limit_full(self):
        ''' eid=2 发布会人数已满 '''
        payload = {'eid':2,'realname':'tom','phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], '发布会人数已满')

    def test_add_guest_time_start(self):
        ''' eid=4 发布会已开始 '''
        payload = {'eid':4,'realname':'tom','phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], '发布会已经开始了')

    def test_add_guest_phone_repeat(self):
        ''' phone=13800113001 手机号重复 '''
        payload = {'eid':1,'realname':'tom','phone':13511001100}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], '手机号码重复')

    def test_add_guest_success(self):
        ''' 添加成功 '''
        payload = {'eid':1,'realname':'tom','phone':13511001199}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], '成功添加嘉宾')


if __name__ == '__main__':
    data_init.init_data() # 初始化接口测试数据
    unittest.main()
