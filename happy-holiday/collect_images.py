from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

def collect_images(text = 'ברכת שנה טובה'):
#Opens up web driver and goes to Google Images
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

    search_box = driver.find_element(By.CSS_SELECTOR, 'input.gLFyf')
    search_box.send_keys(text)
    search_box.send_keys(Keys.ENTER);

    #Will keep scrolling down the webpage until it cannot scroll no more
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height

    for i in range(1, 10):
        try:
            driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('photos/img ('+str(i)+').png')
            time.sleep(2)
        except:
            pass

collect_images()