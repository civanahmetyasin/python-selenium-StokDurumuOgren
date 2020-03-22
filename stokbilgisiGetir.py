from selenium import webdriver
import time

urunURL = 'https://www.robotistan.com/makeblock-mbot-bluetooth-kiti-v11-mavi'
adetYaziKutusu = 'Adet2754'

urunURL = 'https://www.robotistan.com/arduino-uno-r3-klon-usb-kablo-hediyeli-usb-chip-ch340'
adetYaziKutusu = 'Adet2729'

driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.set_window_position(0,0)
driver.set_window_size(800,800)

while True:
    driver.get(urunURL)
    urunAdi = driver.find_element_by_id('productName').text
    time.sleep(5)
    driver.find_element_by_name(adetYaziKutusu).send_keys('1000000000')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="addCartBtn"]/span').click()
    
    time.sleep(5)
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

