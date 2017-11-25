"""
Author : Kd
Running a Headless Browser but PhantomJS doesn't provide with the capability to auto download so had to use Firefox browser instead
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#For PhantomJS remove profile part and replace Firefox with PhantomJS

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", 'E:\\desktop\\Notebooks\\yearly stock data')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

ff=webdriver.Firefox(firefox_profile=profile)
#ff.set_page_load_timeout(10)
try:
      ff.set_page_load_timeout(20)
      ff.get("https://in.finance.yahoo.com/quote/AAPL/history?p=AAPL")
except Exception:
      webdriver.ActionChains(ff).send_keys(Keys.ESCAPE).perform()    
      #ff.find_element_by_name("p").send_keys(Keys.Control+"Escape")
assert "Yahoo Finance" in ff.title
print(ff.title)
ff.find_element_by_name("p").send_keys("AMD")
ff.find_element_by_xpath("""//*[@id="search-assist-input"]/div[1]/input""").send_keys(Keys.RETURN)

#ff.find_element_by_link_text("Download data").send_keys(Keys.RETURN)
ff.find_element_by_link_text("Download data").send_keys(Keys.RETURN)
