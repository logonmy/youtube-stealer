import sys
import os
import os.path
import time

import pickle
import pyautogui
from selenium import webdriver

# add webdriver to environment
webdriver_path=os.getcwd()
if webdriver_path not in sys.path:
    sys.path.append(webdriver_path)

class no_identity_code(Exception):

    def __init__(self):
        self.info='what the fuck you doing? input the identity code!'

# driver=webdriver.Firefox(executable_path=r'chromedriver.exe')
driver=webdriver.Firefox(executable_path=r'geckodriver-selenium.exe')


# driver.set_page_load_timeout(10)
cokies=[{'name': 'BAIDUID', 'value': 'BA9EBE2FD549C3FBD81BE2B99ED18101:FG=1', 'path': '/',
                    'domain': '.baidu.com', 'expiry': 1567433316, 'secure': False, 'httpOnly': False},
                   {'name': 'people', 'value': '0', 'path': '/', 'domain': 'baijiahao.baidu.com',
                    'expiry': 1538489318, 'secure': False, 'httpOnly': False},
                   {'name': 'BDUSS', 'value': 'N5bWhEblV3dXNsV1V5QzZrbWJqY1RGSk1CcVhIc29YY0N0S0tlSXc1SDdlN05iQVFBQUFBJCQAAAAAAAAAAAEAAADFpaZ9tLTWx8TcyrG0-'
                                              'gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPvui1v77otbNn',
                    'path': '/', 'domain': '.baidu.com', 'expiry': 1795097339, 'secure': False, 'httpOnly': True}]

# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
# while (True):
#     print(pyautogui.position())

#百家号的登陆机制：一直加载，卡在driver.get中，因此需要使用多线程，调用pyautogui解决
# driver.get(url='https://baijiahao.baidu.com/builder/app/login')


# [846,590]
# [908,326]
# [926.382]
# [955,464]

# login in manual, then get the cookies
def get_user_id():
    if driver.current_url!='https://baijiahao.baidu.com/builder/app/login':
        driver.get(driver.current_url)
        time.sleep(5)
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        print(driver.get_cookies())

# get_user_id()

def login_with_pyautogui():

    pyautogui.click(477, 546, duration=1)
    pyautogui.typewrite('17806284087')
    time.sleep(1)
    pyautogui.click(477, 546, duration=1)
    pyautogui.typewrite('2468BDwj')
    pyautogui.press('enter')
    time.sleep(2)

# username_login=driver.find_element_by_id(id_='TANGRAM__PSP_4__footerULoginBtn')
# username_login.click()
#
# account=driver.find_element_by_id(id_='TANGRAM__PSP_4__userName')
# account.send_keys('17806284087')
# time.sleep(1)
# passwd=driver.find_element_by_id(id_='TANGRAM__PSP_4__password')
# passwd.send_keys('2468BDwj')
# time.sleep(1)


time.sleep(3)


try:
    driver.find_element_by_id(id_='nc_1_n1z')
    need_to_input_identity_code=True
except:
    need_to_input_identity_code=False

if need_to_input_identity_code:

    pass

else:

    login_submit = driver.find_element_by_id(id_='TANGRAM__PSP_4__submit')
    login_submit.click()


    driver.get(url=driver.current_url)
    test=driver.find_elements_by_class_name(name='aside-action')
    test[2].click()
    # print(test)
    time.sleep(1)

    # driver.get(url=driver.current_url)

    upload_button=driver.find_elements_by_class_name('ant-tabs-tab')
    upload_button[1].click()
    upload_button=driver.find_element_by_class_name(name='webuploader-element-invisible')
    upload_button.click()