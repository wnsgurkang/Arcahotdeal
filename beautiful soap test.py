from selenium import webdriver

# create an instance of the webdriver
driver = webdriver.Chrome()

# navigate to the page
url = "https://namu.wiki/w/수도권%20전철%203호선"
driver.get(url)

# retrieve the html content
html_content = driver.page_source

# print the html content
print(html_content)

# close the browser
driver.quit()