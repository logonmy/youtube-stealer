import sys
import os
import os.path
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class no_identity_code(Exception):
    def __init__(self):
        self.info = 'what the fuck you doing? input the identity code!'


class main_upload(object):

    def __init__(self):

        webdriver_path=os.getcwd()
        if webdriver_path not in sys.path:
            sys.path.append(webdriver_path)



    def cache_html(url):

        html=requests.get(url).content
        f=open('html.html',mode='wb')
        f.write(html)

    def bilibili(self,username,password,filepath):
        # driver=webdriver.Firefox(executable_path=r'chromedriver.exe')
        driver=webdriver.Firefox(executable_path=r'geckodriver-selenium.exe')

        driver.get(url='https://passport.bilibili.com/login')
        initial_url=driver.current_url

        account=driver.find_element_by_id(id_='login-username')
        account.send_keys(username)
        time.sleep(1)
        passwd=driver.find_element_by_id(id_='login-passwd')
        passwd.send_keys(password)
        time.sleep(1)
        print(driver.current_window_handle)

        print('you have to identity manual')

        timeout=60
        end_time = time.time() + timeout

        while(True):
            if time.time() > end_time:
                raise no_identity_code
            else:
                if driver.current_url == 'https://www.bilibili.com/':

                    driver.get(url=driver.current_url)
                    test=driver.find_element_by_class_name(name='u-link')
                    test.click()
                    time.sleep(1)

                    handles=driver.window_handles
                    print(handles)
                    # ['4294967297', '4294967303']

                    time.sleep(1)
                    # the new tab need some time to import,or the 'about:blank' will be returned
                    # driver.switch_to_window(handles[-1])
                    driver.switch_to.window(handles[-1])
                    # driver.get(url=driver.current_url)
                    print(driver.current_url)

                    f = open('html_source_tips.html', mode='w', encoding='utf-8')
                    f.write(driver.page_source)

                    time.sleep(10)

                    tips=driver.find_elements_by_class_name(name='guide-tip-btn-right')
                    print(tips)
                    if tips:
                        tips[0].click()
                    else:
                        # driver.refresh()
                        raise no_identity_code

                    time.sleep(5)
                    # driver.refresh()
                    self.cache_html(driver.current_url)

                    f = open('html_source.html', mode='w',encoding='utf-8')
                    f.write(driver.page_source)

                    time.sleep(5)
                    # driver.get(url=driver.current_url)

                    if driver.current_url == 'https://member.bilibili.com/v2#/home':
                        driver.find_element_by_id(id_='nav_upload_btn').click()
                    time.sleep(5)

                    #!!!!!!!!!!!!!!哔哩哔哩使用网页子页面(iframe)保存的上传按钮等内容导致，查询失败!!!!!!!!!!!!!!
                    # get into iframe to find elements
                    driver.switch_to.frame('videoUpload')
                    # upload_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                    #                                                 ((By.ID, 'bili-upload-btn')))

                    upload_button=driver.find_element_by_id(id_='bili-upload-btn')
                    # upload_button=driver.find_elements_by_class_name(name='webuploader-container')
                    # upload_button=driver.find_element_by_class_name(name='upload-btn-icon')

                    print(upload_button.is_enabled())
                    upload_button.click()
                    time.sleep(15)
                    break


        # if time.time() > end_time:
        #     raise no_identity_code
        # else:
        #     if driver.current_url != initial_url:
        #
        #         # user need to click login_button by themself
        #         # login_submit = driver.find_element_by_class_name(name='btn btn-reg')
        #         # login_submit.click()
        #
        #
        #         driver.get(url=driver.current_url)
        #         test=driver.find_element_by_class_name(name='u-link')
        #         test.click()
        #         # print(test)
        #         time.sleep(1)
        #
        #         driver.get(url=driver.current_url)
        #         # upload_button=driver.find_element_by_class_name(name='article-write_video-container-upload-from localVideoUpload')
        #         upload_button=driver.find_element_by_id(id_='bili-upload-btn')
        #         upload_button.click()


        import pyautogui


        filename_typein_location=[477,496]
        open_button_location=[632,525]
        pyautogui.click(477,496,duration=1)
        pyautogui.typewrite(filepath)
        pyautogui.press('enter',presses=1)
        pyautogui.click(632,525,duration=1)


        # title=driver.find()
        # title.send_keys('')
        #
        # lable1=driver.find_element_by_id()
        # lable1.send_keys('')
        # lable2=driver.find()
        # lable1.send_keys('')
        # lable3=driver.find()
        # lable1.send_keys('')
        # lable4=driver.find()
        # lable1.send_keys('')
        # lable5=driver.find()
        # lable1.send_keys('')
        #
        # submit=driver.find_element_by_id()
        # submit.click()
