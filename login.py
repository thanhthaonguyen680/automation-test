from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.stealmylogin.com/demo.html")
driver.find_element_by_name("username").send_keys("thaonguyen123")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_xpath("//input[@type='submit']").click()


