import asyncio
from telethon import TelegramClient, events

api_id = 20561431
api_hash = '885596e5b35a77727fd5ffa10f718113'

source_channels = ['odes_ai']
target_group = -1003831506066  # ✅ FIXED (no quotes)

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    from telethon import TelegramClient

api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"

client = TelegramClient('session', api_id, api_hash)

import asyncio
from telethon import TelegramClient

api_id = 20561431
api_hash = "885596e5b35a77727fd5ffa10f718113"

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.connect()
    print("🚀 Bot running...")

    await client.run_until_disconnected()

asyncio.run(main())

import asyncio
asyncio.run(main())


async def print_dialogs():
    dialogs = await client.get_dialogs()
    print("\n📌 YOUR TELEGRAM DIALOGS:\n")
    for d in dialogs:
        print(f"Name: {d.name} | ID: {d.id}")
    print("\n👉 Copy your group ID from above\n")


@client.on(events.NewMessage(chats=source_channels))
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

        # ✅ SEND MESSAGE PROPERLY
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

        await asyncio.sleep(2)

    except Exception as e:
        print("❌ Error:", e)


async def main():
    await client.start()
    print("🚀 Telethon Running...\n")

    # optional (can remove later)
    await print_dialogs()

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
