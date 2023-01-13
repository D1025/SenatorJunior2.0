import os
import time
import hikari
import lightbulb
import miru
import gates as g
import race as r



bot = lightbulb.BotApp(token=os.environ["TOKEN"])
miru.install(bot)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Bot has started!")
    
    
@bot.command
@lightbulb.option("trudnosc", "Trudnosc trasy", type=int, required=True)
@lightbulb.command('race', 'Sprawdzmy sie w wyscigu')
@lightbulb.implements(lightbulb.SlashCommand)
async def race(ctx):
    NewEmbed = r.EmbedTournament(ctx.options.trudnosc)
    view = r.ButtonView(NEmbed=NewEmbed, timeout=3600)
    message = await ctx.respond(NewEmbed.callBackEmbed(), components=view.build())
    await view.start(message)
    
    
@bot.command
@lightbulb.option("enemy", "Z kim chcesz grac?", type=hikari.User, required=True)
@lightbulb.command("gates", "zagrajmy w bramy")
@lightbulb.implements(lightbulb.SlashCommand)
async def gates(ctx):
    gameGates = g.Gates(ctx.author, ctx.options.enemy)
    view = g.ButtonViewGates(NGates=gameGates, timeout=600)
    message = await ctx.respond(gameGates.callBackEmbed(), components=view.build())
    await view.start(message)
    
    
    
time.sleep(1)
bot.run(status=hikari.Status.DO_NOT_DISTURB, activity=hikari.Activity(name="DEVELOPMENT", type=hikari.ActivityType.PLAYING, url="https://discord.com/api/oauth2/authorize?client_id=1058750318181105674&permissions=543853770816&scope=bot"))