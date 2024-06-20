from selenium impot webdriver
driver = webdriver.Chrome()

driver.get("URL")

driver.find_element(By.NAME,"q").send_keys("mobiles")

products=driver.find_elements(By.XPATH,"//div[@class='_75nlfW']")

for in range(len(products)):
	price = int(i.find_element(By.XPATH,"div//div[@class='Nx9bqj _4b5DiR']").text)
	if price>10000:
		del =i.find_element(BY.XAPTH,"/div//div[@class='k6cAZE dlFt9U']/div/div[2]").text
		
		if del=="Tomorrow":
			pname = i.find_element(BY.XPATH,"div//div[@class='KzDlHZ']").text
			print("pname")