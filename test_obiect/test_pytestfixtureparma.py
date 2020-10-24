#作者：daniel
#@Time: 2020/8/13 21:36
#@File: test_pytestfixtureparams.PY

import pytest
# from  testpytest.test_fun import func
user_data=['user1','user2']
# func(10)


@pytest.fixture(scope="function",params=user_data,ids=["test1","test2"])  #ids是给执行的参数命名
def users(request):
    return request.param

def test_register(users):
    print("用户：%s" %users)

if __name__ == '__main__':
    pytest.main(["-s","test_pytestfixtureparma.py"])

