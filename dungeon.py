import json
import os
import random
import time
import paiting
import hikari
import miru
import colors



klasy_art = {'Artificer':"https://www.dndbeyond.com/avatars/13916/408/637411847943829485.jpeg",
             'Barbarian':"https://www.dndbeyond.com/avatars/10/0/636336416778392507.jpeg", 
             'Bard': "https://www.dndbeyond.com/avatars/10/1/636336416923635770.jpeg", 
             'Cleric':"https://www.dndbeyond.com/avatars/10/2/636336417054144618.jpeg", 
             'Druid':"https://www.dndbeyond.com/avatars/10/3/636336417152216156.jpeg", 
             'Fighter': "https://www.dndbeyond.com/avatars/10/4/636336417268495752.jpeg", 
             'Monk':"https://www.dndbeyond.com/avatars/10/5/636336417372349522.jpeg", 
             'Paladin': "https://www.dndbeyond.com/avatars/10/6/636336417477714942.jpeg", 
             'Ranger':"https://www.dndbeyond.com/avatars/10/7/636336417569697438.jpeg", 
             'Rogue':"https://www.dndbeyond.com/avatars/10/8/636336417681318097.jpeg", 
             'Sorcerer':"https://www.dndbeyond.com/avatars/10/9/636336417773983369.jpeg", 
             'Warlock': "https://www.dndbeyond.com/avatars/10/12/636336422983071263.jpeg", 
             'Wizard':"https://www.dndbeyond.com/avatars/10/11/636336418370446635.jpeg"}

# personality = []
race_list = []
class_dir = {}
new_traits = []
mele_names = []
femele_names = []
last_name = []



def BuffFromJson():
#   # PERSONALITY
#   global personality
#   pr = open("json/personality.json")
#   personality_result = json.load(pr)
#   for row in personality_result['results']:
#     name = row['name']
#     personality.append(name)
    
  # RACE 
  global race_list
  rr = open("json/newrases.json")
  race_result = json.load(rr)
  for row in race_result['results']:
    name = row['name']
    race_list.append(name)
    
  # CLASS / SUBCLASS
  global class_dir
  cr = open("json/clases.json")
  class_ressult = json.load(cr)
  for row in class_ressult['results']:
    name = row['name']
    subclass_list = []
    for nextrow in row['archetype']:
      s_name = nextrow['name']
      subclass_list.append(s_name)
    class_dir[name] = subclass_list

    # NEW PERSONALITY:
    global new_traits
    tr = open("json/traits.json")
    trait_resssult = json.load(tr)
    for row in trait_resssult['personality']:
        new_traits.append(row)
        
    #NAMES
    global mele_names, femele_names, last_name
    file = open('generator/femele.txt')
    femele_names = file.readlines()
    file.close()
    file = open('generator/male.txt')
    mele_names = file.readlines()
    file.close()
    file = open('generator/last.txt')
    last_name = file.readlines()
    file.close()
    
    


    # pr.close()
    rr.close()
    cr.close()
    tr.close()
    
def ShowAll(ctx, page):
    file = "".join(["json/data/", str(ctx.author.id), ".json"])
    if os.path.isfile(file):
        with open(file, 'r') as js:
            data = json.load(js)
        embed = (hikari.Embed(title="".join([str(ctx.author), " you have ", str(data['count']), " characters"]), description="", color=random.choice(colors.colors_list))
        .set_thumbnail("Arts/Logos/DnD.png")
        .set_footer(" ".join([str(ctx.author), "●",str(time.strftime("%H:%M"))])))
        i = 1
        for row in data['data']:
            if int(i/11)+1 != page:
                i+=1
                continue
            if i == (10*page)+1:
                break
            final = row['rasa'] + ", " + row['klasa'] + row['subclassa']
            embed.add_field("".join([str(i), " - " ,row['name']]), final)
            i+=1
        return embed
    else:
                return (
        hikari.Embed(title="You have 0 characters..", description="", color=random.choice(colors.colors_list))
        .set_thumbnail("Arts/Logos/DnD.png")
        .set_footer(" ".join([str(ctx.author), "●",str(time.strftime("%H:%M"))]))
    )
    
def deleteFromJson(author, id):
    file = "".join(["json/data/", str(author), ".json"])
    if os.path.isfile(file):
        with open(file, 'r') as js:
            data = json.load(js)
        
        newData = {
                'count':data['count']-1, 
                'data':[
                ]
                }
        i = 1
        for row in data['data']:
            if row['id']!=id:
                newData['data'].append(
                {
                    'id':i,
                    'name':row['name'],
                    'plec':row['plec'],
                    'klasa':row['klasa'],
                    'subclassa':row['subclassa'],
                    'rasa':row['rasa'],
                    'stats':row['stats'],
                    'traits':row['traits']   
                }
                )
                i+=1
        with open(file, "w") as outfile:
            json.dump(newData, outfile)
        return True
    return False
        

    
 
