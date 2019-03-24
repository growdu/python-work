# -*- coding；UTF-8 -*-

from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.keys import Keys
import time
import urllib

def get_pic():
    # PROXY = '119.28.194.66:8888'
    proxyHost="36.34.15.188"
    proxyPort="6436"
    proxyType='http'
    service_args = [
    "--proxy-type=%s" % proxyType,
    "--proxy=%(host)s:%(port)s" % {
        "host" : proxyHost,
        "port" : proxyPort,
    }
    ]
    chrome_options = webdriver.ChromeOptions()
    #firefox_options=webdriver.FirefoxOptions()
    # chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
    #driver = webdriver.Chrome(chrome_options=chrome_options)  # 启动全局浏览器
    driver = webdriver.Chrome(chrome_options=chrome_options,service_args=service_args) 
    #driver=webdriver.Firefox(firefox_options=firefox_options,service_args=service_args)
    #driver=webdriver.Firefox()
    driver.set_window_size(1024, 768)

    driver.get('http://www.gsxt.gov.cn/index.html')
    time.sleep(3)
    # kw = driver.find_element_by_xpath('//form[@class="search_index_box auto fix mt10"]//input[7]')
    try:
        kw = driver.find_element_by_xpath('//*[@id="keyword"]')
    except:
        driver.quit()
        get_pic()

    kw.clear()
    kw.send_keys('阿里巴巴')

    # driver.find_element_by_xpath('//*[@id="btn_query"]').click()  #这句会影响验证码通过
    time.sleep(5)
    btn = driver.find_element_by_xpath('//*[@id="btn_query"]')

    btn.send_keys(Keys.ENTER)
    #print('+' * 100)
    time.sleep(5)  # 点击搜索后，等待加载

    while True:
        login_text = driver.page_source
        login_html = etree.HTML(login_text)


        img_link = login_html.xpath(
            '//*[@class="geetest_item_img"]/@src')  # 获取验证码链接


        try:
            if img_link[0]:  # 如果弹出验证码
                #print(img_link)
                # driver.get_screenshot_as_file('.//static/1.png')
                #print('*' * 100)
                # logger.info('出现验证码--{}'.format(uuid))
                #img_path = '../jiyan/crawled_img/verifyCode{0}.jpg'.format(int(time.time()))
                img_path = 'C:/Users/along/Desktop/verifyCode{0}.jpg'.format(int(time.time()))

                urllib.request.urlretrieve(img_link[0], img_path)
            else:
                btn_retry = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[4]/div[3]')
                #print(btn_retry)
                btn_retry.click()
                time.sleep(6)
                login_text = driver.page_source
                login_html = etree.HTML(login_text)
                img_link1 = login_html.xpath('//*[@class="geetest_item_img"]/@src')  # 获取验证码链接
                img_path = 'C:/Users/along/Desktop/verifyCode{0}.jpg'.format(int(time.time()))
                urllib.request.urlretrieve(img_link1[0], img_path)
        except:
            driver.quit()
            time.sleep(200)
            get_pic()

            # except:
            #     btn_retry = driver.find_element_by_xpath('//*[@class="geetest_panel_content"]')
            #     print(btn_retry)
            #     btn_retry.click()
            #     # btn_retry.send_keys(Keys.ENTER)
                # time.sleep(2)
            #     img_link = login_html.xpath('//*[@class="geetest_item_img"]/@src')  # 获取验证码链接
            #     urllib.request.urlretrieve(img_link[0], img_path)
            # # except:
            #     driver.quit()
            #     get_pic()

        btn = driver.find_element_by_xpath('//*[@class="geetest_commit"]')
        btn.send_keys(Keys.ENTER)
        time.sleep(5)

if __name__ == '__main__':

    get_pic()