import sys
import os
import os.path
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


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
time.sleep(2)
passwd=driver.find_element_by_id(id_='YT-ytpassword')
passwd.send_keys('2468YKwj2468')
time.sleep(2)

try:
    driver.find_element_by_id(id_='nc_1_n1z')
    need_to_input_identity_code=True
except:
    need_to_input_identity_code=False

if need_to_input_identity_code:

    # time.sleep(3)
    #
    # def wait_until(timeout):
    #     print('please input the identity code!')
    #     end_time=time.time()+timeout
    #     if time.time()>end_time:
    #         raise no_identity_code
    #     else:
    #         time.sleep(1)
    #
    # if driver.current_url == initial_url:
    #     try:
    #         driver.find_element_by_id(id_='nc_1_n1z')
    #         wait_until(10)
    #     except:
    #         raise no_identity_code
    #         # print('can not find huakuai')

    timeout=60
    end_time = time.time() + timeout

    while(True):
        if time.time() > end_time:
            raise no_identity_code
        else:
            print(time.time())

            if driver.current_url == '':

                # if driver.find_element_by_class_name(name='nc-lang-cnt'):
                #     wait_until(5)
                # else:
                #     login_submit = driver.find_element_by_id(id_='YT-nloginSubmit')
                #     login_submit.click()

                driver.get(driver.current_url)
                try:
                    time.sleep(2)
                    quick_login = driver.find_element_by_class_name(name='YT-form-btn')
                    quick_login.click()
                except:
                    pass

                time.sleep(5)

                handle=driver.current_window_handle
                print(driver.window_handles,handle)
                # driver.switch_to.window()

                driver.get(url=driver.current_url)
                test=driver.find_elements_by_class_name(name='w-menu_title')
                test[1].click()
                # print(test)
                time.sleep(5)

                # upload_button=driver.find_element_by_class_name(name='article-write_video-container-upload-from localVideoUpload')
                upload_button=driver.find_element_by_class_name(name='article-write_video-container-upload-local')
                upload_button.click()
