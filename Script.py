class script(object):
    START_TXT = """ʜᴇʟʟᴏ {},
ᴍʏꜱᴇʟꜰ <a href=https://t.me/{}>{}</a>,\n\ᴛʀᴜꜱᴛ ᴍᴇ! ɪ ᴄᴀɴ ꜱᴘᴇᴇᴅ ᴜᴘ ʏᴏᴜʀ ᴅᴀᴛᴀʙᴀꜱᴇ ᴄʜᴀɴɴᴇʟ ʙᴇʏᴏɴᴅ ɪᴍᴀɢɪɴᴀᴛɪᴏɴ. \n\nᴀʀᴇ ʏᴏᴜ ʀᴇᴀᴅʏ ꜰᴏʀ ᴀɴ ᴇxʜɪʟᴀʀᴀᴛɪɴɢ ʀɪᴅᴇ, ʙᴀʙʏ? 🚀"""
    
    DNT_TEXT = """Hey sweetie {},
Thanks for thinking about us.\nIt seems that you really love <a href=https://t.me/CinemaVenoOfficial >CinemaVenoOfficial</a> work.\n\n<b>For your kind information, we do not ask or force anyone for any kind of payment</b>. But if you really want to donate us then you can send money to us from below links...\n\n💵 Reach Donation Page : <a href=https://t.me/HexaSupportOfficial>Click here...</a>\n\nT❤️ hank you so much..
    """
    REQ_AUTH_TEXT = """ʜᴇʟʟᴏ {},
\nꜱᴏʀʀʏ ꜱᴡᴇᴇᴛɪᴇ.. ʏᴏᴜ ᴍᴜꜱᴛ ʜᴀᴠᴇ ᴛᴏ ʙᴇ ᴛʜᴇ ᴀᴜᴛʜᴇɴᴛɪᴄ ᴜꜱᴇʀ ᴛᴏ ᴄᴏᴍᴘʟᴇᴛᴇ ᴛʜɪꜱ ᴏᴘᴇʀᴀᴛɪᴏɴ...\n\n👮‍♀ 𝚁𝙴𝙿𝙾𝚁𝚃 𝙸𝚂𝚂𝚄𝙴 𝙷𝙴𝚁𝙴: <a href=https://t.me/HexaSupportOfficial>ʜᴇxᴀ ꜱᴜᴘᴘᴏʀᴛ</a>\n\n
    """
    ALRDY_UPLDD_TEXT = """✅ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ.\n\nName:{}\nPlease make sure about your spelling before submiting request..."""
    HELP_TXT = """𝙷𝙴𝚈 {}
ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ ꜰᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/CinemaVenoOfficial>CinemaVenoOfficial</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙺𝙾𝚈𝙴𝙱
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- ʜᴇxᴀ ɪꜱ ᴀ ᴘʀᴏꜰᴇꜱꜱɪᴏɴᴀʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ. 
- ꜱᴏᴜʀᴄᴇ - <a href=https://t.me/CinemaVenoOfficial>ɴᴏᴋɪ ɪʀɴᴏ</a>"  

<b>ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ:</b>
- <a href=https://t.me/CinemaVenoOfficial>CinemaVenoOfficial</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Hexa will respond whenever that keyword hits the message

<b>NOTE:</b>
1. BOT should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/CinemaVenoOfficial)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ.
 ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""
    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>

- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/connect</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ ᴘᴍ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ ꜰʀᴏᴍ ᴘᴍ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""
    EXTRAMOD_TXT = """ʜᴇʟᴘ: <b>ᴇxᴛʀᴀ ᴍᴏᴅᴜʟᴇꜱ</b>

<b>NOTE:</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ʜᴇxᴀ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    PROGRESS_BAR = """\n
╭━━━━❰ PROGRESS BAR ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """
