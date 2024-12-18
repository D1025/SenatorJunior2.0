import math
import hikari
import miru
import lightbulb


class TableOfPoints:
    def __init__(self, poziom) -> None:
        self.TableOfNames = []
        self.TableOfTrasa = []
        self.TableOfPunkt1 = []
        self.TableOfPunkt2 = []
        self.TableOfWytrz = []
        self.TableOfZwierzak = []
        self.PoziomTrudnosc = poziom
        self.Maks = 0
        self.Actual = 0
        self.Tab = 1
        self.Done = 0
    def AddNames(self, name, tableZwierzak):
        name+="\n"
        self.TableOfNames.append(name)
        self.TableOfTrasa.append(" ")
        self.TableOfPunkt1.append(" ")
        self.TableOfPunkt2.append(" ")
        self.TableOfWytrz.append(" ")
        self.TableOfZwierzak.append(tableZwierzak)
        self.Maks+=1
        
    def ShowNames(self):
        FullNames=""
        if not self.TableOfNames:
            return "Please insert name"
        for name in self.TableOfNames:
            FullNames+=name
        return FullNames
    
    def AddPoints(self, points):
        if self.Actual==self.Maks:
            if self.Tab == 4:
                return
            if not self.TableOfNames:
                return
            self.Tab+=1
            self.Actual=0
        if self.Tab == 1:
            temp = -self.PoziomTrudnosc+int(points)
            if temp < -3:
                temp = -3
            if temp > 3:
                temp = 3
            self.TableOfTrasa[self.Actual]=str(temp)
        if self.Tab == 2:
            cap = self.TableOfZwierzak[self.Actual][2]+math.ceil(self.TableOfZwierzak[self.Actual][1]/2)+int(self.TableOfTrasa[self.Actual])
            if int(points) > cap:
                points = cap 
            self.TableOfPunkt1[self.Actual]=str(points)
        if self.Tab == 3:
            self.TableOfWytrz[self.Actual]=points
        if self.Tab == 4:
            cap = self.TableOfZwierzak[self.Actual][2]+math.ceil(self.TableOfZwierzak[self.Actual][1]/2)+int(self.TableOfTrasa[self.Actual])
            if int(points) > cap:
                points = cap 
            self.TableOfPunkt2[self.Actual]=str(points)
        self.Actual+=1
    
    def ShowPoints(self):
        Full=""
        if not self.TableOfNames:
            return "/"
        if self.TableOfTrasa[0]==" ":
            return "/"
        for i in range(self.Maks):
            Full+="`"
            Full+=BialeZnaki(self.TableOfTrasa[i], 3)
            Full+=BialeZnaki(self.TableOfPunkt1[i], 6)
            Full+=BialeZnaki(self.TableOfWytrz[i], 4)
            Full+=BialeZnaki(self.TableOfPunkt2[i], 5)
            Full+="`\n"
        return Full
    
    def ShowWhoWinning(self):
        if not self.TableOfNames:
            return "/"
        table = []
        for i in range(len(self.TableOfNames)):
            punkty = 0 
            punkty += check(self.TableOfPunkt1[i])
            punkty += check(self.TableOfWytrz[i])
            punkty += check(self.TableOfPunkt2[i])
            table.append(punkty)
        maks = max(table)
        sorted_table = sorted(table, reverse=True)
        smaks = -1
        tmaks = -1
        if len(sorted_table) >1:
            smaks = sorted_table[1]
        if len(sorted_table) >2:
            tmaks = sorted_table[2]
        all = ""
        for i in table:
            all+=str(i)
            if i == maks:
                all+=":first_place:"
                maks=-1
            elif i == smaks:
                all+=":second_place:"
                smaks=-1
            elif i == tmaks:
                all+=":third_place:"
                tmaks=-1
            all+="\n"
                
        return all
    
    def End(self):
        if self.Tab==4 and self.Actual==self.Maks:
            return True
        return False
    
    def ShowNamesWin(self):
        table = []
        
        for i in range(len(self.TableOfNames)):
            punkty = 0 
            punkty += check(self.TableOfPunkt1[i])
            punkty += check(self.TableOfWytrz[i])
            punkty += check(self.TableOfPunkt2[i])
            table.append(punkty)
        zipped = zip(table, self.TableOfNames, self.TableOfZwierzak)
        sorted_zipped = sorted(zipped, key=lambda x: x[0], reverse=True)
        sorted_points, sorted_names, sorted_zwierzak = zip(*sorted_zipped)
        NAMES = ""
        max1, max2, max3 = find_maxes(sorted_points)
        for i in range(len(self.TableOfNames)):
            if sorted_points[i] == max1:
                NAMES+=":first_place:"
            if sorted_points[i] == max2:
                NAMES+=":second_place:"            
            if sorted_points[i] == max3:
                NAMES+=":third_place:"
            NAMES+=sorted_names[i]+ " with " + sorted_zwierzak[i][0] + " - " + str(sorted_points[i]) + "\n"
            
            
        return NAMES            

    def ReturnActualState(self):
        if self.Done == 0:
            return "Add some names!"
        Next = self.Actual
        NextTab = self.Tab
        if Next == self.Maks:
            if NextTab == 4:
                return "Click last time that button please"
            Next=0
            NextTab+=1
        FullText = "Wprowadz "
        if NextTab == 1:
            FullText+="sukcesy na wyznaczanie trasy dla "
        if NextTab == 2:
            FullText+="wynik trasy 1 dla "
        if NextTab == 3:
            FullText+="wynik wytrzymalosci dla "
        if NextTab == 4:
            FullText+="wynik trasy 2 dla "
        FullText+="`"+self.TableOfNames[Next]+"`"
        return FullText
            
        
            
            
            
        
