from email.quoprimime import quote
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
import requests
import os

base_url = "https://api.l0calserve4.ml/"

bot = Client('hentaibot',
             api_id= int(os.environ["API_ID"]),
             api_hash= os.environ["API_HASH"],
             bot_token= os.environ["BOT_TOKEN"],
             workers= int(os.environ["WORKERS"]),
             sleep_threshold= int(os.environ["THRESHOLD"]),)

@bot.on_message(filters.command('start') & filters.private)
def start(bot, message):
    # user_id = message.from_user.id
    # print(user_id)
    message.reply_text("Hello! \nI Am Hentai \nAlways Horny 🥵 Like you", quote=True)

# pussy section 
@bot.on_message(filters.command('pussy') & filters.private)
def pussy(bot, message):
    pussy_api_url = base_url + "hmtai/v2_4/pussy"
    # print(pussy_api_url)
    r = requests.get(pussy_api_url)
    data = r.json()
    img_link = str(data)
    message.reply_photo(img_link, quote=True)

# cum section

@bot.on_message(filters.command('cum') & filters.private)
def cum(bot, message):
    cum_api_url = base_url + "hmtai/v2_4/cum"
    # print(cum_api_url)
    r = requests.get(cum_api_url)
    data = r.json()
    img_link = str(data)
    message.reply_photo(img_link, quote=True)

# blowjob section 

@bot.on_message(filters.command('blowjob') & filters.private)
def bj(bot, message):
    bj_api_url = base_url + "hmtai/v2_4/blowjob"
    # print(bj_api_url)
    r = requests.get(bj_api_url)
    data = r.json()
    img_link = str(data)
    message.reply_photo(img_link, quote=True)

# creampie section

@bot.on_message(filters.command('creampie') & filters.private)
def creampie(bot, message):
    creampie_api_url = base_url + "hmtai/v2_4/creampie"
    # print(creampie_api_url)
    r = requests.get(creampie_api_url)
    data = r.json()
    img_link = str(data)
    message.reply_photo(img_link, quote=True)
print("I am alive")
bot.run()
