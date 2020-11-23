# -*- coding: utf-8 -*-
'''
@author: liudinglong

@software: pycharm

@file:  add_event_test.py

@time: 2020/2/23 0023 13:43

'''

import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_init import data_init
from common.logger import Log

logger = Log()

class AddEventTest(unittest.TestCase):
    ''' 添加发布会 '''

    def setUp(self):
        logger.info("开始执行测试".center(60,'#'))
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def tearDown(self):
        logger.info(("接口返回数据:%s"%self.result).center(60, '#'))
        print(self.result)
        logger.info("测试执行结束".center(60,'#'))


    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        payload = {'eid':'','':'','limit':'','address':"",'start_time':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], '参数错误')

    def test_add_event_eid_exist(self):
        ''' id已经存在 '''
        payload = {'eid':1,'name':'一加4发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], '发布会id已存在')

    def test_add_event_name_exist(self):
        ''' 名称已经存在 '''
        payload = {'eid':11,'name':'红米Pro发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], '发布会名称已存在')

    def test_add_event_data_type_error(self):
        ''' 日期格式错误 '''
        payload = {'eid':11,'name':'一加4手机发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('开始日期格式错误，必须是:YYYY-MM-DD HH:MM:SS', self.result['message'])

    def test_add_event_success(self):
        ''' 添加成功 '''
        payload = {'eid':11,'name':'一加4手机发布会','limit':2000,'address':"深圳宝体",'start_time':'2017-05-10 12:00:00'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], '添加成功')


if __name__ == '__main__':
    data_init.init_data() # 初始化接口测试数据
    unittest.main()
