import os
from config import Config
from .fonts import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'zautebot'

    # start text
    text = f"""👋🏻Hi {m.from_user.mention(style='md')}!
    
** JUST SEND ME ANY TEXT FOR CHANGE FONT**"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('ᴊᴏɪɴ ɢʀᴏᴜᴩ', url=f"https://t.me/HD_Sanatan_Movies"),
            InlineKeyboardButton('ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ', url=f"https://t.me/Sanatan_Movies")
            ],[
            InlineKeyboardButton('ᴛɢ ᴀɴᴅ ɪɴꜱᴛᴀ ʜᴀᴄᴋ ʙᴏᴛ', url=f"https://t.me/RTG_Premium_Bot"),
            InlineKeyboardButton('ᴛʀᴀᴅᴇ ʙᴏᴛ', url=f"https://t.me/Colour_Trading_Robot")
        ]
    ]
    await m.reply_photo(
        photo="https://graph.org/file/1751949660c59152c9962-e49c2ed67ef33b6189.jpg", 
        caption=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛', callback_data='style+typewriter'),
        InlineKeyboardButton('Oᨘuᨘtᨘlᨘiᨘnᨘeᨘ', callback_data='style+outline'), # <--- text updated for consistency
        InlineKeyboardButton('𝐒𝐞𝐫𝐢𝐟', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('𝑺𝒆𝒓𝒊𝒇', callback_data='style+bold_cool'),
        InlineKeyboardButton('𝑆𝑒𝑟𝑖𝑓', callback_data='style+cool'),
        InlineKeyboardButton('Sᴍᴀʟʟ Cᴀᴘs', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('𝓈𝒸𝓇𝒾𝓅𝓉', callback_data='style+script'),
        InlineKeyboardButton('𝓼𝓬𝓻𝓲𝓹𝓽', callback_data='style+script_bolt'),
        InlineKeyboardButton('ᵗⁱⁿʸ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('ᑕOᗰIᑕ', callback_data='style+comic'),
        InlineKeyboardButton('𝗦𝗮𝗻𝘀', callback_data='style+sans'),
        InlineKeyboardButton('𝙎𝙖𝙣𝙨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('𝘚𝘢𝘯𝘴', callback_data='style+slant'),
        InlineKeyboardButton('𝖲𝖺𝗇𝗌', callback_data='style+sim'),
        InlineKeyboardButton('Circles', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎', callback_data='style+circle_dark'),
        InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
        InlineKeyboardButton('𝕲𝖔𝖙𝖍𝖎𝖈', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡', callback_data='style+cloud'),
        InlineKeyboardButton('H̆̈ă̈p̆̈p̆̈y̆̈', callback_data='style+happy'),
        InlineKeyboardButton('S̑̈ȃ̈d̆̈', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('🇸 🇵 🇪 🇨 🇮 🇦 🇱 ', callback_data='style+special'),
        InlineKeyboardButton('🅂🅀🅄🄰🅁🄴🅂', callback_data='style+squares'),
        InlineKeyboardButton('🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎', callback_data='style+squares_bold'),
        ],[
        InlineKeyboardButton('ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ', callback_data='style+andalucia')
        ]]
    
    if hasattr(m, "answer"):
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        # 🌟 ZAROORI BADLAV: User ke message par reply_to_message_id ke sath reply bhejein
        await m.reply_text(
            text="**Select Your Style From Below Buttons 👇**", 
            reply_markup=InlineKeyboardMarkup(buttons),
            reply_to_message_id=m.id
        )

@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    elif style == 'outline':
        cls = Fonts.outline
    elif style == 'serif':
        cls = Fonts.serief
    elif style == 'bold_cool':
        cls = Fonts.bold_cool
    elif style == 'cool':
        cls = Fonts.cool
    elif style == 'small_cap':
        cls = Fonts.smallcap
    elif style == 'script':
        cls = Fonts.script
    elif style == 'script_bolt':
        cls = Fonts.bold_script
    elif style == 'tiny':
        cls = Fonts.tiny
    elif style == 'comic':
        cls = Fonts.comic
    elif style == 'sans':
        cls = Fonts.san
    elif style == 'slant_sans':
        cls = Fonts.slant_san
    elif style == 'slant':
        cls = Fonts.slant
    elif style == 'sim':
        cls = Fonts.sim
    elif style == 'circles':
        cls = Fonts.circles
    elif style == 'circle_dark':
        cls = Fonts.dark_circle
    elif style == 'gothic':
        cls = Fonts.gothic
    elif style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    elif style == 'cloud':
        cls = Fonts.cloud
    elif style == 'happy':
        cls = Fonts.happy
    elif style == 'sad':
        cls = Fonts.sad
    elif style == 'special':
        cls = Fonts.special
    elif style == 'squares':
        cls = Fonts.square
    elif style == 'squares_bold':
        cls = Fonts.dark_square
    elif style == 'andalucia':
        cls = Fonts.andalucia
    elif style == 'manga':
        cls = Fonts.manga
    elif style == 'stinky':
        cls = Fonts.stinky
    elif style == 'bubbles':
        cls = Fonts.bubbles
    elif style == 'underline':
        cls = Fonts.underline
    elif style == 'ladybug':
        cls = Fonts.ladybug
    elif style == 'rays':
        cls = Fonts.rays
    elif style == 'birds':
        cls = Fonts.birds
    elif style == 'slash':
        cls = Fonts.slash
    else:
        return

    # 🌟 ZAROORI BADLAV: Sahi se user_text nikalne ka tareeka
    if m.message.reply_to_message and m.message.reply_to_message.text:
        user_text = m.message.reply_to_message.text
    else:
        await m.message.edit_text("❌ **Error:** Original text nahi mila! Kripya dobara text bhejein.")
        return

    new_text = cls(user_text)
    
    # Text edit karne ke liye try-except block
    try:
        await m.message.edit_text(
            text=new_text, 
            reply_markup=m.message.reply_markup
        )
    except Exception as e:
        print(f"Error updating text: {e}")
