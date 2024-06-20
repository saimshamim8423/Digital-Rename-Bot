# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "21118391")
    API_HASH = os.environ.get("API_HASH", "43b91164d7825dc577c2baa7c6cdcee6")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQFCPbcAmOrlu6evMUo1OnH8LGya2LYim9nbmvgsCiumxSLEb8IPpntxdxdcJMPV69M_fdexcvHCW-GJbeHSWZdCG0NltWAg2mgBhI913453qzZUlQTBumgw3pyWkgrUVE5odf31ZhKZC3MsI3uqKhKeKZ78hnLwBPFxSVI9fdhjgvpVxsgjvqkM3EaBKu9jIjDWgkPD0MzJLeo4BH0hxB9h-huHYBKoJTC3_rhexRwuq-9m3ZudPaVxhBmn4KHH86K01PPVjQrX3Ga1CGHkVHccqF_pqXHdarC-j_d7On3LOxSdkaAG7r8eHuSfyFrrxz_2j1rHN2On58jfSN1Lk3XmtcbGawAAAAGJgMuXAQ")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","Digital_Rename_Bot")     
    DB_URL = os.environ.get("DB_URL","mongodb+srv://Kakashi:aloksingh@kakashi.hnjnbw0.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://graph.org/file/507c658ba287e8d0206db.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1977715968').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002149498453"))

    #force subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "Anity_managementbots")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # part of text configuration
    START_TXT = """<b>Ｈ𝙰𝙸, {}👋

𝚃ʜɪs 𝙸s 𝙰ɴ 𝙰ᴅᴠᴀᴄᴇᴅ 𝙰ɴᴅ 𝚈ᴇᴛ 𝙿ᴏᴡᴇʀғᴜʟ 𝚁ᴇɴᴀᴍᴇ 𝙱ᴏᴛ
𝚄sɪɴɢ 𝚃ʜɪs 𝙱ᴏᴛ 𝚈ᴏᴜ 𝙲ᴀɴ 𝚁ᴇɴᴀᴍᴇ & 𝙲ʜᴀɴɢᴇ 𝚃ʜᴜᴍʙɴᴀɪʟ 𝙾ғ 𝚈ᴏᴜʀ 𝙵ɪʟᴇ 
𝚈ᴏᴜ 𝙲ᴀɴ 𝙰ʟsᴏ 𝙲ᴏɴᴠᴇʀᴛ 𝚅ɪᴅᴇᴏ 𝚃ᴏ 𝙵ɪʟᴇ & 𝙵ɪʟᴇ 𝚃ᴏ 𝚅ɪᴅᴇᴏ
𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙰𝙻𝚂𝙾 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝙰𝙽𝙳 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽

Tʜɪs Bᴏᴛ Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ : @Beesmileee 💞</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/Anity_managementbots>Anity Botz</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://github.com/SmileBotz>wanttobuy</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📊 ᴠᴇʀsɪᴏɴ: <a href=https://github.com/SmileBotz/Smile-Rename-Bot>3.𝟶.𝟶</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
<b>•></b> /start Tʜᴇ Bᴏᴛ.

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Anity_botsupport>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

    UPGRADE= """
•⪼ ★𝘗𝘭𝘢𝘯𝘴     -    ⏳𝘋𝘢𝘵𝘦 -  💸𝘗𝘳𝘪𝘤𝘦 
•⪼ 🥉𝘉𝘳𝘰𝘯𝘻𝘦   -     3𝘥𝘢𝘺𝘴 -    39
•⪼ 🥈𝘚𝘪𝘭𝘷𝘦𝘳    -     7𝘥𝘢𝘺𝘴 -    59
•⪼ 🥇𝘎𝘰𝘭𝘥     -    15𝘥𝘢𝘺𝘴 -   99
•⪼ 🏆𝘗𝘭𝘢𝘵𝘪𝘯𝘶𝘮  -    1𝘮𝘰𝘯𝘵𝘩 -   179
•⪼ 💎𝘋𝘪𝘢𝘮𝘰𝘯𝘥  -    2𝘮𝘰𝘯𝘵𝘩 -   319

