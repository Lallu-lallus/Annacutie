class script(object):
    START_TXT = """đˇđ´đģđž {},
đŧđĸ đđđđ , <a href='https://t.me/Dqautofl_bot'>đđđđ đđđ</a>, đ¸đ'đ đđđđĸ đđđđĸ đđđđ đđđ đđ đđ đĸđđđ đđđđđ đđđ đđđđ đđ đđđđđ, đđđđđ đđđ đ¸'đđ đđđđđđđ đđđđđđ đđđđđ đ¤
"""
    HELP_TXT = """đˇđ´đ {}
đđĻđŗđĻ đđ´ đđŠđĻ đđĻđ­đą đđ°đŗ đđē đđ°đŽđŽđĸđ¯đĨđ´."""
    ABOUT_TXT = """
đ§đđđĻ đđĄđĄđ đđđĄ'đĻ đđđĸđ¨đ§ đ đĻđ
âĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩ
ââââââ° ęĒáĨęĒŽęĒđŊ ęĒđ´á§ âąâââąâÛĒÛĒ
ââ­ââââââââââââââââŖ 
ââŖâĒŧ đđ đđŧđđ - <a href="https://t.me/Dqautofl_Bot"> đ¨đĩđĩđ¨ đŠđŦđĩ </a>
ââŖâĒŧ âšī¸âēī¸âī¸1 - <a href="https://t.me/pro_editor_tg"> đī¸đī¸đī¸đī¸đ¤ī¸áĩáĩ </a>
ââŖâĒŧ âšī¸âēī¸âī¸2 - <a href="https://t.me/PANDITHAN_SIR"> â¸ę ę ę ę ę ę ę ę ę ę ę ę ę ę ę ę ę ę ę M-STER </a>
ââŖâĒŧ đđ˛đĢđģđĒđģđģđ - đŋđđđžđļđđ°đŧ
ââŖâĒŧ đđĒđˇđ°đžđĒđ°đŽ - đŋđđđˇđžđŊ đš
ââŖâĒŧ đđĒđŊđĒ đđĒđŧđŽ - đŧđžđŊđļđž đŗđą
ââŖâĒŧ đđ¸đŊ đŧđŽđģđŋđŽđģ -  đˇđ´đđžđēđ
ââŖâĒŧ đđžđ˛đĩđ­ đĸđŊđĒđŊđžđŧ - v1.0.1 [ đąđ´đđ° ]
ââ°ââââââââââââââââŖ âââââââââââââââââââââąâÛĒÛĒ"""
    SOURCE_TXT = """<b>NOTE:</b>
- đ° đđ  đ đđđđ đđđđđđ đđđđđđđ. 
- ÕOáááá´ áOáĒá´ - <a href="https://github.com/Lallu-lallus/AnnaBen_robot"> đđđđđ đđđĨđ </a>

đ đđĻđ§đđĨ:
<a href="https://t.me/team_annaben"> đģđŦđ¨đ´ đ¨đĩđĩđ¨ </a>"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>đ˛ NOTHING MUCH JUST SOME FUN THINGS</b>
tđđ đđđđ đŽđđ: 
đŖ. /dice - Roll The Dice 
đ¤. /Throw đđ /Dart - đŗđ đŦđēđđž Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. đ¨đđđ đđđ đđđđđđ đđđđ đđđđđ đđđđđđđđđđ.
2. đļđđđ đđđđđđ đđđ đđđ đđđđđđđ đđ đ đđđđ.
3. đ¨đđđđ đđđđđđđ đđđđ đ đđđđđ đđ 64 đđđđđđđđđđ.

<b>Commands and Usage:</b>
âĸ /filter - <code>add a filter in chat</code>
âĸ /filters - <code>list all the filters of a chat</code>
âĸ /del - <code>delete a specific filter in chat</code>
âĸ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Anna ben Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ANNA BEN supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âĸ /connect  - <code>connect a particular chat to your PM</code>
âĸ /disconnect  - <code>disconnect from a chat</code>
âĸ /connections - <code>list all your connections</code>"""
    IMBD_TXT ="""<b>NOTE:</b>

âĸ /imdb  - <code>get the film information from IMDb source.</code>
âĸ /search  - <code>get the film information from various sources.</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of anna ben

<b>Commands and Usage:</b>
âĸ /id - <code>get id of a specifed user.</code>
âĸ /info  - <code>get information about a user.</code>
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĸ /logs - <code>to get the rescent errors</code>
âĸ /stats - <code>to get status of files in db.</code>
âĸ /users - <code>to get list of my users and ids.</code>
âĸ /chats - <code>to get list of the my chats and ids </code>
âĸ /leave  - <code>to leave from a chat.</code>
âĸ /disable  -  <code>do disable a chat.</code>
âĸ /ban  - <code>to ban a user.</code>
âĸ /unban  - <code>to unban a user.</code>
âĸ /channel - <code>to get list of total connected channels</code>
âĸ /broadcast - <code>to broadcast a message to all users</code>"""
    FILTER_TXT = """đđđđđđ đ đđđđđđ đđđđ đđđđđ
â đđđđ đ°đĸđ­đĄ @team_annaben"""
    STATUS_TXT = """âĒ đģđđđđ đđđđđ: <code>{}</code>
âĒ đģđđđđ đŧđđđđ: <code>{}</code>
âĒ đģđđđđ đĒđđđđ: <code>{}</code>
âĒ đŧđđđ đēđđđđđđ: <code>{}</code> đŧđđą
âĒ đ­đđđ đēđđđđđđ: <code>{}</code> đŧđđą"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
