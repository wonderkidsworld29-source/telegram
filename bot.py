import os
import asyncio
import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# =========================
# CONFIG (ENV ONLY)
# =========================
TOKEN = os.getenv("TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
BASE_PATH = "images"

bot = None  # will be set in main()

# =========================
# ALL MESSAGES (NO SKIP)
# =========================
MESSAGES = [

(
"""👍👍👍👍👍👍👍👍👍

👉 Win Up To ₹9999 Daily on WR777! 🎉

🌟 Spin the lucky wheel every day and win exciting cash rewards — up to ₹9999 in a single spin! 🌟

✅ Daily chances 🎯
✅ Multiple prize levels 🎁
✅ Big rewards, instant wins 🪙

💎 Why everyone loves WR777:
✅ 100% Safe 🔓
✅ Fast Deposit/Withdrawal ⚡️
✅ 24/7 Online Support ⏰

🚩 Start spinning for BIG rewards! 💌

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""","photo1.jpg"),

(
"""🎉GET ₹500 FREE on 🚩🚩🚩‼️

Spin the Lucky Wheel and win exciting cash rewards instantly!

🎰 Feeling Lucky?
Join WR777 today and enjoy 1️⃣ Free Spin — win up to ₹500 on the spot!

🔥 How to Get Your Free ₹500:
1️⃣ Register
2️⃣ Use FREE SPIN
3️⃣ Win instantly
4️⃣ Invite friends

✅ Up to ₹500 Free
✅ 100% Safe
✅ Fast Withdrawal
✅ 24/7 Support

📱 Download link - https://invite.wr777.club/?code=UMraTJ7PS
""","photo2.jpg"),

(
"""🏦 Bank Delay? Don’t Worry — WR777 Pays You! 💰

Compensation up to ₹399 on withdrawal delay.

🛡 ₹100–₹999 → ₹9 / ₹19 / ₹39
🛡 ₹1000–₹4999 → ₹19 / ₹39 / ₹99
🛡 ₹5000–₹50000 → ₹99 / ₹199 / ₹399

🔒 Safe | ⚡ Fast | ⏰ 24/7 Support

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""","photo3.jpg"),

(
"""💰 Get High Bonuses on First Deposit!

💱 ₹100 → ₹37
💱 ₹1000 → ₹177
💱 ₹5000 → ₹777
💱 ₹50000 → ₹5777

✔️ Instant bonus
✔️ Fast withdrawal
✔️ 24/7 Support

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""","photo4.jpg"),

(
"""🔔 Free Bonus ₹188 — Just Share!

📲 Share → wait 2 hrs → contact support
⏰ Once per day (08:00–22:00)

💎 100% Safe
⚡ Fast Withdrawal

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""","photo5.jpg"),

(
"""🔔 Bonus on EVERY Deposit!

💰 Unlimited bonus
⚡ Fast deposit/withdrawal
🔓 100% Safe
⏰ 24/7 Support

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""","photo6.jpg"),

(
"""⭐⭐ Easy UPI Deposit Guide

1️⃣ Screenshot QR
2️⃣ PhonePe → Scan
3️⃣ Upload QR
4️⃣ Pay & submit UPI Ref

💯 Safe | ⚡ Fast | ⏰ 24/7

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""","photo7.jpg"),

(
"""👑 VIP Rewards Unlocked!

➡️ Weekly bonus ₹1,777
➡️ Upgrade bonus ₹59,999
➡️ Free withdrawals daily

🔒 Safe | ⚡ Fast | ⏰ 24/7

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""","photo8.jpg"),

(
"""🔗 Invite Friends & Earn ₹15,000/month!

🟠 ₹50 per invite
🟠 Friend gets ₹20
🟠 10 invites/day = ₹500

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""","photo9.jpg"),

(
"""🔗 Become an Agent & Earn Big!

LV1: 0.30%–0.70%
LV2: 0.15%–0.25%
LV3: 0.07%–0.15%

💰 Passive income
⚡ Fast payout
🔒 100% Safe

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""","photo10.jpg"),

]

# =========================
# AUTO SCHEDULER
# =========================
async def auto_scheduler():
    last_date = None
    while True:
        now = datetime.datetime.now()
        if now.strftime("%H:%M") == "08:00" and last_date != now.date():
            for text, photo in MESSAGES:
                try:
                    path = os.path.join(BASE_PATH, photo)
                    if os.path.exists(path):
                        with open(path, "rb") as img:
                            await bot.send_photo(chat_id=CHAT_ID, photo=img, caption=text)
                    else:
                        await bot.send_message(chat_id=CHAT_ID, text=text)
                    await asyncio.sleep(1800)  # 30 min gap
                except Exception as e:
                    print("SEND ERROR:", e)
            last_date = now.date()
        await asyncio.sleep(60)

# =========================
# COMMAND
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot running (Railway stable)")

# =========================
# MAIN
# =========================
async def main():
    global bot
    app = ApplicationBuilder().token(TOKEN).build()
    bot = app.bot

    app.add_handler(CommandHandler("start", start))
    asyncio.create_task(auto_scheduler())

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
