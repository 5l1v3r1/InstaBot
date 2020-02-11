from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import uniform


class InstaBot:
    def __init__(self, username, password):  
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')

        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')

        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_posts(self, hashtag):
        count = 0
        bot = self.bot
        bot.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(3)

        for i in range(1, 3):  # scrolls down twice
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(uniform(2.5, 3.5))
            posts = bot.find_elements_by_class_name('v1Nh3')
            links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in posts]
            # we get links in the format of instagram.com/p/id

            for link in links:  
                count += 1
                if count < 35:  # number of top posts to leave a like on
                    bot.get(link)
                    try:
                        div = bot.find_elements_by_class_name('dCJp8')
                        like = [el.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click() for el in div]
                        print(f'liked photo {link}')
                        time.sleep(uniform(5, 7))
                    except Exception as ex:
                        time.sleep(7)
                else:  # after 45 times the bot exits
                    bot.close()


obj = InstaBot('', '')  # type in your name and password here
obj.login()
obj.like_posts('')  # type the hashtag name (without #)
