import os
import asyncio
import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8573280925:AAHlT2QIZTvFbFyV4YgGR56cuz_-4ld-Yy4"
CHAT_ID = -1002659872445

BASE_PATH = "images"

MESSAGES = [
    (
        """👍👍👍👍👍👍👍👍👍

👉 Win Up To ₹9999 Daily on WR777! 🎉

🌟 Spin the lucky wheel every day and win exciting cash rewards — up to ₹9999 in a single spin! 🌟

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo1.jpg"
    ),

    (
        """🎉GET ₹500 FREE on 🚩🚩🚩‼️

Spin the Lucky Wheel and win exciting cash rewards instantly!

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo2.jpg"
    ),

    (
        """🏦 Bank Delay? Don’t Worry — WR777 Pays You! 💰

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo3.jpg"
    ),

    (
        """💰 Get High Bonuses on Your First Deposit! 💰

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo4.jpg"
    ),

    (
        """🔔 Free Bonus ₹188 — Just Share on Social Media! 🔔

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo5.jpg"
    ),

    (
        """🔔 Enjoy Bonus on Every Deposit! 💱

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo6.jpg"
    ),

    (
        """⭐⭐ Easy UPI Deposit Guide (WR777)

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo7.jpg"
    ),

    (
        """👑 Unlock Elite VIP Rewards at WR777! 👑

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo8.jpg"
    ),

    (
        """🔗 Invite Friends & Earn Up to ₹15,000/Month! ✨

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo9.jpg"
    ),

    (
        """🔗 Become an Agent & Start Earning with WR777! 💎

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo10.jpg"
    ),
]


# ===========================
#  SCHEDULER LOOP
# ===========================
async def scheduler(app):
    while True:
        now = datetime.datetime.now().strftime("%H:%M")

        if now == "08:00":
            print("🎉 Starting auto-schedule...")

            for idx, (text, photo) in enumerate(MESSAGES):
                photo_path = os.path.join(BASE_PATH, photo)

                try:
                    if os.path.exists(photo_path):
                        await app.bot.send_photo(
                            chat_id=CHAT_ID,
                            photo=open(photo_path, "rb"),
                            caption=text
                        )
                    else:
                        await app.bot.send_message(chat_id=CHAT_ID, text=text)

                    print(f"✔ Sent message {idx+1}")

                except Exception as e:
                    print("SEND ERROR:", e)

                if idx != len(MESSAGES) - 1:
                    await asyncio.sleep(60 * 30)  # 30 min gap

            print("🎉 Completed all 10 messages for today!")
            await asyncio.sleep(3600)

        await asyncio.sleep(20)


# ===========================
#   /start COMMAND
# ===========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot is running 24/7 on Render with schedule!")


# ===========================
#   MAIN BOT APP
# ===========================
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    asyncio.create_task(scheduler(app))

    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())

