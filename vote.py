import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType

import random

def vote():
    driver = webdriver.Chrome('chromedriver')
    driver.get('https://www.10best.com/awards/travel/best-wellness-retreat/eupepsia-bland-va/');
    time.sleep(5)
    driver.find_element_by_id("awardVoteButton").click()
    time.sleep(5)
    driver.quit()

def random_wait_time():
    rand_num = random.randint(0,10)
    time.sleep(rand_num)

def vote_script():
    count=0
    while count < 300:
        vote()
        random_wait_time()
        count = count+1
        print(count)

vote_script()
