from selenium import webdriver
import time
import datetime

tarihSaat = datetime.datetime.now()


print("Urun Linki Giriniz")
urunURL = raw_input()
print(urunURL)

print("Yazi Kutusu ID Giriziniz - Adet2729 gibi")
adetYaziKutusu = raw_input()
print(adetYaziKutusu)

print("Dakika Cinsinden Ornekleme Suresi Girin")
ORNEKLEME_SURESI_SANIYE = 60* int (raw_input())
print(ORNEKLEME_SURESI_SANIYE + " Saniyede bir veri cekecek")


driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.set_window_position(0,0)
driver.set_window_size(800,800)

while True:
    logDosyasi = open("stokBilgileri.txt","a")
    driver.get(urunURL)
    urunAdi = driver.find_element_by_id('productName').text
    time.sleep(5)
    driver.find_element_by_name(adetYaziKutusu).send_keys('1000000000')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="addCartBtn"]/span').click()
    
    time.sleep(5)
    mevcutStok = driver.find_element_by_id('myPopup3').text
    
    print( urunAdi + " : " + mevcutStok.split(': ')[1])

    logDosyasi.write("%d" % tarihSaat.year + "-" +"%d" % tarihSaat.month + "-" + "%d" % tarihSaat.day +"-"+ "%d" % tarihSaat.hour + "-" + "%d" % tarihSaat.minute)    
    logDosyasi.write(" : " + mevcutStok.split(': ')[1] + "\n")
    logDosyasi.close()
    time.sleep(ORNEKLEME_SURESI_SANIYE)



driver.close()
