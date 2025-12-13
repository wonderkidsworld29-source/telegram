import os
import asyncio
import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler


# ===========================
#  CONFIGURATION
# ===========================
TOKEN = "8573280925:AAHlT2QIZTvFbFyV4YgGR56cuz_-4ld-Yy4"
CHAT_ID = -1002659872445
BASE_PATH = "images"  # Images folder

# ===========================
#  MESSAGES & IMAGES
# ===========================
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
""",
        "photo1.jpg"
    ),
    (
        """🎉GET ₹500 FREE on 🚩🚩🚩‼️

Spin the Lucky Wheel and win exciting cash rewards instantly!

🎰 Feeling Lucky?
Join WR777 today and enjoy 1️⃣ Free Spin — win up to ₹500 on the spot!
Every spin gives you a chance to grab cash, coins, or bonus rewards!

🔥 How to Get Your Free ₹500:
1️⃣ Register on WR777
2️⃣ Use your FREE SPIN
3️⃣ Win cash instantly
4️⃣ Invite friends to earn more!

✅ Free Spin Rewards
✅ Up to ₹500 Free
✅ 100% Safe & Trusted
✅ Fast Deposit/Withdrawal
✅ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMraTJ7PS
""",
        "photo2.jpg"
    ),
    (
        """🏦 Bank Delay? Don’t Worry — WR777 Pays You! 💰

WR777 offers up to ₹399 compensation whenever your bank withdrawal is delayed.

💰 Compensation Chart (Based on delay & withdrawal amount):
🛡 ₹100–₹999 → ₹9 / ₹19 / ₹39
🛡 ₹1000–₹4999 → ₹19 / ₹39 / ₹99
🛡 ₹5000–₹50000 → ₹99 / ₹199 / ₹399

☄️ Fast Deposit & Withdrawal
🔒 100% Safe
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo3.jpg"
    ),
    (
        """💰 Get High Bonuses on Your First Deposit! 💰

Make your first deposit on WR777 and receive instant rewards up to ₹5777! 🎁

💰 Bonus Examples:
💱 Deposit ₹100 → Get ₹37
💱 Deposit ₹1000 → Get ₹177
💱 Deposit ₹5000 → Get ₹777
💱 Deposit ₹50000 → Get ₹5777 

✔️ Fast Deposit & Withdrawal 💥
✔️ 100% Safe & Trusted 🆒
✔️ 24/7 Online Support ⏰

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        "photo4.jpg"
    ),
    (
        """🔔 Free Bonus ₹188 — Just Share on Social Media! 🔔

📲 Share WR777 and get a free ₹188 bonus! ✅

⏰ How to Claim:
➡️ Share → Wait 2 hours → Contact Customer Service
➡️ You can claim once every day
➡️ Activity Time: 08:00 - 22:00

💎 100% Safe
🌟 Fast Deposit/Withdrawal
🕒 24/7 Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
    
        "photo5.jpg"
    ),
    (
        """🔔 Enjoy Bonus on Every Deposit! 💱

Deposit anytime on WR777 and get an instant extra bonus added to your balance — unlimited times!

💰 More deposits = more bonus
⚡️ Fast Deposit & Withdrawal
🔓 100% Safe & Trusted
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        "photo6.jpg"
    ),
    (
        """⭐⭐ Easy UPI Deposit Guide (WR777)

Follow these 4 simple steps to deposit quickly:
1️⃣ Screenshot the QR
2️⃣ Open PhonePe → Tap Scan
3️⃣ Select Upload QR → Choose your screenshot
4️⃣ Complete payment → Copy the UPI Ref No and submit

💯 100% Safe
💎 Fast Deposit/Withdrawal
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        "photo7.jpg"
    ),
    (
        """👑 Unlock Elite VIP Rewards at WR777! 👑

🎆 Level up your tier and enjoy weekly bonuses, upgrade rewards, and free daily withdrawals — up to ₹59,999 when you reach VIP!

✅ VIP Benefits Include:
➡️ Weekly Bonus up to ₹1,777
➡️ Level Upgrade Bonus up to ₹59,999
➡️ Free Withdrawals: 2–10 times daily
➡️ Exclusive Monday VIP Rewards

🔒 100% Safe
☄️ Fast Deposit/Withdrawal
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        "photo8.jpg"
    ),
    (
        """🔗 Invite Friends & Earn Up to ₹15,000/Month! ✨

Earn money daily just by sharing your WR777 invite link! 🎁

💸 Rewards:
🟠 You get ₹50 per invite
🟠 Your friend gets ₹20
🟠 Up to 10 invites/day = ₹500 daily

📌 How to Join:
1️⃣ Register on WR777 📲
2️⃣ Share your invite link 😀
3️⃣ Friend registers + deposits ₹100 🎉

Rewards credited instantly

🔒 💯 Safe | ⚡ Fast Withdrawal | ⏰ 24/7 Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        "photo9.jpg"
    ),
    (
        """🔗 Become an Agent & Start Earning with WR777! 💎

🔔 Build your own team and earn commissions from 3 levels of sub-agents — bigger network = bigger income!

💼 Commission Rates:
✅ LV1 Subordinates: 0.30% – 0.70%
✅ LV2 Subordinates: 0.15% – 0.25%
✅ LV3 Subordinates: 0.07% – 0.15%

➡️ Earn daily, weekly, monthly passive income with zero investment!

🔓 100% Safe
⚡️ Fast Deposit/Withdrawal
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        "photo10.jpg"
    ),
]

# ===========================
#  SCHEDULER FUNCTION
# ===========================
async def scheduler(app):
    last_run_date = None
    while True:
        now_time = datetime.datetime.now()
        now_str = now_time.strftime("%H:%M")
        today = now_time.date()

        # Run at 08:00 only once per day
        if now_str == "08:00" and last_run_date != today:
            print("🎉 Starting auto-schedule...")

            for idx, (text, photo) in enumerate(MESSAGES):
                photo_path = os.path.join(BASE_PATH, photo)

                try:
                    if os.path.exists(photo_path):
                        with open(photo_path, "rb") as f:
                            await app.bot.send_photo(
                                chat_id=CHAT_ID,
                                photo=f,
                                caption=text
                            )
                    else:
                        await app.bot.send_message(chat_id=CHAT_ID, text=text)

                    print(f"✔ Sent message {idx+1}")

                except Exception as e:
                    print("SEND ERROR:", e)

                if idx != len(MESSAGES) - 1:
                    await asyncio.sleep(60 * 30)  # 30 min gap between messages

            last_run_date = today
            print("🎉 Completed all 10 messages for today!")

        await asyncio.sleep(60)  # Check every 1 min

# ===========================
#  /start COMMAND
# ===========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot is running 24/7 on Render with schedule!")

# ===========================
#  MAIN BOT
# ===========================
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Run scheduler in background
    asyncio.create_task(scheduler(app))

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
