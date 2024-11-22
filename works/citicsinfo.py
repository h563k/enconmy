import time
from tools.spider_net import env_init





def citicsinfo_main():
    driver, options = env_init(command_executor="http://192.168.28.5:4444")
    url = "https://weixin.citicsinfo.com/tztweb/deal/index.html#!/account/index.html"
    driver.get(url)
    time.sleep(6)
    # driver.quit()
    return driver, options