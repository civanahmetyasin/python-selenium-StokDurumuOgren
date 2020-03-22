from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
while True:
    driver.set_window_position(0,0)
    driver.set_window_size(800,800)
    driver.get('https://www.robotistan.com/makeblock-mbot-bluetooth-kiti-v11-mavi')
    urunAdi = driver.find_element_by_id('productName').text
    time.sleep(2)
    driver.find_element_by_name('Adet2754').send_keys('100000')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="addCartBtn"]/span').click()
    
    time.sleep(2)
    mevcutStok = driver.find_element_by_id('myPopup3').text
    
    print( urunAdi + " : " + mevcutStok.split(': ')[1])
    time.sleep(10)

driver.close()

#driver.get('https://www.robotistan.com/makeblock-mbot-ranger-bluetooth')
#urunAdi = driver.find_element_by_id('productName').text
#time.sleep(2)
#driver.find_element_by_name('Adet5798').send_keys('100000')
#time.sleep(2)
#driver.find_element_by_xpath('//*[@id="addCartBtn"]/span').click()
#
#time.sleep(2)
#mevcutStok = driver.find_element_by_id('myPopup3').text
#
#print( urunAdi + " : " + mevcutStok.split(': ')[1])
#

