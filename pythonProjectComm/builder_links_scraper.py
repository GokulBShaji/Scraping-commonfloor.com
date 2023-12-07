from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd

df = pd.DataFrame()

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()

browser = webdriver.Chrome(service=service, options=options)

browser.get('https://www.commonfloor.com/all-apartments-in-ameenpur/psl-3doi8b')
#browser.get('https://www.commonfloor.com/all-apartments-in-bachupally/psl-69fxzk')
#browser.get('https://www.commonfloor.com/all-apartments-in-kondapur/psl-dxyh16')
#browser.get('https://www.commonfloor.com/all-apartments-in-miyapur/psl-c6vr3c')
#browser.get('https://www.commonfloor.com/all-apartments-in-shadnagar/psr-51c1e6139267a')
browser.maximize_window()

l1 =[]
l2 =[]
l3 =[]
l4 =[]
l5 =[]
l6 =[]
l7 =[]
l8 =[]
l9 =[]
l10 =[]
l11 =[]
l12 =[]
l13 =[]
l14 =[]
l15 =[]
l16 =[]
l17 =[]
l18 =[]
l19 =[]
l20 =[]

option_list = [2,6]
#option_list = [2]
#option_list = [2,24]
#option_list = [2,24]
#option_list = [2]
def correct_link(a):
    l = len(a)
    b = a[::-1]
    for i in range(l):
        if b[i]==',':
            c = b[:i-10]
            d = len(c)
    for i in range(d):
        if c[i]=='F':
            e = c[2:i]
            f = c[i+3:d]
            g = e+"/"+f
            h = 'https://www.commonfloor.com/'
            result =h+g[::-1]
    return result

for i in range(6):
#for i in range(11):
#for i in range(25):
#for i in range(25):
#for i in range(11):
    print(f"scraping page {i+1}")
    if i == 0:
        i1 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[1]')
        i2 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[2]')
        i3 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[3]')
        i4 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[4]')
        i5 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[5]')
        i6 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[6]')
        i7 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[7]')
        i8 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[8]')
        i9 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[9]')
        i10 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[10]')
        i11 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[11]')
        i12 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[12]')
        i13 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[13]')
        i14 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[14]')
        i15 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[15]')
        i16 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[16]')
        i17 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[17]')
        i18 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[18]')
        i19 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[19]')
        i20 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[20]')
        l1.append(i1.get_attribute('href'))
        l2.append(i2.get_attribute('href'))
        l3.append(i3.get_attribute('href'))
        l4.append(i4.get_attribute('href'))
        l5.append(i5.get_attribute('href'))
        l6.append(i6.get_attribute('href'))
        l7.append(i7.get_attribute('href'))
        l8.append(i8.get_attribute('href'))
        l9.append(i9.get_attribute('href'))
        l10.append(i10.get_attribute('href'))
        l11.append(i11.get_attribute('href'))
        l12.append(i12.get_attribute('href'))
        l13.append(i13.get_attribute('href'))
        l14.append(i14.get_attribute('href'))
        l15.append(i15.get_attribute('href'))
        l16.append(i16.get_attribute('href'))
        l17.append(i17.get_attribute('href'))
        l18.append(i18.get_attribute('href'))
        l19.append(i19.get_attribute('href'))
        l20.append(i20.get_attribute('href'))

    else:
        i1 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[1]')
        i2 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[2]')
        i3 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[3]')
        i4 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[4]')
        i5 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[5]')
        i6 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[6]')
        i7 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[7]')
        i8 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[8]')
        i9 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[9]')
        i10 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[10]')
        i11 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[11]')
        i12 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[12]')
        i13 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[13]')
        i14 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[14]')
        i15 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[15]')
        i16 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[16]')
        i17 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[17]')
        i18 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[18]')
        i19 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[19]')
        i20 = browser.find_element(By.XPATH, '(//div[@class="cf-tile"]/a)[20]')
        k1 = i1.get_attribute('onclick')
        y1 = correct_link(k1)
        l1.append(y1)
        k2 = i2.get_attribute('onclick')
        y2 = correct_link(k2)
        l2.append(y2)
        k3 = i3.get_attribute('onclick')
        y3 = correct_link(k3)
        l3.append(y1)
        k4 = i4.get_attribute('onclick')
        y4 = correct_link(k4)
        l4.append(y4)
        k5 = i5.get_attribute('onclick')
        y5 = correct_link(k5)
        l5.append(y5)
        k6 = i6.get_attribute('onclick')
        y6 = correct_link(k6)
        l6.append(y6)
        k7 = i7.get_attribute('onclick')
        y7 = correct_link(k7)
        l7.append(y7)
        k8 = i8.get_attribute('onclick')
        y8 = correct_link(k8)
        l8.append(y8)
        k9 = i9.get_attribute('onclick')
        y9 = correct_link(k9)
        l9.append(y9)
        k10 = i10.get_attribute('onclick')
        y10 = correct_link(k10)
        l10.append(y10)
        k11 = i11.get_attribute('onclick')
        y11 = correct_link(k11)
        l11.append(y11)
        k12 = i12.get_attribute('onclick')
        y12 = correct_link(k12)
        l12.append(y12)
        k13 = i13.get_attribute('onclick')
        y13 = correct_link(k13)
        l13.append(y13)
        k14 = i14.get_attribute('onclick')
        y14 = correct_link(k14)
        l14.append(y14)
        k15 = i15.get_attribute('onclick')
        y15 = correct_link(k15)
        l15.append(y15)
        k16 = i16.get_attribute('onclick')
        y16 = correct_link(k16)
        l16.append(y1)
        k17 = i17.get_attribute('onclick')
        y17 = correct_link(k17)
        l17.append(y17)
        k18 = i18.get_attribute('onclick')
        y18 = correct_link(k18)
        l18.append(y18)
        k19 = i19.get_attribute('onclick')
        y19 = correct_link(k19)
        l19.append(y19)
        k20 = i20.get_attribute('onclick')
        y20 = correct_link(k20)
        l20.append(y20)



    if (i+1) in option_list:
        next_button = browser.find_element(By.XPATH,'(//div[@id="results"]/div/ul/li/a)[4]')
    else:
        next_button = browser.find_element(By.XPATH, '(//div[@id="results"]/div/ul/li/a)[3]')
    next_button.click()
    sleep(7)

flat_list = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10 + l11 + l12 + l13 + l14 + l15 + l16 + l17 + l18 + l19 + l20
flat_set = set(flat_list)
flat_new_list = list(flat_set)

print(flat_list)
print(len(flat_list))
print(flat_set)
print(len(flat_set))
print(flat_new_list)
print(len(flat_new_list))

df['links'] = flat_new_list

df.to_excel('ameenpur_builder.xlsx', sheet_name='Sheet1', index=False)
#df.to_excel('bachupally_builder.xlsx', sheet_name='Sheet1', index=False)
#df.to_excel('kondapur_builder.xlsx', sheet_name='Sheet1', index=False)
#df.to_excel('miyapur_builder.xlsx', sheet_name='Sheet1', index=False)
#df.to_excel('shadnagar_builder.xlsx', sheet_name='Sheet1', index=False)

sleep(20)
browser.quit()