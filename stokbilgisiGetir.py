from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.set_window_position(0,0)
driver.set_window_size(800,800)
driver.get('https://www.robotistan.com/makeblock-mbot-bluetooth-kiti-v11-mavi')
time.sleep(5)
driver.find_element_by_name('Adet2754').send_keys('100000')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="addCartBtn"]/span').click()

time.sleep(5)
mevcutStok = driver.find_element_by_id('myPopup3').text

print(mevcutStok.split(': ')[1])

driver.get('https://www.robotistan.com/makeblock-mbot-ranger-bluetooth')
time.sleep(5)
driver.find_element_by_name('Adet5798').send_keys('100000')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="addCartBtn"]/span').click()

time.sleep(5)
mevcutStok = driver.find_element_by_id('myPopup3').text

print(mevcutStok.split(': ')[1])

driver.close()
