=============================================================================
单个case工作流程：

1：编写输入数据文本 在auto_test/in_data 目录下，最好跟接口同名，方便

2：转到auto_test/test_tool 目录下，执行命令
    php .\AesEnTest.php  
   或者  
    python  AesEn_call_php.py
    将加密输入数据，生成加密文件，在原文件的基础上加前缀 “en_”

3：在case目录下，运行程序
        python case文件，将发起向服务器的request请求，并获取服务器返回结果，保存到out_data目录下，
        判断用例请求是否成功，断言。
4：转到auto_test/test_tool 目录下，执行命令
    php .\AesDeTest.php 
   或者
    python AesDe_call_php.py

    将out_data目录的加密数据文件，生成解密文件，在原文件的基础上加前缀 “de_”

===============================================================================
case编写及测试过程

1. 在case目录下新建py 文件，模板在templete下
2. 编写完成后，可自己做单元测试，看程序运行有无错误，通过后
3. 将case增加到 s_visit.py 中，填写两个地方即可，一处是 import 导入case文件
   另一处是suite 方法里，增加suite.addTest，把导入的包名.模块名 跟‘ApiTestCase("test_1")’拼接即可
   如导入包
      import case.api_login
   增加测试case
      	suite.addTest(case.api_login.ApiTestCase("test_1"))
4. 最后运行t_run.py,
5. 到out_report目录下查看测试报告。

===============================================================================

author: xuejf
mail: 171521952@qq.com
version：1.2
build on April 3,2018