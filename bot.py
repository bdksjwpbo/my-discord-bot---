import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# أمر لعرض الأوامر
@bot.command()
async def اوامر(ctx):
    embed = discord.Embed(title="قائمة أوامر البوت", color=discord.Color.blue())
    embed.add_field(name="!start_spam [الرسالة]", value="لبدء السبام", inline=False)
    embed.add_field(name="!stop_spam", value="لإيقاف السبام", inline=False)
    embed.add_field(name="!اوامر", value="لعرض هذه القائمة", inline=False)
    await ctx.send(embed=embed)

# أمر لبدء السبام
@bot.command()
@commands.has_permissions(administrator=True)
async def start_spam(ctx, *, message: str):
    await ctx.send("بدء السبام... (أرسل !stop_spam للإيقاف)")
    bot.spamming = True
    while bot.spamming:
        await ctx.send(message)
        await asyncio.sleep(0.5) 

# أمر لإيقاف السبام
@bot.command()
@commands.has_permissions(administrator=True)
async def stop_spam(ctx):
    bot.spamming = False
    await ctx.send("تم إيقاف السبام.")

# ملاحظة: لا تضع التوكن هنا، استخدم Variables في Railway
import os
bot.run(os.getenv('TOKEN'))
