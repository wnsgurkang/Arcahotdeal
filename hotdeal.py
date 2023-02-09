#나도 모르는 미지의 영역, 건들었다가는 *될지도 모르는 영역
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
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver
#여기서부터는 그래도 아는 영역

badges = [] #뱃지를 담을 리스트
delivery_prices = [] #배송비를 담을 리스트
prices = [] #가격을 담을 리스트
titles = [] #제목을 담을 리스트
shops = [] #쇼핑몰 이름을 담을 리스트
links = [] #링크를 담을 리스트
deleted_lists = [] #삭제된 핫딜의 제목을 담을 리스트

def list_maker(fromsoup, check, list_name):
    for check in fromsoup:
        if check.text.strip() != '':
            list_name.append(check.text.strip())
        elif check.text.strip() == '':
            list_name.append('카테고리 없음')
            
def hotdeal(page_num): #핫딜 함수
    url = "https://arca.live/b/hotdeal?p="+str(page_num) #핫딜채널에서
    
    driver = set_chrome_driver() #새 드라이버 세팅
    
    print(url) 
    
    driver.get(url)
    
    html_content = driver.page_source #페이지 소스를 가져온다
    soup = BeautifulSoup(html_content, 'html.parser') #그걸 파싱한다
    shop = soup.findAll("span", {'class': 'deal-store'}) #핫딜채널에서 쇼핑몰 이름을 가져온다
    title = soup.findAll("a", {'class': 'title'}) #핫딜채널에서 제목을 가져온다
    badge = soup.findAll("a", {'class': 'badge'}) #핫딜채널에서 뱃지를 가져온다
    price = soup.findAll("span", {'class': 'deal-price'}) #핫딜채널에서 가격을 가져온다
    delivery_price = soup.findAll("span", {'class': 'deal-delivery'}) #핫딜채널에서 배송비를 가져온다
    link = soup.findAll("a", {'class': 'title'}) #핫딜채널에서 링크를 가져온다
    deleted_list = soup.findAll("div", {'class': 'vrow-top deal deal-close'})

    list_maker(shop, 'deal-store', shops) #쇼핑몰 이름을 리스트에 담는다
    list_maker(badge, 'badge', badges) #뱃지를 리스트에 담는다
    list_maker(price, 'deal-price', prices) #가격을 리스트에 담는다
    list_maker(delivery_price, 'deal-delivery', delivery_prices) #배송비를 리스트에 담는다
    
    for deleted in deleted_list: #구조상 한 번 더 검색해야함
        another_class_element = deleted.find("a", {'class': 'title'})
        if another_class_element:
            deleted_lists.append(another_class_element.text.strip())
    
    for titles in title: 
        if titles.text.strip() == '핫딜 채널':
            pass
        elif titles.text.strip() != '':
            titles.append(title.text.strip())
        elif title.text.strip() == '':
            titles.append('제목 없음')

    for links in link:
        links.append(link.get('href'))
    driver.quit() #드라이버를 종료한다

    
if __name__ == "__main__":
    for page_num in range(1, 3):
        hotdeal(page_num) 

for a in range(0, len(shops)): #리스트를 출력한다
    print(shops[a], titles[a], badges[a], prices[a], delivery_prices[a],'arca.live',links[a])
