import asyncio
from telethon import TelegramClient, events

# 🔑 YOUR API DETAILS
api_id = 20561431
api_hash = "885596e5b35a77727fd5ffa10f718113"

# 📡 SOURCE CHANNEL
source_channel = "odes_ai"

# 🎯 TARGET GROUP
target_group = -1003831506066

client = TelegramClient('session', api_id, api_hash)


# 🔥 YOUR BRANDING FOOTER
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

        # ❌ Skip voice/video
        if msg.voice or msg.video:
            return

        # 🧠 Get text/caption
        text = msg.message or msg.caption or ""

        if not text:
            return

        # ❌ Filters
        if "http" in text.lower():
            return

        if any(x in text.lower() for x in ["follow", "subscribe", "join"]):
            return

        # ✅ Add branding footer
        final_caption = text + FOOTER

        # 🥇 BEST METHOD: Download → Send as DOCUMENT (No compression)
        if msg.media:
            file = await client.download_media(msg, file=bytes)

            await client.send_file(
                target_group,
                file,
                caption=final_caption,
                force_document=True  # 🔥 NO COMPRESSION
            )
        else:
            await client.send_message(
                target_group,
                final_caption
            )

        print("✅ Sent in HIGH QUALITY with branding")

        await asyncio.sleep(2)

    except Exception as e:
        print("❌ Error:", e)


async def main():
    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Session not working")
        return

    print("✅ Session loaded successfully")
    print("🚀 Bot running...")

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
