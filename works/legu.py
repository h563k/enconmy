import re
import time
import json
import requests
import datetime
import hashlib
import pandas as pd
from selenium.webdriver.common.by import By
from tools.spider_net import env_init
from tools.echobot import robot_send_message
from tools.standard_log import log_to_file
import akshare as ak


def get_token():
    # 获取今天的日期
    today = datetime.date.today()
    # 将日期转换为字符串
    today_str = str(today)
    # 将字符串编码为字节串
    today_bytes = today_str.encode('utf-8')
    # 创建MD5哈希对象
    m = hashlib.md5()
    # 更新哈希对象
    m.update(today_bytes)
    # 获取十六进制表示的哈希值
    return m.hexdigest()


def get_today_baffe_index(driver):
    xpath = "/html/body/div[1]/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[2]/span"
    element = driver.find_element(by=By.XPATH, value=xpath)
    return element.text


def baffe_index_process(years, data):
    # data = pd.DataFrame(all_baffe_index['data'])
    data['baffe_index'] = data['总市值']/data['GDP']
    baffe_index_25 = data['baffe_index'][-365*years:].quantile(0.25)
    baffe_index_50 = data['baffe_index'][-365*years:].quantile(0.5)
    baffe_index_75 = data['baffe_index'][-365*years:].quantile(0.75)
    return baffe_index_25, baffe_index_50, baffe_index_75


@log_to_file
def legu_main():
    # 获取巴菲特指数, 并判断目前高估还是低估
    driver, _ = env_init()
    url = "https://legulegu.com/stockdata/marketcap-gdp?utm_source=wechat_session&utm_medium=social&utm_oi=676400100432154624"
    driver.get(url)
    time.sleep(5)
    cookies = driver.get_cookies()
    today_buffet_index = ak.stock_buffett_index_lg()
    buffet_index = float(re.findall('\d+.\d+', today_buffet_index)[0])/100
    all_baffe_index = get_all_baffe_index(cookies)
    baffe_index_525, baffe_index_550, baffe_index_575 = baffe_index_process(
        5, all_baffe_index)
    baffe_index_125, baffe_index_150, baffe_index_175 = baffe_index_process(
        1, all_baffe_index)
    driver.quit()
    message = f"""
今日巴菲特指数:                            {buffet_index:.2%}
最近1年巴菲特指数上四分位:      {baffe_index_175:.2%}
最近1年巴菲特指数均值:              {baffe_index_150:.2%}
最近1年巴菲特指数下四分位:      {baffe_index_125:.2%}
最近5年巴菲特指数上四分位:      {baffe_index_575:.2%}
最近5年巴菲特指数均值:              {baffe_index_550:.2%}
最近5年巴菲特指数下四分位:      {baffe_index_525:.2%}"""
    robot_send_message(message)
    return message
