import discord
import asyncio
#import requests
from bs4 import BeautifulSoup
from random import randint



client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('f'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, '')

    if message.content.startswith('help me doctor'):
            await client.send_message(message.channel,"Do you want to roll again? !yes or !no")

    if message.content.startswith('roll a dice Dr'):

            await client.send_message(message.channel,randint(1, 6))
            await client.send_message(message.channel,"Do you want to roll again? !yes or !no")

    if message.content.startswith('!yes'):

            await client.send_message(message.channel,randint(1, 6))
            await client.send_message(message.channel,"Do you want to roll again? !yes or !no")

    if message.content.startswith('!no'):

            await client.send_message(message.channel,'ok')

    if message.content.startswith('hey Dr help me'):
        await client.send_message(message.channel, '')

    if message.content.startswith('help'):
        await client.send_message(message.channel, 'these are the commands !dice, !help, !test' )
        await client.send_message(message.channel, 'voice commands are @summon(Dr java enters the channel), @play "input song"(prefomes web quary and plays song')

    if message.content.startswith('!more'):
        print('test')
       # userInput = str(message[:])
        await client.send_message(message.channel,'ok')
        slicearray[:20]
        for name in slicearray:
            print(name)
            await client.send_message(message.channel, name)



    if message.content.startswith('!webcrawler'):
        await client.send_message(message.channel, 'yes master searching craigslist for computers')
        async def spider(max_pages):
            page = 1
            while page <= max_pages:
                url = "https://cleveland.craigslist.org/search/sya?s=" + str(page)
                source_code = requests.get(url)
                # just the code, no headers
                plain_text = source_code.text
                # BeautifulSoup objects
                soup = BeautifulSoup(plain_text,"html.parser")
                for link in soup.findAll('a', {'class': 'result-title hdrlnk'}):
                    href = "" + link.get('href')
                    title = link.string  # just the text, not the HTML
                    await client.send_message(message.channel, href)
                    await client.send_message(message.channel, title)
                    # get_single_item_data(href)
                page += 1

        await spider(200)
        async def get_single_item_data(item_url):
            source_code = requests.get(item_url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text,"html.parser")

            for item_name in soup.findAll('span', {'class': 'bestof-text'}):
                print(item_name.string)

            for link in soup.findAll('a'):
                href = "" + link.get('href')
                await client.send_message(message.channel, href)

client.run('API Token')
