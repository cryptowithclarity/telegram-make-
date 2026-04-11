import asyncio
from telethon import TelegramClient, events

api_id = 20561431
api_hash = "885596e5b35a77727fd5ffa10f718113

source_channel = "odes_ai"
target_group = -1003831506066

client = TelegramClient('session', api_id, api_hash)

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

        if msg.voice or msg.video:
            return

        text = msg.message or msg.caption or ""
        if not text:
            return

        if "http" in text.lower():
            return

        if any(x in text.lower() for x in ["follow", "subscribe", "join"]):
            return

        final_caption = text + FOOTER

        # 🔥 HANDLE MEDIA SAFELY
        if msg.photo:
            await client.send_file(
                target_group,
                msg.photo,
                caption=final_caption
            )

        elif msg.document:
            # Only send images (skip PDFs etc)
            if msg.document.mime_type and "image" in msg.document.mime_type:
                await client.send_file(
                    target_group,
                    msg.document,
                    caption=final_caption
                )
            else:
                return

        else:
            await client.send_message(target_group, final_caption)

        print("✅ Sent")

        await asyncio.sleep(3)  # ⚠️ Prevent rate issues

    except Exception as e:
        print("❌ Error:", e)
        await asyncio.sleep(5)  # ⚠️ Prevent crash loop


async def main():
    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Session not authorized")
        return

    print("🚀 Running...")
    await client.run_until_disconnected()


asyncio.run(main())
