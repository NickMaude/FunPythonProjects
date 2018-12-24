import discord
import selenium.webdriver as webdriver
import asyncio
from selenium.webdriver.support import expected_conditions as EC
client = discord.Client()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import threading
import time
import ControlledVaribles

global array1



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


async def get_netflix(search):
    url= 'https://www.netflix.com/search?q=' + search
    email = '------'
    password='-------'
    driver = webdriver.Chrome('C:\Program Files\chromedriver')
    #driver = ControlledVaribles.driver
    driver.get(url)
    WebDriverWait(driver, 10)

    find_email_box = driver.find_element_by_id('email')
    find_email_box.send_keys(email)

    find_password_box = driver.find_element_by_id('password')
    find_password_box.send_keys(password)
    find_password_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 30)
    wait=WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@style='background-image:url(https://assets.nflxext.com/ffe/profiles/avatars_v2/320x320/PICON_027.png);']")))
    driver.find_element_by_xpath("//*[@style='background-image:url(https://assets.nflxext.com/ffe/profiles/avatars_v2/320x320/PICON_027.png);']").click()

    await client.edit_message(responce, 'ok, i found some titles they are')
    WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    time.sleep(2)

    ControlledVaribles.driver=driver
    links = driver.find_elements_by_class_name('slider-refocus')


    arrayname = []
    for link in links[:1]:
        name = link.get_attribute("aria-label")
        print(name)
        arrayname.append(name)
        ControlledVaribles.slicearray.append((name))
        await client.send_message(message1.channel,name)


    arrayname = []

    for link in links[:10]:
        name = link.get_attribute("aria-label")
        print(name)
        ControlledVaribles.slicearray.append((name))
        arrayname.append(name)
        #await client.send_message(message1.channel, name)
    array1=arrayname

    await client.send_message(message1.channel, 'is that what your looking for !watch or !more')
    time.sleep(5)




async def discord_call(serchThing):
    url = "https://discordapp.com/login?redirect_to=%2Fchannels%2F%40me"
    email = '--------'
    password = '----'
    browser = webdriver.Chrome('C:\Program Files\chromedriver')
    wait = WebDriverWait(browser, 10)
    browser.get(url)

    find_email_box = browser.find_element_by_xpath("//*[@class='inputDefault-_djjkz input-cIJ7To size16-14cGz5']")
    find_email_box.send_keys(email)
    find_email_box.submit()

    find_password_box = browser.find_element_by_xpath("//*[@type='password']")
    find_password_box.send_keys(password)
    find_password_box.send_keys(Keys.RETURN)
    find_password_box.submit()
    WebDriverWait(browser, 50)
    browser.implicitly_wait(10) #change the wait time depending on how fast the computer is


    browser.implicitly_wait(100)

    browser.implicitly_wait(30)


    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'friends-row')))

    browser.find_element_by_class_name("friends-row").click()

    browser.find_element_by_xpath("//*[@name='VideoCamera']").click()

@client.event
async def on_message(message):
    global message1
    message1=message
    if message.content.startswith('!netflix'):
        print(message1)
       # userInput = str(message[:])
        mes = await client.send_message(message.channel,'thinking...')
        global responce
        responce=mes

        await get_netflix(str(message.content[8:]))

        if message.content.startswith('!watch'):

            import ControlledVaribles
            if (len(ControlledVaribles.slicearray) == 0):
                print('search for a movie first')
                await client.send_message(message.channel, 'search for a movie first')
            try:
                ControlledVaribles.driver.find_element_by_xpath("//*[@aria-label=" + message + "]").click()
            except:
                print('invalid name')
                await client.send_message(message.channel, 'invalid name try agan')
                return None
                await discord_call(str(message.content[8:]))
        if message.content.startswith('!more'):
            import ControlledVaribles
            print('test')
            # userInput = str(message[:])
            await client.send_message(message.channel, 'ok')
            for name in ControlledVaribles.slicearray[:20]:
                print(name)
                await client.send_message(message.channel, name)


#        await discord_call(str(message.content[8:]))


client.run('API Token')
