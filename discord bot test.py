import discord
import asyncio

client = discord.Client()

#get token by using input
input_token = input("Enter your token: ")

print('token:',input_token)
#print that if this discord bot is running well

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    if message.content.startswith("!embedtest"):   
        await client.wait_until_ready()
        channel = client.get_channel(819719798345695235)

        while not client.is_closed():
            embed = discord.Embed(title="Example Embed", description="This is an example embed.")
            await channel.send(embed=embed)
            await asyncio.sleep(60)

client.run(input_token)