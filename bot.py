import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        # used to determine if it sends the message to the channel or privately
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTExNDcwMzQxNzAyMjA5MTI3NQ.GD8utV.FrsKza-wNI2-rp3pq-VqCWjd5QSDYeD1RqtRKk'
    # client = discord.Client()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # if running do this
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    # used to response to user
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        # private messages, 1: ignores the first character
        if username[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)



    client.run(TOKEN)
