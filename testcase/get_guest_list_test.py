# -*- coding: utf-8 -*-
'''
@author: liudinglong

@software: pycharm

@file:  get_guest_list_test.py

@time: 2020/2/23 0023 13:44

'''

import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_init import data_init


class GetGuestListTest(unittest.TestCase):
    ''' 获得嘉宾列表 '''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/get_guest_list/"

    def tearDown(self):
        print(self.result)

    def test_get_guest_list_eid_null(self):
        ''' eid 参数为空 '''
        r = requests.get(self.base_url, params={'eid':''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], '发布会id不能为空')

    def test_get_event_list_eid_error(self):
        ''' 根据 eid 查询结果为空 '''
        r = requests.get(self.base_url, params={'eid':901})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], '查询的数据不存在')

    def test_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        r = requests.get(self.base_url, params={'eid':1})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], '查询成功')
        self.assertEqual(self.result['datas'][0]['realname'],'alen')
        self.assertEqual(self.result['datas'][0]['phone'],'13511001100')

    def test_get_event_list_eid_phone_null(self):
        ''' 根据 eid 和phone 查询结果为空 '''
        r = requests.get(self.base_url, params={'eid':1,'phone':'10000000000'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], '查询的结果为空')

    def test_get_event_list_eid_phone_success(self):
        ''' 根据 eid 和phone 查询结果成功 '''
        r = requests.get(self.base_url, params={'eid':1,'phone':'13511001100'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], '查询成功')
        self.assertEqual(self.result['datas']['realname'],'alen')
        self.assertEqual(self.result['datas']['phone'],'13511001100')


if __name__ == '__main__':
    data_init.init_data() # 初始化接口测试数据
    unittest.main()
