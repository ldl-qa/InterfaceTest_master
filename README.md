### 介绍
本文总结介绍接口测试框架开发，环境使用python3+unittest测试框架及模块驱动，采用db初始化测试数据，以及使用HTMLTestRunner来生成测试报告。

### 流程图
![flow](https://github.com/ldl-qa/InterfaceTest_master/raw/master/common/flow.png)

### 框架处理过程： 
    1.首先编写一份测试数据初始化的脚本，维护一批测试数据到数据库，并且每次初始化前，清空原来的数据，这样保证数据是最新和唯一的(避免重复)。 
    2.调用被测系统的接口，传入参数，这个请求参数是字典，并且数据与数据库数据(数据是初始化时插入)中一致。 
    3.系统接口会根据入参，向测试数据库查询。 
    4.查询结果组装成一定格式(dict、json)的数据，返回给测试框架。 
    5.测试框架断言接口返回的数据，并生成测试结果(测试报告)。

### 项目结构： 
    common/: 报告、日志等公共模块存放文件夹 
    config/: 文件路径、配置信息存放 
    db_init/: 测试数据初始化处理程序 
    logs/: 生成日志文件 
    pies/: 饼图存放 
    report/: 测试报告存放 
    testcase/: 用于编写测试用例 
    run_main.py 执行测试集的主程序


具体文档可以参考我的博客，地址：https://www.cnblogs.com/liudinglong/p/12350109.html