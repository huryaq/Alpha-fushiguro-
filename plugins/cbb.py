from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

message_content = '''👋 <b>Hey {first}\n
🎖️ <u>Available Plans</u>:</b>\n
<blockquote expandable><i>●  ₹80 For 7 Days Prime Membership\n
● ₹199 For 1 Month Prime Membership\n
● ₹249 For 2 Months Prime Membership\n
● ₹349 For 3 Months Prime Membership\n
● ₹499 For 6 Months Prime Membership\n
● ₹699 For 9 Months Prime Membership\n
● ₹999 For 1 Year Prime Membership\n
●  ₹1,999 For Lifetime Prime Membership</i></blockquote>\n
💵 DM - @Nagi_Seishiro_x <code>9322351589@ibl</code>
<b>(Tap to copy UPI Id)</b>\n\n
♻️ <b>If payment is not getting sent on above given QR code then inform Admin, He will give you new QR code</b>\n
‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ'''


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')],
                [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.reply_photo(
            photo=("https://graph.org/file/1e9020a80c983a8853080-632cfe5e165596e90b.jpg"),
            caption=message_content.format(
                first = query.from_user.mention, 
                second = query.from_user.mention
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Owner", url="https://t.me/ABT_Fushiguro"),
                        InlineKeyboardButton("𝗠𝗮𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/Vap_World")
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
