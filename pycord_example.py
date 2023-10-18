# 뇌절을 위해 discord.py가 아닌 pycord로 하겠습니다.
import discord
import sexyNy64
import tok
bot = discord.Bot()

@bot.event
async def on_ready():
    print("Ready!")

@bot.slash_command(name="미테테네")
async def random(ctx: discord.ApplicationContext, id:int) -> None:
    섹시 = sexyNy64()
    await ctx.respond(섹시.make(id), ephemeral=True)

@bot.slash_command(name="콘나가치데")
async def checkit(ctx: discord.ApplicationContext, id:int, word:str) -> None:
    섹시 = sexyNy64()
    res = 섹시.check(id=id, word=word)

    if res:
        await ctx.respond("론리 로리로리 카미 코-린")
    else:
        await ctx.respond("슈쿠세-!! 로리카미 레쿠이에무")


bot.run(tok.남냥뷴태)