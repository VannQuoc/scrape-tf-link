import requests
from bs4 import BeautifulSoup
import random
import telebot
import string
from concurrent.futures import ThreadPoolExecutor

hit = "https://api.telegram.org/bot5678937930:AAForYgL5zts5wawsdfmfgP_5-sraeugnp8/sendMessage?chat_id=-1001878033586"

def testflight(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        span_element = soup.find('span', string='This beta is full.')

        title_tag = soup.title
        if title_tag and "Join the" in title_tag.text and "beta - TestFlight - Apple" in title_tag.text:
            start_index = title_tag.text.find("Join the") + len("Join the")
            end_index = title_tag.text.find("beta - TestFlight - Apple")
            app = title_tag.text[start_index:end_index].strip()
        if span_element:
            print(url, " ", app, " Full")
        else:
            print(url, " ", app, " Success")
            bot_token = '5678937930:AAForYgL5zts5wawsdfmfgP_5-sraeugnp8'  
            bot = telebot.TeleBot(bot_token)
            chat_id = '-1001878033586'
            msg = f"{app}\n{url}\nTình Trạng: Live\nTool By MonLeoHayKhok"
            bot.send_message(chat_id, msg)
    else:
        print(f"{url} failed with status code: {response.status_code}")

if __name__ == "__main__":
    while True:
        urls = [f"https://testflight.apple.com/join/{''.join(random.choices(string.ascii_letters + string.digits, k=8))}" for _ in range(10)]
        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(testflight, urls)
