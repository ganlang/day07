import unittest
from case.TestIHRMEmplopy import TestEmployee
from case.TestIHRMUser import TestUser

# 组织测试套件对象
suite = unittest.TestSuite()
suite.addTest(TestUser("test_login_success"))
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_get"))
suite.addTest(TestEmployee("test_emp_delete"))

# 执行套件对象
runner = unittest.TextTestRunner()
runner.run(suite)
