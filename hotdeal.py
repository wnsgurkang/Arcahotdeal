#나도 모르는 미지의 영역, 건들었다가는 *될지도 모르는 영역
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import  discord
import asyncio

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
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
        deleted_add = deleted.find("a", {'class': 'title'})
        if deleted_add:
            deleted_lists.append(deleted_add.text.strip())
    
    for title_add in title: #title class의 구조상 핫딜 채널 이라는게 자동적으로 나옴, 그걸 제외하고 리스트에 담는다
        if title_add.text.strip() == '핫딜 채널':
            pass
        elif title_add.text.strip() != '':
            titles.append(title_add.text.strip())
        elif title_add.text.strip() == '':
            titles.append('제목 없음')

    for link_add in link:
        links.append(link_add.get('href'))
    driver.quit() #드라이버를 종료한다

def discord_bot(input_token) : #디스코드 봇 함수   
    client = discord.Client()
    async def on_ready():
        print(client.user.id)
        print("ready")
        game = discord.Game("arca.live 감시중...")
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(message):
        if message.content.startswith("!핫딜"):
            for a in range(0, len(shops)):
                if shops[a] in deleted_lists:
                    pass
                else:
                    await message.channel.send(shops[a], titles[a], badges[a], prices[a], delivery_prices[a],'arca.live',links[a])
    
    async def embed_task(message):
        if message.content.startswith("!embedtest"):   
            await client.wait_until_ready()
            channel = client.get_channel(819719798345695235)

            while not client.is_closed():
                embed = discord.Embed(title="Example Embed", description="This is an example embed.")
                await channel.send(embed=embed)
                await asyncio.sleep(60)

    client.run(input_token)


if __name__ == "__main__":
    for page_num in range(1, 3):
        hotdeal(page_num) 

for a in range(0, len(shops)): #리스트를 출력한다
    print(shops[a], titles[a], badges[a], prices[a], delivery_prices[a],'arca.live',links[a])