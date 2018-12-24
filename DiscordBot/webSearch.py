import discord
import selenium.webdriver as webdriver
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


async def get_result(serchThing):
    url = "https://www.startpage.com/"
   # browser = webdriver.Chrome()
    #browser = webdriver.Chrome('C:\Program Files\chromedriver.exe')
   # browser = webdriver.Opera('C:\Program Files\Opera\launcher.exe')
    browser = webdriver.Chrome('C:\Program Files\chromedriver.exe')

    browser.get(url)
    find_seach_box = browser.find_element_by_id("query")
    find_seach_box.send_keys(serchThing)
    find_seach_box.submit()

    try:
        links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
    except:
        links = browser.find_elements_by_xpath("//h3//a")

    #returns array of links found from the search
    results = []
    for link in links:
        href = link.get_attribute("href")
        print(href)
        await client.send_message(message1.channel,href)
        results.append(href)
    browser.close()
    return results

@client.event
async def on_message(message):
    global message1
    message1=message
    if message.content.startswith('!search'):
       # userInput = str(message[:])
        await client.send_message(message.channel,'I found these links')

        await get_result(str(message.content[7:]))

        await client.send_message(message.channel, str(message.content[7:]))


client.run('API Token')
