import time
import datetime
from selenium.webdriver import Chrome, ChromeOptions


def getvalue(data):
    # 登录
    print('[2] 打开登录页面...')
    try:
        browser.get("http://manage.xxxxxxx.com")
    except:
        print('[2][ERROR] 打开登录页面失败！')
        return 0
    try:
        browser.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[1]/div[1]/input').send_keys('xxxxx')
        browser.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[1]/div[2]/input').send_keys('xxxxx')
        browser.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[2]/input[1]').click()
        time.sleep(1)
        if browser.title != '桌面 - 中国电能服务网':
            print('[2][ERROR] 登陆失败，请检查用户信息！')
            return 0
    except:
        print('[2][ERROR] 登陆失败，请检查用户信息！')
        return 0
    # 传统页面
    print('[3] 进入传统版界面...')
    try:
        browser.get("http://manage.xxxxxxx.com/classic.html")
    except:
        print('[3][ERROR] 进入传统版界面失败！')
        return 0
    time.sleep(1)
    print('[3] 进入能源分析板块...')
    try:
        browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div[1]').click()
    except:
        print('[3][ERROR] 进入能源分析板块失败！')
        return 0
    time.sleep(1)
    print('[3] 进入电量与电费分析模块...')
    try:
        browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/ul/li[7]/ul/li[1]/div/span[4]').click()
    except:
        print('[3][ERROR] 进入电量与电费分析模块失败！')
        return 0
    time.sleep(1)
    print('[4] 进入iframe子框架...')
    try:
        iframe = browser.find_element_by_xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/iframe')
        browser.switch_to.frame(iframe)
    except:
        return 0
    # 选择日报表
    print('[5] 正在选择报表类型...')
    try:
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/span/input[1]').clear()
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/span/input[1]').send_keys('日报表')
    except:
        print('[5][ERROR] 报表类型检索失败！')
        return 0
    time.sleep(1)
    # 选择日期
    print('[5] 正在选择日期...')
    try:
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[2]/span[1]/span/input[1]').clear()
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[2]/span[1]/span/input[1]').send_keys(data)
    except:
        print('[5][ERROR] 日期选择失败！')
        return 0
    time.sleep(1)
    # 确定
    print('[5] 正在查询...')
    try:
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[3]/a[1]/span').click()
    except:
        print('[5][ERROR] 查询按钮失效！')
        return 0
    time.sleep(1)

    #######################   特化厂区   #########################
    print('[6] 检索到特化厂区电源进线昨日总电量...')
    try:
        tehuachang = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/table/tbody/tr[1]/td[3]/div').text
        print('[6] 特化厂区电源进线昨日总电量为：'+tehuachang)
    except:
        print('[6][ERROR] 查询特化厂区电源进线昨日总电量失败！')
        return 0
    #######################   涤纶厂区   #########################
    time.sleep(1)
    print('[6] 检索到涤纶厂区电源进线昨日总电量...')
    try:
        browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div/ul/li/ul/li[2]/div/span[4]').click()
        time.sleep(1)
        dilunchang = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/table/tbody/tr/td[3]/div').text
        print('[6] 涤纶厂区电源进线昨日总电量为：'+dilunchang)
    except:
        print('[6][ERROR] 查询涤纶厂区电源进线昨日总电量失败！')
        return 0

    return tehuachang, dilunchang

if __name__ == "__main__":
    today = datetime.datetime.now()
    print('[1] 今日日期：' + (today).strftime('%Y-%m-%d'))
    offset = datetime.timedelta(days=-1)
    re_date = (today + offset).strftime('%Y-%m-%d')
    print('[1] 前一天日期：' + re_date)
    print('[2] 设置Chrome无界面浏览器...')
    opt = ChromeOptions()
    opt.headless = True
    browser = Chrome(executable_path='chromedriver', options=opt)
    # browser.maximize_window()
    elec1, elec2 = getvalue(re_date)
    total = float(elec1) + float(elec2)
    print('[6][涤纶有限公司] 昨日总电量为：' + str(total))
    browser.close()
