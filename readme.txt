=============================================================================
����case�������̣�

1����д���������ı� ��auto_test/in_data Ŀ¼�£���ø��ӿ�ͬ��������

2��ת��auto_test/test_tool Ŀ¼�£�ִ������
    php .\AesEnTest.php  
   ����  
    python  AesEn_call_php.py
    �������������ݣ����ɼ����ļ�����ԭ�ļ��Ļ����ϼ�ǰ׺ ��en_��

3����caseĿ¼�£����г���
        python case�ļ������������������request���󣬲���ȡ���������ؽ�������浽out_dataĿ¼�£�
        �ж����������Ƿ�ɹ������ԡ�
4��ת��auto_test/test_tool Ŀ¼�£�ִ������
    php .\AesDeTest.php 
   ����
    python AesDe_call_php.py

    ��out_dataĿ¼�ļ��������ļ������ɽ����ļ�����ԭ�ļ��Ļ����ϼ�ǰ׺ ��de_��

===============================================================================
case��д�����Թ���

1. ��caseĿ¼���½�py �ļ���ģ����templete��
2. ��д��ɺ󣬿��Լ�����Ԫ���ԣ��������������޴���ͨ����
3. ��case���ӵ� s_visit.py �У���д�����ط����ɣ�һ���� import ����case�ļ�
   ��һ����suite ���������suite.addTest���ѵ���İ���.ģ���� ����ApiTestCase("test_1")��ƴ�Ӽ���
   �絼���
      import case.api_login
   ���Ӳ���case
      	suite.addTest(case.api_login.ApiTestCase("test_1"))
4. �������t_run.py,
5. ��out_reportĿ¼�²鿴���Ա��档

===============================================================================

author: xuejf
mail: 171521952@qq.com
version��1.2
build on April 3,2018