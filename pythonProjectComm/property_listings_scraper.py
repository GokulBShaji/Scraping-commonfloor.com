from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd

df = pd.read_excel('Hyderabad_Builders_links_Database.xlsx')
list_of_links = df['links'].to_list()
l = len(list_of_links)
sf = pd.DataFrame()

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []
l10 = []
l11 = []
l12 = []
l13 = []
l14 = []
l15 = []
l16 = []
l17 = []
l18 = []
l19 = []


for i in range(l):
    service = Service(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(list_of_links[i])
    browser.maximize_window()
    try:
        i1 = browser.find_element(By.XPATH, '//h1/span')
        l1.append(i1.text)
    except:
        l1.append('NA')
    try:
        p1 = browser.find_element(By.XPATH, '(//div[@class="recentlypro mh77"]/h3)[1]')
        l2.append(p1.text)
    except:
        l2.append('NA')
    try:
        p2 = browser.find_element(By.XPATH, '(//div[@class="recentlypro mh77"]/div)[1]')
        l3.append(p2.text)
    except:
        l3.append('NA')
    try:
        p3 = browser.find_element(By.XPATH, '(//div[@class="recentlypro mh77"]/div/span)[1]')
        l4.append(p3.text)
    except:
        l4.append('NA')
    try:
        p4 = browser.find_element(By.XPATH, '(//div[@class="recentlypro mh77"]/h3)[2]')
        l5.append(p4.text)
    except:
        l5.append('NA')
    try:
        p5 = browser.find_element(By.XPATH, '(//div[@class="recentlypro mh77"]/div)[2]')
        l6.append(p5.text)
    except:
        l6.append('NA')
    try:
        p6 = browser.find_element(By.XPATH, '(//div[@class="recentlypro mh77"]/div/span)[2]')
        l7.append(p6.text)
    except:
        l7.append('NA')
    try:
        p7 = browser.find_element(By.XPATH, '(//div[@class="recentlypro mh77"]/h3)[3]')
        l8.append(p7.text)
    except:
        l8.append('NA')
    try:
        p8 = browser.find_element(By.XPATH, '(//div[@class="recentlypro mh77"]/div)[3]')
        l9.append(p8.text)
    except:
        l9.append('NA')
    try:
        p9 = browser.find_element(By.XPATH, '(//div[@class="recentlypro mh77"]/div/span)[3]')
        l10.append(p9.text)
    except:
        l10.append('NA')
    try:
        p10 = browser.find_element(By.XPATH, '(//div[@class="body"]/div[@class="col"])[1]')
        l11.append(p10.text)
    except:
        l11.append('NA')
    try:
        p11 = browser.find_element(By.XPATH, '(//div[@class="body"]/div[@class="col"])[2]')
        l12.append(p11.text)
    except:
        l12.append('NA')
    try:
        p12 = browser.find_element(By.XPATH, '(//div[@class="body"]/div[@class="col"])[4]')
        l13.append(p12.text)
    except:
        l13.append('NA')
    try:
        p13 = browser.find_element(By.XPATH, '(//div[@class="body"]/div[@class="col"])[6]')
        l14.append(p13.text)
    except:
        l14.append('NA')
    try:
        p14 = browser.find_element(By.XPATH, '(//div[@class="body"]/div[@class="col"])[7]')
        l15.append(p14.text)
    except:
        l15.append('NA')
    try:
        p15 = browser.find_element(By.XPATH, '(//div[@class="body"]/div[@class="col"])[9]')
        l16.append(p15.text)
    except:
        l16.append('NA')
    try:
        p16 = browser.find_element(By.XPATH, '(//div[@class="body"]/div[@class="col"])[11]')
        l17.append(p16.text)
    except:
        l17.append('NA')
    try:
        p17 = browser.find_element(By.XPATH, '(//div[@class="body"]/div[@class="col"])[12]')
        l18.append(p17.text)
    except:
        l18.append('NA')
    try:
        p18 = browser.find_element(By.XPATH, '(//div[@class="body"]/div[@class="col"])[14]')
        l19.append(p18.text)
    except:
        l19.append('NA')

    print(f"Scraped link number {i + 1}")

    sleep(3)
    browser.quit()
    sleep(2)

sf['Project Name']=l1
sf['listing_type_1']=l2
sf['SA_type1']=l3
sf['price_type1']=l4
sf['listing_type_2']=l5
sf['SA_type2']=l6
sf['price_type2']=l7
sf['listing_type_3']=l8
sf['SA_type3']=l9
sf['price_type3']=l10
sf['UC_listing_type_1']=l11
sf['UC_SA_type1']=l12
sf['UC_price_type1']=l13
sf['UC_listing_type_2']=l14
sf['UC_SA_type2']=l15
sf['UC_price_type2']=l16
sf['UC_listing_type_3']=l17
sf['UC_SA_type3']=l18
sf['UC_price_type3']=l19

sf.to_excel('property_listings_hyderabad.xlsx', sheet_name='Sheet1', index=False)