from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
import pickledb
import asyncio
import os

db = pickledb.load("sldlink.db", True)
bot = Client('stevebot',
             api_id= int(os.environ["API_ID"]),
             api_hash= os.environ["API_HASH"],
             bot_token= os.environ["BOT_TOKEN"],
             workers= int(os.environ["WORKERS"]),
             sleep_threshold= int(os.environ["THRESHOLD"]) )


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply_text("**Hello \nI Am DRM remover bot** 🤓", quote=True)

@bot.on_message(filters.command('link') & filters.private)
async def convert_link(bot, message):
    if len(message.command) > 1:
        jio_link = message.command[1]
        # print(jio_link)
        copy_after_wvdata = (jio_link.split("wvdata",1)[1]) 
        sld_link = f"https://sldhnecdnems02.cdnsrv.jio.com/jiobeats.cdn.jio.com/content/entry/data{copy_after_wvdata}"
        sep = '_' # removes everything from _ to the end
        stripped_link = sld_link.split(sep, 1)[0]
        db.set(str(message.from_user.id), stripped_link)
        await message.reply_text("**Now Send Code ID Along With /id command**", quote=True)
    else:
        await message.reply_text("**Please Provied Jio Link Along With Command**", quote=True)

@bot.on_message(filters.command('id') & filters.private)
async def id(bot, message):
    try:
        if len(message.command) > 1:
            # ggg
            # db3.get(str(message.from_user.id))
            process = await message.reply_text(f"**Wait! Processing ⚙️**", quote=True)
            await asyncio.sleep(3)
            id = message.command[1]
            sld_link_2 = db.get(str(message.from_user.id))
            final_link = f"{sld_link_2}{id}" # final link https://sldhnecdnems02.cdnsrv.jio.com/jiobeats.cdn.jio.com/content/entry/data/6/27/05c42750ce6611ecb02fb72cf54ee32b_4192.mp4
            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=process.id,
                text=f"**Here Is Your Link:**\n\n`{final_link}`"
                )
            # await message.reply_text(f"**Here Is Your Link:**\n\n`{final_link}`", quote= True)
            db.rem(str(message.from_user.id))
        else:
            await message.reply_text(f"**Please Provied Code ID Along With Command**", quote=True)
    except KeyError:
            error_msg = await message.reply_text(f"**Error:**\n`Please Send The Jio Link First`", quote=True)
            del_msg_id = (int(error_msg.id) - 1)
            await bot.delete_messages(message.chat.id, del_msg_id)
print("Bot Started!")
bot.run()
