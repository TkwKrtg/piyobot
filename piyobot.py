import discord
import os
from dotenv import load_dotenv
from mhwilds import MonsterHunterWildsBot

load_dotenv() 

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if TOKEN is None:
    print("Failed to get token [error:001]")
    exit()

intents =discord.Intents.default()
client = discord.Client(intents=intents)

# インスタンス作成
mhwilds_list = MonsterHunterWildsBot()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        if "おぴよ" in message.content or "<:hiyoko_goodmorning:857140570194837505>" in message.content:
            await message.channel.send('<:hiyoko_goodmorning:857140570194837505>')
        if "一狩り" in message.content or "ひと狩り" in message.content or "モンハンワイルズ" in message.content or "MHWilds" in message.content or "なに狩ろ" in message.content or "何狩ろ" in message.content or "なに狩る" in message.content or "何狩る" in message.content:
            mhsuggestion = mhwilds_list.suggest_monster()
            await message.channel.send(mhsuggestion)
            await message.channel.send("<:hiyoko_hitokari:1001692854646751332><:hiyoko_karyoku:1011457279003992125>")
        else:
            await message.channel.send('<:hiyoko_car:856717584992305162>')

client.run(TOKEN)