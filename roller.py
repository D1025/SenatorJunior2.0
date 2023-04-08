import random
import time
import hikari
import colors
import miru

class roller():
    def __init__(self, author, dices, diceType, target, auto) -> None:
        self.author = author
        self.dices = dices
        self.diceType = diceType
        self.target = target
        self.auto = auto
    
    
    def roll(self):
        if self.diceType == "exalted":
            roll = self.exalted(10)
        elif self.diceType == "exalted-damage":
            roll = self.exalted(11)
            
        
        return roll
    
    def exalted(self, double):
        self.listOfThrows = []
        self.successes = 0
        
        for i in range (self.dices):
            self.listOfThrows.append(random.randint(1, 10))
            
        for dice in self.listOfThrows:
            if dice >= self.target:
                self.successes+=1
            if dice >= double:
                self.successes+=1
        self.successes+=self.auto
            
        title = (str(self.successes)+" SUCCESSES")
        desc = "[" + str(self.dices) + "]: " + self.exaltedDesc()
        return (hikari.Embed(title=title, description=desc, color=random.choice(colors.colors_list))
                .set_footer(" ".join([str(self.author), "●",str(time.strftime("%H:%M"))])))
    
    
    def exaltedDesc(self):
        desc = ""
        for i in range(len(self.listOfThrows)):
            if self.listOfThrows[i] == 10:
                desc+= "__**"+str(self.listOfThrows[i])+"**__"
            elif self.listOfThrows[i] >= 7:
                desc+= "**"+str(self.listOfThrows[i])+"**"
            else:
                desc+= str(self.listOfThrows[i])
                
            if i!=len(self.listOfThrows)-1:
                desc += ", "
                
        if self.auto > 0:
            desc+= " with __**" + str(self.auto) + "**__ automatic success"
        return desc
                


class ButtonViewRoller(miru.View):
    def __init__(self, NRoller,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.Roll = NRoller
    @miru.button(label="Re-Roll")
    async def btn_punkty(self, button: miru.Button, ctx:miru.Context):
        await ctx.respond(embed=self.Roll.roll())
            
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        await self.message.edit(components=[])
        self.Roll=None
        self.stop()

            
            
def kultroller(ctx, bonus:int):
    roll = list.append(random.randint(1,10))
    roll = list.append(random.randint(1,10))
    suma = sum(roll)+bonus
    embed = hikari.Embed(title=ctx.author, description=f"you rolled **{roll[0]}, {roll[1]}** + {bonus} = **{suma}**",
                         color=random.choice(colors.colors_list))
    if suma>=15:
        embed.add_field(name="SCORE", value="You have succeeded.")
    elif suma>=10:
        embed.add_field(name="SCORE", value="It didn't turn out exactly as you wanted.")
    else:
        embed.add_field(name="SCORE", value="You have failed.")
    return (embed.set_footer(" ".join([str(ctx.author), "●",str(time.strftime("%H:%M"))])))
        
        
        