
import telebot, requests

TOKEN="8717882444:AAHC4CJWMHlV25xdN60ldp8XIc_0spLC5V0"
bot=telebot.TeleBot(TOKEN, parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(m):
    bot.reply_to(m,
"""<b>FF Multi Tool</b>

Commands:
/bio <uid> <pass> <bio text>
/emote <uid> <pass>
/add <target_uid> <jwt>""")

@bot.message_handler(commands=["bio"])
def bio(m):
    p=m.text.split(maxsplit=3)
    if len(p)<4:
        return bot.reply_to(m,"Usage:\n/bio uid pass bio")
    uid,pw,bio=p[1],p[2],p[3]
    url=f"https://ob54-asd-long-bio.vercel.app/bio?bio={requests.utils.quote(bio)}&uid={uid}&pass={pw}"
    try:
        r=requests.get(url,timeout=30)
        bot.reply_to(m,f"<pre>{r.text}</pre>")
    except Exception as e:
        bot.reply_to(m,str(e))

@bot.message_handler(commands=["emote"])
def emote(m):
    p=m.text.split()
    if len(p)!=3:
        return bot.reply_to(m,"Usage:\n/emote uid pass")
    uid,pw=p[1],p[2]
    url=f"https://mafu-token-converter-production.up.railway.app/mafu?emote_enquip&uid={uid}&password={pw}"
    try:
        r=requests.get(url,timeout=30)
        bot.reply_to(m,f"<pre>{r.text}</pre>")
    except Exception as e:
        bot.reply_to(m,str(e))

@bot.message_handler(commands=["add"])
def add(m):
    p=m.text.split(maxsplit=2)
    if len(p)<3:
        return bot.reply_to(m,"Usage:\n/add target_uid jwt")
    target,jwt=p[1],p[2]
    url=f"https://shinchan-fm.vercel.app/add?uid={target}&jwt={requests.utils.quote(jwt)}&region=bd"
    try:
        r=requests.get(url,timeout=30)
        bot.reply_to(m,f"<pre>{r.text}</pre>")
    except Exception as e:
        bot.reply_to(m,str(e))

bot.infinity_polling()