- 𝘋𝘢𝘪𝘭𝘺 𝘜𝘱𝘭𝘰𝘢𝘥 𝘓𝘪𝘮𝘪𝘵 𝘜𝘯𝘭𝘪𝘮𝘪𝘵𝘦𝘥
- 𝘋𝘪𝘴𝘤𝘰𝘶𝘯𝘵 𝘈𝘭𝘭 𝘗𝘭𝘢𝘯 𝘙𝘴.9
    """
    THUMBNAIL = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>

<b>•></b> Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
"""
    CAPTION= """
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

Exᴀᴍᴩʟᴇ:- `/set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`
"""
    BOT_STATUS = """
⚡️ ʙᴏᴛ sᴛᴀᴛᴜs ⚡️

⌚️ ʙᴏᴛ ᴜᴩᴛɪᴍᴇ: `{}`
👭 ᴛᴏᴛᴀʟ ᴜsᴇʀꜱ: `{}`
💸 ᴛᴏᴛᴀʟ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: `{}`
֍ ᴜᴘʟᴏᴀᴅ: `{}`
⊙ ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
"""
    LIVE_STATUS = """
⚡ ʟɪᴠᴇ sᴇʀᴠᴇʀ sᴛᴀᴛᴜs ⚡

ᴜᴘᴛɪᴍᴇ: `{}`
ᴄᴘᴜ: `{}%`
ʀᴀᴍ: `{}%` 
ᴛᴏᴛᴀʟ ᴅɪsᴋ: `{}`
ᴜsᴇᴅ sᴘᴀᴄᴇ: `{} {}%`
ғʀᴇᴇ sᴘᴀᴄᴇ: `{}`
ᴜᴘʟᴏᴀᴅ: `{}`
ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
V𝟹.𝟶.𝟶 [STABLE]
"""
    DIGITAL_METADATA = """
❪ SET CUSTOM METADATA ❫

- /metadata - Tᴏ Sᴇᴛ & Cʜᴀɴɢᴇ ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @Beesmileee" -metadata author="@Anity_managementbots" -metadata:s:s title="Subtitled By :- @Beesmileee" -metadata:s:a title="By :- @Beesmileee" -metadata:s:v title="By:- @Anity_managementbots" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Anity_managementbots
"""
    
    CUSTOM_FILE_NAME = """
<u>🖋️ Custom File Name</u>

you can pre-add a prefix and suffix along with your new filename

➢ /set_prefix - To add a prefix along with your _filename.
➢ /see_prefix - Tᴏ Sᴇᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /del_prefix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /set_suffix - To add a suffix along with your filename_.
➢ /see_suffix - Tᴏ Sᴇᴇ Yᴏᴜʀ Sᴜғғɪx !!
➢ /del_suffix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Sᴜғғɪx !!

Exᴀᴍᴩʟᴇ:- `/set_suffix @Beesmileee`
Exᴀᴍᴩʟᴇ:- `/set_prefix @Beesmileee`
"""
    
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @Beesmileee🙏🥲
    # ᴡʜᴏᴇᴠᴇʀ ɪs ᴅᴇᴘʟᴏʏɪɴɢ ᴛʜɪs ʀᴇᴘᴏ ɪs ᴡᴀʀɴᴇᴅ ⚠️ ᴅᴏ ɴᴏᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛs ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʀᴇᴘᴏ #ғɪʀsᴛ ᴀɴᴅ ʟᴀsᴛ ᴡᴀʀɴɪɴɢ ⚠️
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
    
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://github.com/SmileBotz/Smile-Rename-Bot>WanttobuyDmOwner</a>

• ❣️ <a href=https://t.me/Anity_managementbots>SmileDeveloper</a>
• ❣️ <a href=https://t.me/Beesmileee>SmileBotz</a>
• ❣️ <a href=https://t.me/Beemsmileee>Wanttobuyrepoorpremium</a> """
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @Beesmileee" -metadata author="@Anity_managementbots" -metadata:s:s title="Subtitled By :- @Beesmileee" -metadata:s:a title="By :- @Beesmileee" -metadata:s:v title="By:- @Anity_managementbots" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Anity_managementbots
"""
    
    Smile_PROGRESS = """<b>\n
╭━━━━❰Anity PROCESSING...❱━➣
┣⪼ 🗃️ ꜱɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ ᴅᴏɴᴇ : {0}%
┣⪼ 🚀 ꜱᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
