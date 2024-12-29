import hikari
import lightbulb
import miru

class Gates():
    def __init__(self, playerOne, playerTwo, tactics) -> None:
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.gateA = 0
        self.gateB = 0
        self.gateC = 0
        self.rounds = 1
        self.playerInputOne = None
        self.playerInputTwo = None
        self.playerFightOne = None
        self.playerFightTwo = None
        self.actualRound = 1
        self.tactics = tactics
        
    def callGate(self, gate):
        GateString = ""
        if gate == 0:
            GateString += ":white_circle:"
        elif gate < 0:
            GateString += ":red_circle:"
            gate*=-1
        else:
            GateString += ":green_circle:"
        GateString+= str(gate)
        return GateString
    
    def playerInput(self, player, playerInput):
        # print(self.playerTwo.id==player.id)
        # print(self.playerTwo)
        # print(player)
        print(playerInput, player)
        if self.playerOne.id == player.id:
            self.playerInputOne = playerInput
        if self.playerTwo.id == player.id:
            self.playerInputTwo = playerInput
            
    def playerFInput(self, player, playerInput):
        # print(self.playerTwo.id==player.id)
        # print(self.playerTwo)
        # print(player)
        print(playerInput, player)
        if self.playerOne.id == player.id:
            self.playerFightOne = playerInput
        if self.playerTwo.id == player.id:
            self.playerFightTwo = playerInput
        
    def fight(self, gate, tacticOne, tacticTwo, warriorsOne, warriorsTwo, pointsOne, pointsTwo):
        print("===FIGHT===")
        print(gate, tacticOne, tacticTwo, warriorsOne, warriorsTwo, pointsOne, pointsTwo)
        points = gate
        if tacticOne == "S":
            if tacticTwo == "D":
                points-=self.tactics
            elif tacticTwo == "P":
                points+=self.tactics
        elif tacticOne == "D":
            if tacticTwo == "P":
                points-=self.tactics
            elif tacticTwo == "S":
                points+=self.tactics
        elif tacticOne == "P":
            if tacticTwo == "S":
                points-=self.tactics
            elif tacticTwo == "D":
                points+=self.tactics
        print("Points after tactics: ", points)
        points = -warriorsOne+warriorsTwo-pointsOne+pointsTwo
        if points == 0:
            return points
        if gate < 0:
            if points < 0:
                if points < -warriorsOne+gate:
                    points = -warriorsOne+gate
            elif points > 0:
                if points > warriorsTwo:
                    points = warriorsTwo
        else:
            if points < 0:
                if points < -warriorsOne:
                    points = -warriorsOne
            elif points > 0:
                if points > warriorsTwo+gate:
                    points = warriorsTwo+gate
        print("Points after fight: ", points)
        return points
    
    def returnActualGatesValue(self):
        if self.actualRound==1:
            return self.gateA
        elif self.actualRound==2:
            return self.gateB
        else:
            return self.gateC
        
    def setActualGatesValue(self, value):
        if self.actualRound==1:
            self.gateA = value
        elif self.actualRound==2:
            self.gateB = value
        else:
            self.gateC = value
    
    def addActualGatesValue(self, value):
        if self.actualRound==1:
            self.gateA += value
        elif self.actualRound==2:
            self.gateB += value
        else:
            self.gateC += value
            
    def ReturnWin(self):
        points = 0
        if self.gateA < 0:
            points-=1
        elif self.gateA > 0:
            points+=1
        if self.gateB < 0:
            points-=1
        elif self.gateB> 0:
            points+=1
        if self.gateC < 0:
            points-=1
        elif self.gateC > 0:
            points+=1
        if points < 0:
            return "Winner is " + str(self.playerOne)
        elif points > 0:
            return "Winner is "+ str(self.playerTwo)
        else:
            points=self.gateA+self.gateB+self.gateC
            if points < 0:
                return "Winner is " + str(self.playerOne)
            elif points > 0:
                return "Winner is " + str(self.playerTwo)
            else:
                return "Draw...."
            
                    
    def callBackEmbed(self):
        return (
    hikari.Embed(title=":red_circle:@"+str(self.playerOne)+" vs :green_circle:@"+str(self.playerTwo), description=" ")
    .add_field("Gate A", value=self.callGate(self.gateA),inline=True)
    .add_field("Gate B", value=self.callGate(self.gateB),inline=True)
    .add_field("Gate C", value=self.callGate(self.gateC),inline=True)
    .set_footer(("Runda " +str(self.rounds)))
    )
        
    
    def callbackFight(self):
        gatestring = ""
        gatename = "Gate "
        if self.actualRound==1:
            gatename+="A"
            if self.gateA == 0:
                gatestring +=":white_circle:" + str(self.gateA)
            elif self.gateA < 0:
                gatestring +=":red_circle:" + str(-self.gateA)
            else:
                gatestring +=":green_circle:" + str(self.gateA)
                
            string = (":red_circle:"+str(self.playerOne)+ " - " + str(self.playerInputOne[0]) +" :arrow_right: " 
                      + gatestring +
                      " :arrow_left: " + str(self.playerInputTwo[0])  + " - "+ str(self.playerTwo) + ":green_circle:")
        elif self.actualRound == 2:
            gatename+="B"
            if self.gateB == 0:
                gatestring +=":white_circle:" + str(self.gateB)
            elif self.gateB < 0:
                gatestring +=":red_circle:" + str(-self.gateB)
            else:
                gatestring +=":green_circle:" + str(self.gateB)
                
            string = (":red_circle:"+str(self.playerOne)+ " - " + str(self.playerInputOne[1]) +" :arrow_right: " 
                      + gatestring +
                      " :arrow_left: " + str(self.playerInputTwo[1])  + " - "+ str(self.playerTwo) + ":green_circle:")
        else:
            gatename+="C"
            if self.gateC == 0:
                gatestring +=":white_circle:" + str(self.gateC)
            elif self.gateC < 0:
                gatestring +=":red_circle:" + str(-self.gateC)
            else:
                gatestring +=":green_circle:" + str(self.gateC)
                
            string = (":red_circle:"+str(self.playerOne)+ " - " + str(self.playerInputOne[2]) +" :arrow_right: " 
                      + gatestring +
                      " :arrow_left: " + str(self.playerInputTwo[2]) + " - " + str(self.playerTwo) + ":green_circle:")
        return (    
    hikari.Embed(title=gatename, description=" ")
    .add_field("Fight", value=string,inline=True))
        
    def callbackSummary(self, tacticsOne, tacticsTwo):
        
        tacticsOne=checkTactics(tacticsOne)
        tacticsTwo=checkTactics(tacticsTwo)
        
        if self.returnActualGatesValue()==0:
            taken = "None"
        elif self.returnActualGatesValue()>0:
            taken = self.playerTwo
        else:
            taken = self.playerOne
            
        if self.actualRound==1:
            gate = "GATE A"
        elif self.actualRound==2:
            gate = "GATE B"
        else:
            gate = "GATE C"
        
        return (hikari.Embed(title=("SUMMARY "+gate), description="")
                .add_field((":red_circle: " + str(self.playerOne)), ("Tactic: "+tacticsOne), inline=True)
                .add_field((":green_circle: " + str(self.playerTwo)), ("Tactic: "+tacticsTwo), inline=True)
                .add_field("TAKEN", ("BY " + str(taken)), inline=True)
                .set_footer(("Runda " +str(self.rounds)))
                )
        
        
