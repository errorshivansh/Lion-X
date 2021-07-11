from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

Lion_pic = Config.ALIVE_PIC or "https://telegra.ph/file/8fcbf4621cd6c9dc46897.jpg"
alive_c = f"__**🔥🔥ʟɨօռ-Ӽ ɨs օռʟɨռɛ🔥🔥**__\n\n"
alive_c += f"__↼ Øwñêr ⇀__ : 『 {Lion_mention} 』\n\n"
alive_c += f"•♦• Telethon     :  `{tel_ver}` \n"
alive_c += f"•♦• ʟɨօռ-Ӽ       :  __**{Lion_ver}**__\n"
alive_c += f"•♦• Sudo            :  `{is_sudo}`\n"
alive_c += f"•♦• Channel      :  {Lion_channel}\n"

#-------------------------------------------------------------------------------

@bot.on(Lion_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(Lion):
    if Lion.fwd_from:
        return
    await Lion.get_chat()
    await Lion.delete()
    await bot.send_file(Lion.chat_id, Lion_pic, caption=alive_c)
    await Lion.delete()

msg = f"""
**⚡ ʟɨօռ-Ӽ ιѕ σиℓιиє ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
**ʟɨօռ-Ӽ  :**  **{Lion_ver}**
**Uptime   :**  `{uptime}`
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(Lion_cmd(pattern="Lion$"))
@bot.on(sudo_cmd(pattern="Lion$", allow_sudo=True))
async def Lion_a(event):
    try:
        Lion = await bot.inline_query(botname, "alive")
        await Lion[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "Lion", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