else:
    login_submit = driver.find_element_by_id(id_='YT-nloginSubmit')
    login_submit.click()
    time.sleep(5)

    if driver.current_url==initial_url:
        print('login failed, you need to login again.')

    driver.get(driver.current_url)
    try:
        time.sleep(2)
        quick_login=driver.find_element_by_class_name(name='YT-form-btn')
        quick_login.click()
    except:
        pass

    time.sleep(5)

    driver.get(url=driver.current_url)
    time.sleep(5)
    test = driver.find_elements_by_class_name(name='w-menu_title')
    test[1].click()
    time.sleep(5)

    upload_button = driver.find_element_by_class_name(name='article-write_video-container-upload-local')
    upload_button.click()


    import pyautogui


    filename_typein_location=[477,546]
    open_button_location=[632,585]
    pyautogui.click(477,546,duration=1)
    pyautogui.typewrite(r'C:\Users\lenovo\Desktop\project1\server-version\local\HUAWEI MateBook X Pro.mp4')
    time.sleep(1)
    pyautogui.press('enter')
    # pyautogui.click(632,585,duration=1)
    time.sleep(2)


    title='title'
    info='info'
    label1='1'
    label2 = '2'
    label3 = '3'
    label4 = '4'

    f = open('dayuhao_submit_source.html', mode='w', encoding='utf-8')
    f.write(driver.page_source)

    print(driver.current_url)
    # driver.get(driver.current_url)
    print(driver.window_handles)

    time.sleep(2)

    #标题无法清空，无法send_keys
    title_input=driver.find_elements_by_class_name(name='w-form-field-content')
    # #w-form-field-content;title\info\labels\classes
    print(title_input[0])
    # title_input[0].clear()
    # title_input[0].send_keys(title)

    # ActionChains(driver).click(title_input[0]).perform()
    # ActionChains(driver).send_keys_to_element(element=title_input[0],).perform()

    info_input=driver.find_element_by_tag_name(name='textarea')
    info_input.clear()
    info_input.send_keys(info)

    # !!!!!!!!!scroll to the bottom!!!!!!!!!!
    driver.execute_script("window.scrollTo(0, 650)")

    #not reachable by keyboard
    # labels=driver.find_element_by_class_name(name="article-write_video-tags form-control")
    labels=driver.find_element_by_css_selector("div[class='article-write_video-tags form-control']")
    # WebDriverWait(driver, 20).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "w-btn-toolbar")))
    # labels=driver.find_element_by_css_selector(css_selector='div.article-write_video-tags.form-control')

    time.sleep(5)
    labels.click()

    f = open('dayuhao_submit_source_labels.html', mode='w', encoding='utf-8')
    f.write(driver.page_source)

    labels.find_elements_by_tag_name('input')[0].send_keys(label1)
    labels.find_elements_by_tag_name('input')[0].send_keys(Keys.ENTER)
    time.sleep(1)
    # labels.click()
    labels.find_elements_by_tag_name('input')[1].send_keys(label2)
    labels.find_elements_by_tag_name('input')[1].send_keys(Keys.ENTER)
    time.sleep(1)
    # labels.click()
    labels.find_elements_by_tag_name('input')[2].send_keys(label3)
    labels.find_elements_by_tag_name('input')[2].send_keys(Keys.ENTER)
    time.sleep(1)
    # labels.click()
    labels.find_elements_by_tag_name('input')[3].send_keys(label4)
    labels.find_elements_by_tag_name('input')[3].send_keys(Keys.ENTER)
    time.sleep(1)

    #视频分类
    classes=driver.find_element_by_class_name(name='widgets-selects_container')
    # WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CLASS_NAME,'widgets-selects_container'))

    # WebDriverWait(driver,10).until(EC.visibility_of(classes))
    # WebDriverWait(driver,20).until(EC.invisibility_of_element_located((By.CLASS_NAME,"w-btn-toolbar")))

    ActionChains(driver).move_to_element(classes).click().perform()
    # classes.click()
    time.sleep(1)
    classes = driver.find_element_by_class_name(name='widgets-selects_select_container')
    time.sleep(1)
    real_classes=classes.find_elements_by_tag_name(name='a')
    real_classes[4].click()

    #封面的选取1，！！！
    upload_state = True
    while(upload_state):

        try:
            print('???')
            # driver.find_elements_by_css_selector("div[class='article-write_video-container-result-opt']")
            driver.find_element_by_class_name(name='article-write_video-container-result-opt')
            break
        except:
            upload_state=True
            time.sleep(1)
            print('video uploading.')

    time.sleep(5)
    cover=driver.find_element_by_class_name(name='article-write_box-form-coverImg')
    ActionChains(driver).move_to_element(cover).perform()
    time.sleep(2)

    # cover3=cover.find_elements_by_css_selector("div[class='w-btn w-btn_primary']")
    cover3=cover.find_elements_by_tag_name('button')
    cover3[2].click()

    #封面的选取2
    # WebDriverWait(driver,100).until(EC.presence_of_element_located(By.CLASS_NAME,"article-write_video-container-result-opt"))
    time.sleep(5)
    cover_choose=driver.find_element_by_class_name(name='article-material-image_image-choose')
    cover_choose.find_elements_by_tag_name(name='img')[0].click()

    cover_button=driver.find_elements_by_class_name(name='article-material-image-dialog_btn')
    print(cover_button)
    next_button=cover_button[0].find_elements_by_tag_name(name='button')
    # next_button=cover_button[1].find_element_by_css_selector("div[class='w-btn w-btn_primary']")
    next_button[1].click()

    time.sleep(5)
    save_button=cover_button[1].find_elements_by_tag_name(name='button')
    save_button[1].click()


    #提交
    time.sleep(1)
    bottom_buttons = driver.find_element_by_class_name(name='w-btn-toolbar')
    submit_button = bottom_buttons.find_elements_by_tag_name(name='button')
    # submit_button=bottom_buttons.find_element_by_css_selector("button[class='w-btn w-btn_primary']")
    print(submit_button)
    submit_button[1].click()

    time.sleep(10)
    preview=driver.find_element_by_class_name(name='article-write-preview_btn')
    make_sure_upload=preview.find_element_by_tag_name("button")
    make_sure_upload.click()

