import sys
import os
import os.path
import time

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


driver.get(url='https://account.youku.com/partnerLogin.htm?pid=20170512PLF000867&callback=https%3A%2F%2Fmp.dayu.com'
                '%2Fyt-login-callback%3Fredirect_url%3D%252Fdashboard%252Fvideo%252Fwrite%253Fspm%253Da2s0i.db_index.menu.4.15fb3caa9Skk74')
initial_url=driver.current_url

account=driver.find_element_by_id(id_='YT-ytaccount')
account.send_keys('17806284087')
time.sleep(1)
passwd=driver.find_element_by_id(id_='YT-ytpassword')
passwd.send_keys('2468YKwj2468')
time.sleep(1)
print(driver.current_window_handle)

login_submit = driver.find_element_by_id(id_='YT-nloginSubmit')
login_submit.click()




time.sleep(3)

def wait_until(timeout):
    print('please input the identity code!')
    end_time=time.time()+timeout
    if time.time()>end_time:
        raise no_identity_code
    else:
        time.sleep(1)

if driver.current_url == initial_url:
    try:
        driver.find_element_by_id(id_='nc_1_n1z')
        wait_until(10)
    except:
        raise no_identity_code
        # print('can not find huakuai')



# if driver.find_element_by_class_name(name='nc-lang-cnt'):
#     wait_until(5)
# else:
#     login_submit = driver.find_element_by_id(id_='YT-nloginSubmit')
#     login_submit.click()


current_handle=driver.current_window_handle
print(current_handle,driver.current_url)

time.sleep(5)
# driver.switch_to_window()
# driver.refresh()
# driver.get(url=driver.current_url)

handle=driver.current_window_handle
print(driver.window_handles,handle)
# driver.switch_to.window()

driver.get(url=driver.current_url)
test=driver.find_elements_by_class_name(name='w-menu_title')
test[1].click()
# print(test)
time.sleep(1)

# upload_button=driver.find_element_by_class_name(name='article-write_video-container-upload-from localVideoUpload')
upload_button=driver.find_element_by_class_name(name='article-write_video-container-upload-local')
upload_button.click()