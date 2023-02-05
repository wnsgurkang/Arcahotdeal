import discord
import asyncio

client = discord.Client()

async def embed_task():
    await client.wait_until_ready()
    channel = client.get_channel(819719798345695235)

    while not client.is_closed():
        embed = discord.Embed(title="Example Embed", description="This is an example embed.")
        await channel.send(embed=embed)
        await asyncio.sleep(60)

async def main():
    await client.start()

if __name__ == '__main__':
    asyncio.run(main())

client.run('MTA3MDczMTE5MTY3NTc4MTE4MQ.GQTr6Q.mrUEyDmucOny6UJ4Qevifzn-uywdrEumO9WdaU')