def genName(plec):
    imie = ""
    if plec == "Femelee":
        imie += femele_names[random.randint(0, 4389)]
        imie = imie.rstrip('\n')
    else:
        imie += mele_names[random.randint(0, 6300)]
        imie = imie.rstrip('\n')
    imie+=" "+last_name[random.randint(0, 10444)]
    return imie

    
def Stats():
    Statystyki = {
    'Strength': 0,
    'Dexterity': 0,
    'Constitution': 0,
    'Intelligence': 0,
    'Wisdom': 0,
    'Charisma': 0
}
    for i in range(6):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll3 = random.randint(1, 6)
        roll4 = random.randint(1, 6)
        nums = [roll1, roll2, roll3, roll4]
        lowest = min(nums)
        score = roll1 + roll2 + roll3 + roll4 - lowest
        Statystyki[Statystyki.keys()[i]] = score
        
    return Statystyki

def AutisticStats():
    Statystyki = {
    'Strength': 0,
    'Dexterity': 0,
    'Constitution': 0,
    'Intelligence': 0,
    'Wisdom': 0,
    'Charisma': 0
}

    for i in range(6):
        Statystyki[Statystyki.keys()[i]] = random.randint(1, 18)


def IntStats(klasa):
    Statystyki = {
    'Strength': 0,
    'Dexterity': 0,
    'Constitution': 0,
    'Intelligence': 0,
    'Wisdom': 0,
    'Charisma': 0
}
    primary = "Dexterity"
    class_result = json.load(open("json/clases.json"))
    for row in class_result['results']:
        if row['name'] == klasa:
            primary = row['primary']

    score_list = []
    for i in range(6):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll3 = random.randint(1, 6)
        roll4 = random.randint(1, 6)
        nums = [roll1, roll2, roll3, roll4]
        lowest = min(nums)
        score_list.append(roll1 + roll2 + roll3 + roll4 - lowest)

    Statystyki[primary] = max(score_list)
    score_list.remove(max(score_list))
    if primary != "Dexterity":
        Statystyki["Dexterity"] = max(score_list)
        score_list.remove(max(score_list))
        atrib = [
            "Strength", "Constitution", "Intelligence", "Wisdom", "Charisma"
        ]
        atrib.remove(primary)
        for i in range(4):
            k = random.choice(atrib)
            Statystyki[k] = score_list[0]
            score_list.pop(0)
            atrib.remove(k)
    else:
        atrib = [
            "Strength", "Constitution", "Intelligence", "Wisdom", "Charisma"
        ]
        for i in range(5):
            k = random.choice(atrib)
            Statystyki[k] = score_list[0]
            score_list.pop(0)
            atrib.remove(k)
    return Statystyki




