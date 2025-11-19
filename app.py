from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID, BOT_TOKEN

app = Client("pin_bot", bot_token=BOT_TOKEN)

# Automatic unpin jab koi hor pin kare
@app.on_message(filters.service & filters.pinned_message)
async def auto_unpin_by_non_owner(client: Client, message: Message):
    if not message.pinned_message or not message.from_user:
        return

    who_pinned_id = message.from_user.id

    if who_pinned_id == OWNER_ID:
        return

    try:
        await client.unpin_chat_message(
            chat_id=message.chat.id,
            message_id=message.pinned_message.id
        )
        await message.reply_text("❌ ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴘɪɴ ᴍᴇssᴀɢᴇs! ᴀᴜᴛᴏ-ᴜɴᴘɪɴɴᴇᴅ.")
    except Exception as e:
        print(f"Auto unpin error: {e}")


# /pin command – only owner
@app.on_message(filters.command("pin") & filters.user(OWNER_ID))
async def pin_command(client: Client, message: Message):
    if not message.reply_to_message:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴜsᴇ /ᴘɪɴ")
        return

    try:
        await client.pin_chat_message(
            chat_id=message.chat.id,
            message_id=message.reply_to_message.id,
            disable_notification=False
        )
        await message.reply_text("✅ ᴍᴇssᴀɢᴇ ᴘɪɴɴᴇᴅ ʙʏ ᴏᴡɴᴇʀ!")
    except Exception as e:
        await message.reply_text(f"ᴘɪɴ ғᴀɪʟᴇᴅ: {e}")


# /unpin command – only owner
@app.on_message(filters.command("unpin") & filters.user(OWNER_ID))
async def unpin_command(client: Client, message: Message):
    if not message.reply_to_message:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴜsᴇ /ᴜɴᴘɪɴ")
        return

    try:
        await client.unpin_chat_message(
            chat_id=message.chat.id,
            message_id=message.reply_to_message.id
        )
        await message.reply_text("✅ ᴍᴇssᴀɢᴇ ᴜɴᴘɪɴɴᴇᴅ ʙʏ ᴏᴡɴᴇʀ.")
    except Exception as e:
        await message.reply_text(f"ᴜɴᴘɪɴ ғᴀɪʟᴇᴅ: {e}")


# /unpinall command – only owner
@app.on_message(filters.command("unpinall") & filters.user(OWNER_ID))
async def unpinall_command(client: Client, message: Message):
    try:
        await client.unpin_all_chat_messages(message.chat.id)
        await message.reply_text("🧹 ᴀʟʟ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇs ʜᴀᴠᴇ ʙᴇᴇɴ ᴜɴᴘɪɴɴᴇᴅ!")
    except Exception as e:
        await message.reply_text(f"ᴜɴᴘɪɴᴀʟʟ ғᴀɪʟᴇᴅ: {e}")


# Block non-owner se command use karne ki koshish
@app.on_message(filters.command(["pin", "unpin", "unpinall"]))
async def block_non_owner(client: Client, message: Message):
    await message.reply_text("🚫 ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴘɪɴ ᴄᴏᴍᴍᴀɴᴅs!")
    await message.delete()


print("ʙᴏᴛ sᴛᴀʀᴛᴇᴅ – ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴘɪɴ/ᴜɴᴘɪɴ/ᴜɴᴘɪɴᴀʟʟ 👑")
app.run()
