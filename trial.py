import asyncio
from telethon import TelegramClient, events

# 🔑 YOUR API DETAILS
api_id = 20561431
api_hash = "885596e5b35a77727fd5ffa10f718113"

# 📡 SOURCE CHANNEL (WITHOUT @)
source_channel = "odes_ai"

# 🎯 TARGET GROUP (PRIVATE GROUP ID FOR MAKE)
target_group = -1003831506066

# 🤖 CLIENT (must match your session file name: session.session)
client = TelegramClient('session', api_id, api_hash)


@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    try:
        msg = event.message

        print("📩 New message received")

        # ❌ Skip voice/video
        if msg.voice or msg.video:
            return

        # 🧠 Get text or caption
        text = msg.message or msg.caption or ""

        if not text:
            return

        # ❌ Skip unwanted content
        if "http" in text.lower():
            return

        if any(x in text.lower() for x in ["follow", "subscribe", "join"]):
            return

        # ✅ SEND MESSAGE (NOT FORWARD)
        if msg.media:
            await client.send_file(
                target_group,
                msg.media,
                caption=text
            )
        else:
            await client.send_message(
                target_group,
                text
            )

        print("✅ Sent to group")

        await asyncio.sleep(2)

    except Exception as e:
        print("❌ Error:", e)


async def main():
    await client.connect()

    # ✅ Check session
    if not await client.is_user_authorized():
        print("❌ Session not working")
        return

    print("✅ Session loaded successfully")
    print("🚀 Bot running...")

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
