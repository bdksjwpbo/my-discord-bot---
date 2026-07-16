import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# أمر حذف جميع الرتب (عدا الرتبة الافتراضية)
@bot.command()
@commands.has_permissions(administrator=True)
async def delete_all_roles(ctx):
    await ctx.send("بدء حذف الرتب...")
    for role in ctx.guild.roles:
        # لا يمكن حذف رتبة @everyone أو رتبة البوت نفسه
        if role.name != "@everyone" and role != ctx.guild.me.top_role:
            try:
                await role.delete()
            except:
                continue
    await ctx.send("تم الانتهاء من حذف الرتب المتاحة.")

# أمر حذف جميع القنوات
@bot.command()
@commands.has_permissions(administrator=True)
async def delete_all_channels(ctx):
    await ctx.send("بدء حذف جميع القنوات...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            continue
