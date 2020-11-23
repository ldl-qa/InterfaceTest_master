# -*- coding: utf-8 -*-
'''
@author: liudinglong

@software: pycharm

@file:  get_event_list_test.py

@time: 2020/2/23 0023 13:44

'''


import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_init import data_init


class GetEventListTest(unittest.TestCase):
    ''' 获得发布会列表 '''


    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/get_event_list/"

    def tearDown(self):
        print(self.result)

    def test_get_event_list_eid_error(self):
        ''' eid=901 查询结果为空 '''
        r = requests.get(self.base_url, params={'eid':901})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], '查询对象结果为空')

    def test_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        r = requests.get(self.base_url, params={'eid':1})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], '查询成功')
        self.assertEqual(self.result['datas']['name'],u'红米Pro发布会')
        self.assertEqual(self.result['datas']['address'],u'北京会展中心')

    def test_get_event_list_nam_result_null(self):
        ''' 关键字‘abc’查询 '''
        r = requests.get(self.base_url, params={'name':'abc'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], '查询的数据不存在')

    def test_get_event_list_name_find(self):
        ''' 关键字‘发布会’模糊查询 '''
        r = requests.get(self.base_url, params={'name':'发布会'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], '查询成功')
        self.assertEqual(self.result['datas'][0]['name'],u'红米Pro发布会')
        self.assertEqual(self.result['datas'][0]['address'],u'北京会展中心')


if __name__ == '__main__':
    data_init.init_data() # 初始化接口测试数据
    unittest.main()
