import discord
from discord.ext import commands
import asyncio
import os

# تعريف البوت كحساب شخصي (self_bot=True)
bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول بنجاح كحساب شخصي: {bot.user}')

# أمر لعرض الأوامر
@bot.command()
async def اوامر(ctx):
    await ctx.send("قائمة الأوامر:\n!start_spam [الرسالة] - لبدء السبام\n!stop_spam - لإيقاف السبام\n!اوامر - لعرض القائمة")

# أمر لبدء السبام
@bot.command()
async def start_spam(ctx, *, message: str):
    await ctx.send("بدء السبام...")
    bot.spamming = True
    while bot.spamming:
        await ctx.send(message)
        await asyncio.sleep(0.5) 

# أمر لإيقاف السبام
@bot.command()
async def stop_spam(ctx):
    bot.spamming = False
    await ctx.send("تم إيقاف السبام.")

# تشغيل البوت
bot.run(os.getenv('TOKEN'))
