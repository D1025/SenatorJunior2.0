import os
import time
import hikari
import lightbulb
import miru
import dungeon
import roller
import feedback.feedback as f

bot = lightbulb.BotApp(token=os.environ["TOKEN"])
miru.install(bot)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    dungeon.BuffFromJson()
    print("Bot has started!")
    
    
    
@bot.command
@lightbulb.command('dnd', 'Dungeons and Dragons 5e')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def dnd(ctx):
    pass
    
    

@dnd.child
@lightbulb.option('intelligence',
                  "Do you want turn off intelligence stats?",
                  type=str,
                  required=False,
                  choices=["Turn off", "Autistic"],
                  default="No")
@lightbulb.command('make', 'Makes random character for dnd 5e')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def make(ctx):
    Character = dungeon.DungeonsAndDragons().normal(inteligence=ctx.options.intelligence, author=ctx.author.id)
    dungeonView = dungeon.ButtonViewDungeon(NDungeon=Character, timeout=120)
    name = "".join(["Arts/Stats/",str(ctx.author.id), ".png"])
    message = await ctx.respond(Character.ReturnEmbed(ctx,name), components=dungeonView.build())
    await dungeonView.start(message)
    time.sleep(0.5)
    os.remove(name)
    
    
@dnd.child
@lightbulb.command('show-all', 'shows all characters you made')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def show(ctx):
    pointsView = dungeon.ButtonViewPages(1, timeout=120)
    message = await ctx.respond(dungeon.ShowAll(ctx, 1), components = pointsView.build())
    await pointsView.start(message)
    


@dnd.child
@lightbulb.option('id', 'character number - you can check character list using /dnd show', type=int, required=True)
@lightbulb.command('show', 'shows the full character based on id')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def nime(ctx):
    if dungeon.Check(author=ctx.author.id, id=ctx.options.id):
        Character = dungeon.DungeonsAndDragons().from_file(author=ctx.author.id, id=ctx.options.id)
        dungeonView = dungeon.ButtonViewDungeon(NDungeon=Character, timeout=120)
        name = "".join(["Arts/Stats/",str(ctx.author.id), ".png"])
        message = await ctx.respond(Character.ReturnEmbed(ctx,name), components=dungeonView.build())
        await dungeonView.start(message)
        time.sleep(0.5)
        os.remove(name)
    else:
        await ctx.respond("Wrong id")

@dnd.child
@lightbulb.option('id', 'character number - you can check character list using /dnd show', type=int, required=True)
@lightbulb.command('delete', 'delete character... why?')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def com_delete(ctx):
    if dungeon.deleteFromJson(ctx.author.id, ctx.options.id):
        await ctx.respond("Deleted... You cannot get it back!")
    else:
        await ctx.respond("Wrong id")
    
@bot.command
@lightbulb.option('dices', 'how much dices?', type=int,required=True)
@lightbulb.option('type', 'choose your style of rolling', type=str, required=False, choices=["exalted",  "exalted-damage"], default="exalted")
@lightbulb.option('automatic', 'auto successes added to exalted roller', type=int, required=False, default=0)
@lightbulb.command('roll', 'LETS ROLL!')
@lightbulb.implements(lightbulb.SlashCommand)
async def roll(ctx):
    roll = roller.roller(ctx.author, ctx.options.dices, ctx.options.type, 7, ctx.options.automatic)
    rollView = roller.ButtonViewRoller(roll, timeout=30)
    message = await ctx.respond(roll.roll(), components=rollView.build())
    await rollView.start(message)
    


@bot.command
@lightbulb.option('text', 'enter here your feedback', type=str, required=True)
@lightbulb.command('feedback', 'send your feedback')
@lightbulb.implements(lightbulb.SlashCommand)
async def feedback(ctx):
    f.feedback(ctx, ctx.options.text)
    await ctx.respond("Thank you for your feedback")
    time.sleep(1)
    await ctx.delete_last_response()
    await bot.rest.create_message("1063804680263712768", "".join([str(ctx.author), " - ",ctx.options.text]))
   
    
time.sleep(0.1)
bot.run(status=hikari.Status.ONLINE, activity=hikari.Activity(name="version 2.0 baby", type=hikari.ActivityType.PLAYING, url="https://discord.com/api/oauth2/authorize?client_id=818488309353283624&permissions=414464728128&scope=bot"))