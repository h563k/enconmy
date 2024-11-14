from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver


def env_init(headless=False):
    options = ChromeOptions()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Remote(
        options=options, command_executor="http://192.168.28.2:4444")
    # 设置浏览器窗口大小
    driver.set_window_size(1920, 1080)
    return driver, options
