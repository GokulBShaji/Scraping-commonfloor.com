from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

df = pd.read_excel('Hyderabad_Builders_links_Database.xlsx')
list_of_links = df['links'].to_list()
l = len(list_of_links)

sf = pd.DataFrame()


l1 = []

p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p7 = []
p8 = []
p9 = []
p10 = []
p11 = []
p12 = []
p13 = []
p14 = []
p15 = []
p16 = []
p17 = []
p18 = []
p19 = []
p20 = []
p21 = []
p22 = []
p23 = []
p24 = []
p25 = []
p26 = []
p27 = []
p28 = []
p29 = []
p30 = []
p31 = []
p32 = []
p33 = []
p34 = []
p35 = []
p36 = []
p37 = []
p38 = []
p39 = []

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
        t1 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[1]')
        p1.append(t1.text)
    except:
        p1.append('NA')
    try:
        t2 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[2]')
        p2.append(t2.text)
    except:
        p2.append('NA')
    try:
        t3 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[3]')
        p3.append(t3.text)
    except:
        p3.append('NA')
    try:
        t4 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[4]')
        p4.append(t4.text)
    except:
        p4.append('NA')
    try:
        t5 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[5]')
        p5.append(t5.text)
    except:
        p5.append('NA')
    try:
        t6 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[6]')
        p6.append(t6.text)
    except:
        p6.append('NA')
    try:
        t7 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[7]')
        p7.append(t7.text)
    except:
        p7.append('NA')
    try:
        t8 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[8]')
        p8.append(t8.text)
    except:
        p8.append('NA')
    try:
        t9 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[9]')
        p9.append(t9.text)
    except:
        p9.append('NA')
    try:
        t10 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[10]')
        p10.append(t10.text)
    except:
        p10.append('NA')
    try:
        t11 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[11]')
        p11.append(t11.text)
    except:
        p11.append('NA')
    try:
        t12 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[12]')
        p12.append(t12.text)
    except:
        p12.append('NA')
    try:
        t13 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[13]')
        p13.append(t13.text)
    except:
        p13.append('NA')
    try:
        t14 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[14]')
        p14.append(t14.text)
    except:
        p14.append('NA')
    try:
        t15 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[15]')
        p15.append(t15.text)
    except:
        p15.append('NA')
    try:
        t16 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[16]')
        p16.append(t16.text)
    except:
        p16.append('NA')
    try:
        t17 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[17]')
        p17.append(t17.text)
    except:
        p17.append('NA')
    try:
        t18 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[18]')
        p18.append(t18.text)
    except:
        p18.append('NA')
    try:
        t19 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[19]')
        p19.append(t19.text)
    except:
        p19.append('NA')
    try:
        t20 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[20]')
        p20.append(t20.text)
    except:
        p20.append('NA')
    try:
        t21 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[21]')
        p21.append(t21.text)
    except:
        p21.append('NA')
    try:
        t22 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[22]')
        p22.append(t22.text)
    except:
        p22.append('NA')
    try:
        t23 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[23]')
        p23.append(t23.text)
    except:
        p23.append('NA')
    try:
        t24 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[24]')
        p24.append(t24.text)
    except:
        p24.append('NA')
    try:
        t25 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[25]')
        p25.append(t25.text)
    except:
        p25.append('NA')
    try:
        t26 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[26]')
        p26.append(t26.text)
    except:
        p26.append('NA')
    try:
        t27 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[27]')
        p27.append(t27.text)
    except:
        p27.append('NA')
    try:
        t28 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[28]')
        p28.append(t28.text)
    except:
        p28.append('NA')
    try:
        t29 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[29]')
        p29.append(t29.text)
    except:
        p29.append('NA')
    try:
        t30 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[30]')
        p30.append(t30.text)
    except:
        p30.append('NA')
    try:
        t31 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[31]')
        p31.append(t31.text)
    except:
        p31.append('NA')
    try:
        t32 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[32]')
        p32.append(t32.text)
    except:
        p32.append('NA')
    try:
        t33 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[33]')
        p33.append(t33.text)
    except:
        p33.append('NA')
    try:
        t34 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[34]')
        p34.append(t34.text)
    except:
        p34.append('NA')
    try:
        t35 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[35]')
        p35.append(t35.text)
    except:
        p35.append('NA')
    try:
        t36 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[36]')
        p36.append(t36.text)
    except:
        p36.append('NA')
    try:
        t37 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[37]')
        p37.append(t37.text)
    except:
        p37.append('NA')
    try:
        t38 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[38]')
        p38.append(t38.text)
    except:
        p38.append('NA')
    try:
        t39 = browser.find_element(By.XPATH, '(//div[@class="amtlist clearfix"]/ul/li)[39]')
        p39.append(t39.text)
    except:
        p39.append('NA')

    print(f"Scraped link number {i+1}")
    sleep(5)
    browser.quit()
    sleep(2)

sf['Project Name']=l1
sf['feature_1']=p1
sf['feature_2']=p2
sf['feature_3']=p3
sf['feature_4']=p4
sf['feature_5']=p5
sf['feature_6']=p6
sf['feature_7']=p7
sf['feature_8']=p8
sf['feature_9']=p9
sf['feature_10']=p10
sf['feature_11']=p11
sf['feature_12']=p12
sf['feature_13']=p13
sf['feature_14']=p14
sf['feature_15']=p15
sf['feature_16']=p16
sf['feature_17']=p17
sf['feature_18']=p18
sf['feature_19']=p19
sf['feature_20']=p20
sf['feature_21']=p21
sf['feature_22']=p22
sf['feature_23']=p23
sf['feature_24']=p24
sf['feature_25']=p25
sf['feature_26']=p26
sf['feature_27']=p27
sf['feature_28']=p28
sf['feature_29']=p29
sf['feature_30']=p30
sf['feature_31']=p31
sf['feature_32']=p32
sf['feature_33']=p33
sf['feature_34']=p34
sf['feature_35']=p35
sf['feature_36']=p36
sf['feature_37']=p37
sf['feature_38']=p38
sf['feature_39']=p39

sf.to_excel('hyderabad_builder_database_features.xlsx', sheet_name='Sheet1', index=False)