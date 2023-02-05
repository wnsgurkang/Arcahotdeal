import requests
from bs4 import BeautifulSoup
import textwrap
import discord
from PIL import Image, ImageDraw, ImageFont
import io

# namu.wiki text extraction
def get_namu_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select_one('div[class=wiki-body]').get_text(strip=True)
    return content

# text to image conversion
def text_to_image(text):
    MAX_W, MAX_H = 1000, 1000
    font = ImageFont.truetype('NanumGothic.ttf', 30)
    lines = textwrap.wrap(text, width=30)
    w, h = font.getsize(max(lines, key=len))
    w *= 30
    h *= len(lines) / 30 + 1
    w = min(w, MAX_W)
    h = min(h, MAX_H)
    image = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    y_text = 0
    for line in lines:
        width, height = font.getsize(line)
        draw.text((0, y_text), line, font=font, fill=(0, 0, 0))
        y_text += height
    return image

# sending image to discord
async def send_discord_image(image, channel_id):
    client = discord.Client()
    await client.login('INSERT DISCORD BOT TOKEN HERE')
    channel = client.get_channel(channel_id)
    image_byte_array = io.BytesIO()
    image.save(image_byte_array, format='PNG')
    image_byte_array.seek(0)
    file = discord.File(fp=image_byte_array, filename='text_to_image.png')
    message = await channel.send(file=file)
    return message.attachments[0].url

# slash command that combines all the above codes
@client.command()
async def text_to_image(ctx, url: str):
    text = get_namu_text(url)
    image = text_to_image(text)
    image_link = await send_discord_image(image, CHANNEL_ID)
    await ctx.send(image_link)

client.run('INSERT DISCORD BOT TOKEN HERE')