import discord
from discord.ext import commands
import asyncio
import os

# الحل: تعريف البوت بهذه الطريقة يمنع خطأ BotBase.__init__
bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول بنجاح كحساب شخصي: {bot.user}')

# أمر لعرض قائمة التعليمات
@bot.command()
async def اوامر(ctx):
    instructions = (
        "**قائمة أوامر البوت:**\n\n"
        "`!start_spam [الرسالة]` : لبدء عملية السبام بالرسالة التي تحددها.\n"
        "`!stop_spam` : لإيقاف عملية السبام فوراً.\n"
        "`!اوامر` : لعرض هذه القائمة."
    )
    await ctx.send(instructions)

# أمر لبدء السبام
@bot.command()
async def start_spam(ctx, *, message: str):
    await ctx.send("بدء السبام... (أرسل !stop_spam للإيقاف)")
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
