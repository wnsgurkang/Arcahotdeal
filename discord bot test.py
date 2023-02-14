import discord
import asyncio

token_input = input("Enter your token: ")

print('your token is: ' + token_input)
print('is this correct? (y/n)')

token_confirm = input()

def token_confirm():
    if token_confirm == 'y':
        print('token confirmed')
    elif token_confirm == 'n':
        print('input token again')
        token_input = input("Enter your token: ")
    else:
        print('token not confirmed')
        exit()
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