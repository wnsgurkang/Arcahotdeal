from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
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
    url = "https://arca.live/b/hotdeal" #핫딜채널에서
    driver.get(url)
    deleted_lists = [] #삭제된 게시글 제목을 담을 리스트
    html_content = driver.page_source #페이지 소스를 가져온다
    soup = BeautifulSoup(html_content, 'html.parser') #그걸 파싱한다
    deleted_list = soup.findAll("div", {'class': 'vrow-top deal deal-close'}) #삭제된 게시글을 찾는다
    #delted list 에서 제목만 뽑아서 deleted_lists에 담는다
    for deleted in deleted_list:
        another_class_element = deleted.find("a", {'class': 'title'})
        if another_class_element:
            deleted_lists.append(another_class_element.text.strip())
    print(deleted_lists)