def check(string):
    if string == " ":
        return 0
    return int(string)
                
def BialeZnaki(String, HowMuch):
    new = ""
    for i in range(HowMuch-len(String)):
        new+=" " #u1CBC
    new+=String
    return new

def CzyLiczba(string):
    liczby = ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in string:
        if i not in liczby:
            return False
    return True

def find_maxes(numbers):
    # Create a set to store the unique numbers in the list
    unique_numbers = set(numbers)
    print(unique_numbers)
    
    # Initialize variables to store the max values
    max1 = -1
    max2 = -1
    max3 = -1
    
    # Iterate over the unique numbers in the list
    for number in reversed(list(unique_numbers)):
      if max1<number:
        max1 = number
      elif max2<number:
        max2 = number
      elif max3<number:
        max3 = number
      
    
    # Return the max values
    return max1, max2, max3



class EmbedTournament:
    def __init__(self, poziom):
        self.title = "Tournament"
        self.description = ""
        self.Points = TableOfPoints(poziom)
    def callBackEmbed(self):
        return (
    hikari.Embed(title=self.title, description=self.description)
    .add_field("Name", value=self.Points.ShowNames(),inline=True)
    .add_field("Trasa/Rzut1/Wyt/Rzut2", value=self.Points.ShowPoints(),inline=True)
    .add_field("Who's Winning?", value=self.Points.ShowWhoWinning(),inline=True)
    .add_field(name="Next action:",value=self.Points.ReturnActualState())
    )
        
    def MakeWinningEmbed(self):
        return (
    hikari.Embed(title="WINNERS", description=self.description)
    .add_field("Partisipants:", value=self.Points.ShowNamesWin(),inline=True)
    .set_footer("Thanks for playing")
    )



class ButtonView(miru.View):
    def __init__(self, NEmbed,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.NewEmbed = NEmbed
    @miru.button(label="Dodaj uczestnika")
    async def btn_uczestnik(self, button: miru.Button, ctx:miru.Context):
        modal = NameModal(NEmbed=self.NewEmbed,title="Dodaj uczestnika")
        # await ctx.edit_response("You clicked me")
        # await modal.send(ctx.interaction)
        await ctx.respond_with_modal(modal)
    @miru.button(label="Done", style=hikari.ButtonStyle.DANGER)
    async def btn_done(self, button: miru.Button, ctx:miru.ViewContext):
        self.NewEmbed.Points.Done = 1
        view = ButtonView2(NEmbed=self.NewEmbed, timeout=3600)
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        self.stop()
        message = await ctx.edit_response(embed=self.NewEmbed.callBackEmbed() ,components=view.build())
        await view.start(message)
        
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        await self.message.edit(components=[])
        self.NewEmbed=None
        self.stop()
        


    
class ButtonView2(miru.View):
    def __init__(self, NEmbed,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.NewEmbed = NEmbed
    @miru.button(label="Punkty")
    async def btn_punkty(self, button: miru.Button, ctx:miru.Context):
        if self.NewEmbed.Points.End():
            for item in self.children:
                item.disabled = True # Disable all items attached to the view
            self.stop()
            await ctx.respond(self.NewEmbed.MakeWinningEmbed())
        else:
            modal = PunktModal(NEmbed=self.NewEmbed, title="Podaj punkty")
            await ctx.respond_with_modal(modal)
            
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        await self.message.edit(components=[])
        self.NewEmbed=None
        self.stop()
        

class NameModal(miru.Modal):
    def __init__(self, NEmbed,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.NewEmbed = NEmbed
    name = miru.TextInput(label="Name", placeholder="Type your name!", required=True)
    # ZwierzakName = miru.TextInput(label="Nazwa zwierzaka", placeholder="Nazwij go!", required=True)
    ZwierzakNazwa = miru.TextInput(label="Nazwa Zwierzaka", placeholder="Nazwij go!", required=True)
    ZwierzakSzybkosc = miru.TextInput(label="Szybkosc", placeholder="Ma byc wartosc liczbowa", required=True)
    ZwierzakManewrownosc = miru.TextInput(label="Manewrownosc", placeholder="Ma byc wartosc liczbowa", required=True)
    # ZwierzakWytrzymalosc = miru.TextInput(label="Wytrzymalosc", placeholder="Ma byc wartosc liczbowa", required=True)
    
    

    # bio = miru.TextInput(label="Biography", value="Pre-filled content!", style=hikari.TextInputStyle.PARAGRAPH)
    # The callback function is called after the user hits 'Submit'
    async def callback(self, ctx: miru.ModalContext) -> None:
        if not (CzyLiczba(self.ZwierzakSzybkosc.value) and CzyLiczba(self.ZwierzakManewrownosc.value)):
            return
        temp = [self.ZwierzakNazwa.value, int(self.ZwierzakSzybkosc.value), int(self.ZwierzakManewrownosc.value)]
        self.NewEmbed.Points.AddNames(self.name.value, temp)
        # Nembed.title=self.bio.value
        # You can also access the values using ctx.values, Modal.values, or use ctx.get_value_by_id()
        await ctx.edit_response(embed=self.NewEmbed.callBackEmbed())
        
class PunktModal(miru.Modal):
    def __init__(self, NEmbed,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.NewEmbed = NEmbed
        
    
    punkt = miru.TextInput(label="Punkty", placeholder="Dodaj punkty", required=True)
    

    # The callback function is called after the user hits 'Submit'
    async def callback(self, ctx: miru.ModalContext) -> None:
        if not CzyLiczba(self.punkt.value):
            return
        self.NewEmbed.Points.AddPoints(self.punkt.value)
        await ctx.edit_response(embed=self.NewEmbed.callBackEmbed())