class DungeonsAndDragons():
    def __init__(self, inteligence, author) -> None:
        self.author = author
        self.LosujKlasa()
        self.LosujSub()
        self.Plec = random.choice(["Melee", "Femelee"])
        if inteligence == "Autistic":
            self.Stats = AutisticStats()
        elif inteligence != "No":
            self.Stats = Stats()
        else:
            self.Stats = IntStats(self.Klasa)
        self.LosujRasa()
        # self.Opis
        self.LosujTraits()
        self.Imie = genName(self.Plec)
        self.SaveToJson()
        
    def __init__(self, author, id) -> None:
        self.author = author
        file = "".join(["json/data/", str(self.author), ".json"])
        if os.path.isfile(file):
            with open(file, 'r') as js:
                data = json.load(js)
            for row in data['data']:
                if row['id']==id:
                    self.Klasa = row['klasa']
                    self.Subklasa = row['subclassa']
                    self.Imie = row['name']
                    self.Plec = row['plec']
                    self.Rasa = row['rasa']
                    self.Stats = row['stats']
                    self.Traits = row['traits']
        
    def LosujKlasa(self):
        self.Klasa =  random.choice(list(class_dir.keys()))
    
    def LosujSub(self):
        self.Subklasa =  random.choice(class_dir[self.Klasa])
    
    def LosujRasa(self):
        self.Rasa = random.choice(race_list)
        rr = open("json/newrases.json")
        race_result = json.load(rr)
        for row in race_result['results']:
            if str(row['name']) == self.Rasa:
                hated_i = []
                # print(row['asi'])
                for att in row['asi']:
                    for i in range(0, 6):
                        # print(atrybuty[i])
                        # print(att['attributes'][0])
                        if list(self.Stats.keys())[i] == att['attributes'][0]:
                            self.Stats[list(self.Stats.keys())[i]] += att['value']
                            hated_i.append(i)
                for att in row['asi']:
                    if att['attributes'][0] == 'Other':
                        att_dodaj = random.randint(0, 5)
                        try:
                            hated_i.index(att_dodaj)
                        except:
                            self.Stats[list(self.Stats.keys())[att_dodaj]] += att['value']
                            hated_i.append(att_dodaj)
                        att_dodaj = random.randint(0, 5)
        rr.close()
        
    def LosujTraits(self):
        self.Traits = []
        for i in range(random.randint(2,4)):
            rand = random.choice(new_traits)
            if rand in self.Traits:
                i=-1
            self.Traits.append(rand)
    
    def ReturnEmbed(self, ctx, name):
        final = ("**Rasa:** " + self.Rasa + "\n" + 
                "**Klasa:** " + self.Klasa + '\n' + 
                "**Subklasa:** " + self.Subklasa + '\n' + 
                str(self.Stats) + '\n' + 
                '**Sex:** ' + self.Plec + '\n' + 
                '**Personality:** ')
        
        for trait in self.Traits:
            final += str(trait) + " "
        
        paiting.Paint(self.Stats, name)
        return (
    hikari.Embed(title=self.Imie, description=final, color=random.choice(colors.colors_list))
        .set_thumbnail(klasy_art[self.Klasa])
        .set_image(name)
        .set_footer(" ".join([str(ctx.author), "●",str(time.strftime("%H:%M"))]))
    )
    
    def SaveToJson(self):
        file = "".join(["json/data/", str(self.author), ".json"])
        if os.path.isfile(file):
            with open(file, 'r') as js:
                data = json.load(js)
                
            add =   {
                        'id':data['count']+1,
                        'name':self.Imie,
                        'plec':self.Plec,
                        'klasa':self.Klasa,
                        'subclassa':self.Subklasa,
                        'rasa':self.Rasa,
                        'stats':self.Stats,
                        'traits':self.Traits
                    }
            data['data'].append(add)
            data['count']+=1
            with open(file, "w") as outfile:
                json.dump(data, outfile)
        else:
            data = {
                'count':1, 
                'data':[
                    {
                        'id':1,
                        'name':self.Imie,
                        'plec':self.Plec,
                        'klasa':self.Klasa,
                        'subclassa':self.Subklasa,
                        'rasa':self.Rasa,
                        'stats':self.Stats,
                        'traits':self.Traits
                    }
                ]
                }
            with open(file, "w") as outfile:
                json.dump(data, outfile)
                
    def ChangeName(self, name):
        file = "".join(["json/data/", str(self.author), ".json"])
        with open(file, 'r') as js:
            data = json.load(js)
        for row in data['data']:
            if row['name']==self.Imie:
                row['name']=name
                self.Imie=name
                break
        with open(file, "w") as outfile:
            json.dump(data, outfile)
            
            
class ButtonViewDungeon(miru.View):
    def __init__(self, NDungeon,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.Dungeon = NDungeon
    @miru.button(label="Change Name")
    async def btn_punkty(self, button: miru.Button, ctx:miru.Context):
        modal = DungeonModal(NDungeon=self.Dungeon, title="Rozdziel Wojownikow!")
        await ctx.respond_with_modal(modal)
            
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        await self.message.edit(components=[])
        self.Dungeon=None
        self.stop()
        
class ButtonViewPages(miru.View):
    def __init__(self, page, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.page = page
    @miru.button(emoji="⬅️", style=hikari.ButtonStyle.SUCCESS)
    async def btn_prev(self, button: miru.Button, ctx:miru.Context):
        if self.page == 1:
            pass
        else:
            self.page-=1
            await ctx.edit_response(ShowAll(ctx, self.page))
    @miru.button(label="PAGE", style=hikari.ButtonStyle.SUCCESS)
    async def btn_page(self, button: miru.Button, ctx:miru.Context):
        pass
    @miru.button(emoji="➡️", style=hikari.ButtonStyle.SUCCESS)
    async def btn_next(self, button: miru.Button, ctx:miru.Context):
        self.page+=1
        await ctx.edit_response(ShowAll(ctx, self.page))
    
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        # await self.message.edit(components=[])
        await self.message.delete()
        self.page=None
        self.stop()
        

        
        
class DungeonModal(miru.Modal):
    def __init__(self, NDungeon,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.Dungeon = NDungeon
    newName = miru.TextInput(label="Name", placeholder="Write down new name", required=True)

    

    async def callback(self, ctx: miru.ModalContext) -> None:
        name = "".join(["Arts/Stats/",str(ctx.author.id), ".png"])
        self.Dungeon.ChangeName(self.newName.value)
        await ctx.edit_response(embed=self.Dungeon.ReturnEmbed(ctx, name))
        os.remove(name)
        