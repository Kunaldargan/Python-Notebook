from selenium import webdriver # import webdriver to create FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from os import path
from glob import glob

firefoxProfile = webdriver.FirefoxProfile()
firefoxProfile.set_preference("browser.download.folderList", 2)
firefoxProfile.set_preference("browser.download.manager.showWhenStarting", False)
firefoxProfile.set_preference("browser.download.dir", 'E:\\desktop\\Notebooks\\RDI')
firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
firefoxProfile.set_preference("browser.privatebrowsing.autostart", True)
#firefoxProfile.set_preference('permissions.default.stylesheet', 2)
#firefoxProfile.set_preference('permissions.default.image', 2)
#firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
#firefoxProfile.set_preference("http.response.timeout", 10)
#firefoxProfile.set_preference("dom.max_script_run_time", 10)
"""
def get_data(u):
    print(u)
    try:    
        driver.set_page_load_timeout(8)
        driver.get(u)
        for i in range(15): 
            #home_reports > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(4) > a:nth-child(1)
            xpath="#home_reports > tbody:nth-child(2) > tr:nth-child("+i+") > td:nth-child(4) > a:nth-child(1)"
            driver.find_element_by_xpath(xpath).send_keys(Keys.RETURN)
        webdriver.ActionChains(driver).send_keys(Keys.CONTROL, "w").perform()    

    except Exception:
        #driver.implicitly_wait(10)
        # Interact with elements
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(2)
        if ("Download Report" in driver.page_source):
            print("Dowloading now")
            try:
                for i in range(15): 
                    #home_reports > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(4) > a:nth-child(1)
                    xpath="#home_reports > tbody:nth-child(2) > tr:nth-child("+i+") > td:nth-child(4) > a:nth-child(1)"
                    driver.find_element_by_xpath(xpath).send_keys(Keys.RETURN)
                webdriver.ActionChains(driver).send_keys(Keys.CONTROL, "w").perform()
            except: 
                print("loading time exceeded")
                url.append(u)
                webdriver.ActionChains(driver).send_keys(Keys.CONTROL, "w").perform()
        else:
            url.append(u)
    time.sleep(5)
    #driver.close()
    
# now create browser instance and APPLY the FirefoxProfile

BACKUP PLAN#
def ext():
   l= glob(path.join("E:\\desktop\\Notebooks\\yearly stock data","*.csv"))
   for i in range(len(l)):
    print(path.basename(l[i]).split(".")[0])
ext()
"""
# Visit URL
main="http://www.findthecompany.com"
"""
r= int(input("Till How many pages do u want to extract"))
url=[]
for i in range(r):
           url.append(main+"i")
#url = ["http://rdinvesting.com/reports/?wpv_view_count=397&wpv_paged=1","http://rdinvesting.com/reports/?wpv_view_count=397&wpv_paged=2"]

check=True
"""
service_args = [
    '--proxy=165.84.167.54:8080',
    '--proxy-type=http',
    ]


driver = webdriver.Firefox(firefox_profile=firefoxProfile)
#driver = webdriver.PhantomJS(service_args=service_args)
driver.get(main)
current_url=[]

i= False
while( i is not True):
        time.sleep(12)
        driver.find_element_by_class_name("np-search-tax-input").send_keys("At&T")
        time.sleep(2)
        link = driver.find_element_by_css_selector("span.stnd-btn").send_keys(Keys.RETURN)
        time.sleep(5)
        driver.find_element_by_css_selector("#listing_row_10494214 > td:nth-child(1) > h3:nth-child(1) > a:nth-child(1)").send_keys(Keys.RETURN)
        current_url=driver.current_url
        time.sleep(2)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        links=driver.find_elements_by_tag_name('td')
        for link in links:
            print(link.text)
        i=True
        
  
        #time.sleep(5)
time.sleep(10)
#ssert "company" in driver.title
print(driver.current_url)
"""
for i in range(len(url)):    
        get_data(url[i])
"""        
        
print("hello")
