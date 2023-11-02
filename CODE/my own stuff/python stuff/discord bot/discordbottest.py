# this example requires the 'message_content' intent to be enabled in the gateway intents settings for your bot

import discord
import logging # for logging
import logging.handlers # for logging
import asyncio # for the main loop
import random # for generating random sentences

# bot token 
TOKEN = 'OTUxNjczMjk2Njc4Njk5MTAw.GawGpf.QcV5mu4q708-lPCjMjG4JaIZnTuIwGksQPDGSM'

# channel id where the bot will read and send messages 
CHANNEL_ID = 1007863235724189727

# code for a rotating file handler that ouputs DEBUG output for everything except the http requests 
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)


intents = discord.Intents.default()
intents.message_content = True

# create discord client
client = discord.Client(intents = intents)

# list to store previously read messages
message_history = []

# event to run when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# event to run when a message is sent in the specified channel
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == CHANNEL_ID:
        # add the message content to the message history
        message_history.append(message.content)
        
# function to generate random sentences and send them to the specified channel
def generate_random_sentences():
    # use random words from the message history to generate a sentence 
    if len(message_history) > 0: 
        random_message = random.choice(message_history)
        words = random_message.split()
        random_words = random.sample(words, random.randint(1, len(words)))
        return ' '.join(random_words)
    else:
        return "no message to generate a sentence from"

# main loop to send random sentences every couple of minutes 
async def send_random_sentences():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    
    while not client.is_closed(): 
        random_sentence = generate_random_sentences()
        await channel.send(random_sentence)
        await asyncio.sleep(120) # send a message every 2 minutes 

# assume client refers to a discord.Client subclass...
# suppress the default configuration since we have our own

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(send_random_sentences())
    client.run(TOKEN)