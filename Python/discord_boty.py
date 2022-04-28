import discord
from discord import Intents
from discord.ext import commands, tasks

import serial
from serial import Serial

import time

TOKEN = "token" #token here
CHANNEL_ID = 941268227588239404

bot = commands.Bot(
  command_prefix = "--",
  intents=Intents.all()
)


async def ping():
    await bot.get_channel(CHANNEL_ID).send("doggo :) <@689565874612469784>")


ser = serial.Serial("/dev/ttyACM0") 
time.sleep(1)
print(ser.name)

@bot.event
async def on_ready():
    print("Starting...")
    beaver.start()
    
@tasks.loop(seconds=1)
async def beaver():
    data_raw = ser.readline()
    decoded_data = (data_raw[0:len(data_raw)-2].decode("utf-8"))
    if decoded_data == ("doge"):
        print("DOG!")
        await ping()


bot.run((TOKEN), bot=True, reconnect=True)