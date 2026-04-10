import asyncio
from telethon import TelegramClient, events

# 🔑 API DETAILS
api_id = 20561431
api_hash = "885596e5b35a77727fd5ffa10f718113"

# 📡 SOURCE CHANNEL (without @)
source_channel = "odes_ai"

# 🎯 TARGET GROUP (Make reads from here)
target_group = -1003831506066

# 🤖 TELETHON CLIENT
client = TelegramClient('session', api_id, api_hash)


# 🔥 BRANDING FOOTER
FOOTER = """

━━━━━━━━━━━━━━━
❌ X :- https://x.com/CryptoWSarvesh  
🚀 Instagram :- https://www.instagram.com/cryptowithsarvesh/  
❤️ YouTube :- https://www.youtube.com/@CryptoWithSarvesh_ind
"""


@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    try:
        msg = event.message
        print("📩 New message received")

        # ❌ Skip unwanted media
        if msg.voice or msg.video:
            return

        # 🧠 Extract text/caption
        text = msg.message or msg.caption or ""

        if not text:
            return

        # ❌ Filter unwanted content
        if "http" in text.lower():
            return

        if any(x in text.lower() for x in ["follow", "subscribe", "join"]):
            return

        # ✅ Add branding
        final_caption = text + FOOTER

        # ============================
        # ✅ IMAGE + TEXT (MAIN FIX)
        # ============================

        if msg.photo:
            # 📷 Send as PHOTO (Make compatible)
            await client.send_file(
                target_group,
                msg.photo,
                caption=final_caption
            )

        elif msg.document:
            # 📁 If image comes as file
            await client.send_file(
                target_group,
                msg.document,
                caption=final_caption
            )

        else:
            # 📝 Text only
            await client.send_message(
                target_group,
                final_caption
            )

        print("✅ Sent successfully (Image + Text + Branding)")

        await asyncio.sleep(2)

    except Exception as e:
        print("❌ Error:", e)


async def main():
    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Session not authorized")
        return

    print("✅ Session loaded successfully")
    print("🚀 Bot running...")

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
