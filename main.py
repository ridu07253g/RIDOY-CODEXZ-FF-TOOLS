import telebot
import requests
import os
from flask import Flask
from threading import Thread

TOKEN = "8717882444:AAHC4CJWMHlV25xdN60ldp8XIc_0spLC5V0"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ---------------- Flask ---------------- #

app = Flask(__name__)

@app.route("/")
def home():
    return "FF TOOLS BOT IS RUNNING ✅"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ---------------- START ---------------- #

@bot.message_handler(commands=["start"])
def start(m):
    bot.reply_to(
        m,
        """<b>🤖 FF TOOLS BOT</b>

Welcome! 👋

📖 Use /help to see all commands.
"""
    )

# ---------------- HELP ---------------- #

@bot.message_handler(commands=["help"])
def help_menu(m):
    bot.reply_to(
        m,
        """<b>📖 FF TOOLS BOT - HELP MENU</b>

🔵 <b>Change Bot Bio</b> 🛠️
<code>/bio &lt;uid&gt; &lt;pass&gt; &lt;bio text&gt;</code>

🔵 <b>Add Hi Emote In Bot Account</b> 👋
<code>/emote &lt;uid&gt; &lt;pass&gt;</code>

🔵 <b>Add Bot In Friend List</b> 🫂
<code>/add &lt;target_uid&gt; &lt;jwt&gt;</code>

━━━━━━━━━━━━━━━━━━
"""
    )

# ---------------- BIO ---------------- #

@bot.message_handler(commands=["bio"])
def bio(m):
    p = m.text.split(maxsplit=3)

    if len(p) < 4:
        return bot.reply_to(m, "Usage:\n/bio uid pass bio text")

    uid = p[1]
    pw = p[2]
    bio_text = p[3]

    url = f"https://ob54-asd-long-bio.vercel.app/bio?bio={requests.utils.quote(bio_text)}&uid={uid}&pass={pw}"

    try:
        msg = bot.reply_to(m, "⏳ Changing Bio...")

        r = requests.get(url, timeout=30)

        bot.edit_message_text(
            f"<b>✅ Result</b>\n\n<pre>{r.text}</pre>",
            m.chat.id,
            msg.message_id,
            parse_mode="HTML"
        )

    except Exception as e:
        bot.reply_to(m, str(e))

# ---------------- EMOTE ---------------- #

@bot.message_handler(commands=["emote"])
def emote(m):

    p = m.text.split()

    if len(p) != 3:
        return bot.reply_to(m, "Usage:\n/emote uid pass")

    uid = p[1]
    pw = p[2]

    url = f"https://mafu-token-converter-production.up.railway.app/mafu?emote_enquip&uid={uid}&password={pw}"

    try:

        msg = bot.reply_to(m, "⏳ Adding Emote...")

        r = requests.get(url, timeout=30)

        bot.edit_message_text(
            f"<b>✅ Result</b>\n\n<pre>{r.text}</pre>",
            m.chat.id,
            msg.message_id,
            parse_mode="HTML"
        )

    except Exception as e:

        bot.reply_to(m, str(e))

# ---------------- ADD ---------------- #

@bot.message_handler(commands=["add"])
def add(m):

    p = m.text.split(maxsplit=2)

    if len(p) < 3:
        return bot.reply_to(m, "Usage:\n/add target_uid jwt")

    target = p[1]
    jwt = p[2]

    url = f"https://shinchan-fm.vercel.app/add?uid={target}&jwt={requests.utils.quote(jwt)}&region=bd"

    try:

        msg = bot.reply_to(m, "⏳ Sending Request...")

        r = requests.get(url, timeout=30)

        bot.edit_message_text(
            f"<b>✅ Result</b>\n\n<pre>{r.text}</pre>",
            m.chat.id,
            msg.message_id,
            parse_mode="HTML"
        )

    except Exception as e:

        bot.reply_to(m, str(e))

# ---------------- RUN ---------------- #

Thread(target=run).start()

print("Bot Started...")

bot.infinity_polling(skip_pending=True)