class ButtonViewGates(miru.View):
    def __init__(self, NGates,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.NewGates = NGates
    @miru.button(label="Insert")
    async def btn_punkty(self, button: miru.Button, ctx:miru.Context):
        if self.NewGates.rounds == 4:
            await self.message.edit(components=[])
            await ctx.respond(embed=(hikari.Embed(title=self.NewGates.ReturnWin())))
        else:
            modal = GateModal(NGates=self.NewGates, title="Rozdziel Wojownikow!")
            await ctx.respond_with_modal(modal)
            
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        await self.message.edit(components=[])
        self.NewGates=None
        self.stop()
        
class ButtonViewFightGates(miru.View):
    def __init__(self, NGates,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.NewGates = NGates
    @miru.button(label="Fight")
    async def btn_punkty(self, button: miru.Button, ctx:miru.Context):
        if self.NewGates.playerInputOne[self.NewGates.actualRound-1]==0 and not self.NewGates.returnActualGatesValue()<0:
            self.NewGates.addActualGatesValue(self.NewGates.playerInputTwo[self.NewGates.actualRound-1])
            self.NewGates.actualRound+=1
            if self.NewGates.actualRound==4:
                await self.message.edit(components=[])
                self.NewGates.actualRound=1
                self.NewGates.rounds+=1
                self.NewGates.playerInputOne = None
                self.NewGates.playerInputTwo = None
                view = ButtonViewGates(NGates=self.NewGates, timeout=600)
                message = await ctx.respond(self.NewGates.callBackEmbed(), components=view.build())
                await view.start(message)
            else:
                await ctx.edit_response(embed=self.NewGates.callbackFight())
        elif self.NewGates.playerInputTwo[self.NewGates.actualRound-1]==0 and not self.NewGates.returnActualGatesValue()>0:
            self.NewGates.addActualGatesValue(-self.NewGates.playerInputOne[self.NewGates.actualRound-1])
            self.NewGates.actualRound+=1
            if self.NewGates.actualRound==4:
                await self.message.edit(components=[])
                self.NewGates.actualRound=1
                self.NewGates.rounds+=1
                self.NewGates.playerInputOne = None
                self.NewGates.playerInputTwo = None
                view = ButtonViewGates(NGates=self.NewGates, timeout=600)
                message = await ctx.respond(self.NewGates.callBackEmbed(), components=view.build())
                await view.start(message)
            else:
                await ctx.edit_response(embed=self.NewGates.callbackFight())
        else:
            modal = GateFightModal(NGates=self.NewGates, title="Wynierz taktyke i walcz!")
            await ctx.respond_with_modal(modal)
            
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        await self.message.edit(components=[])
        self.NewGates=None
        self.stop()
        
        

        
class GateModal(miru.Modal):
    def __init__(self, NGates,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.NewGates = NGates
    GateA = miru.TextInput(label="Gate A", placeholder="Insert warriors value", required=True)
    GateB = miru.TextInput(label="Gate B", placeholder="Insert warriors value", required=True)
    GateC = miru.TextInput(label="Gate C", placeholder="Insert warriors value", required=True)
    

    async def callback(self, ctx: miru.ModalContext) -> None:
        self.NewGates.playerInput(ctx.author, [int(self.GateA.value), int(self.GateB.value), int(self.GateC.value)])
        print(self.NewGates.playerInputOne)
        print(self.NewGates.playerInputTwo)
        if self.NewGates.playerInputOne is None or self.NewGates.playerInputTwo is None:
            await ctx.edit_response(embed=self.NewGates.callBackEmbed())
        else:
            view = ButtonViewFightGates(NGates=self.NewGates, timeout=600)
            message = await ctx.respond(embed=self.NewGates.callbackFight(), components=view.build())
            await view.start(message)
            
            
class GateFightModal(miru.Modal):
    def __init__(self, NGates,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.NewGates = NGates
    taktyka = miru.TextInput(label="Litera taktyki", placeholder="P - partyzanka, S - szybka, D - dluga", required=True)
    sukcesy = miru.TextInput(label="Sukcesy na rzut", placeholder="wprowadz sukcesy", required=True)
    

    async def callback(self, ctx: miru.ModalContext) -> None:
        self.NewGates.playerFInput(ctx.author, [self.taktyka.value, int(self.sukcesy.value)])
        print([self.taktyka.value, int(self.sukcesy.value)], ctx.author)
        if self.NewGates.playerFightOne is None or self.NewGates.playerFightTwo is None:
            await ctx.edit_response(embed=self.NewGates.callbackFight())
        else:
            self.NewGates.setActualGatesValue(self.NewGates.fight(self.NewGates.returnActualGatesValue(), self.NewGates.playerFightOne[0], self.NewGates.playerFightTwo[0], self.NewGates.playerInputOne[self.NewGates.actualRound-1], self.NewGates.playerInputTwo[self.NewGates.actualRound-1], self.NewGates.playerFightOne[1], self.NewGates.playerFightTwo[1]))
            
            await ctx.edit_response(embed=self.NewGates.callbackSummary(self.NewGates.playerFightOne[0], self.NewGates.playerFightTwo[0]) ,components=[])
            
            self.NewGates.playerFightOne = None
            self.NewGates.playerFightTwo = None
            self.NewGates.actualRound+=1

            if self.NewGates.actualRound==4:
                self.NewGates.actualRound=1
                self.NewGates.rounds+=1
                self.NewGates.playerInputOne = None
                self.NewGates.playerInputTwo = None
                view = ButtonViewGates(NGates=self.NewGates, timeout=600)
                message = await ctx.respond(self.NewGates.callBackEmbed(), components=view.build())
                await view.start(message)
            else:
                view = ButtonViewFightGates(NGates=self.NewGates, timeout=600)
                message = await ctx.respond(embed=self.NewGates.callbackFight(), components=view.build())
                await view.start(message)
        
        
        


def checkTactics(tactics):
    if tactics == "P":
        return "Partyzanka"
    if tactics == "D":
        return "Dluga"
    if tactics == "S":
        return "Szybka"
    return "error Tactics"
 
        