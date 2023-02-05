#using selenium to get html content from namu.wiki
from selenium import webdriver
from bs4 import BeautifulSoup

# create an instance of the webdriver
driver = webdriver.Chrome()
# navigate to the page
url = "https://namu.wiki/w/%EC%88%98%EB%8F%84%EA%B6%8C%20%EC%A0%84%EC%B2%A0%203%ED%98%B8%EC%84%A0#s-1"
driver.get(url)
# retrieve the html content
html_content = driver.page_source
# print the html content
print(html_content)
# close the browser
driver.quit()
