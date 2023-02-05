# Using selenium to get HTML content from namu.wiki
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
# Function to set up ChromeDriver
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--lang=ko_KR')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--window-size=1920x1080')
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver

if __name__ == "__main__":
    driver = set_chrome_driver()
    url = "https://namu.wiki/w/%EC%88%98%EB%8F%84%EA%B6%8C%20%EC%A0%84%EC%B2%A0%203%ED%98%B8%EC%84%A0/%EC%97%AD%20%EB%AA%A9%EB%A1%9D"
    driver.get(url)
    html_content = driver.page_source
    # parse the html content
    soup = BeautifulSoup(html_content, 'html.parser')
    # find the class "9a52f10e"
    content = soup.find("div", class_="sH7lKmx5 _a5b5640faca9f1712f81cb0b01f8ea51")
    print(content)
    driver.quit()
