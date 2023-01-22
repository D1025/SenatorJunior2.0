import json
import os
import random
import time
import paiting
import hikari
import miru
import colors
import sqlite3
import data
import ast


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



def ShowRases(cursor):
    rases = data.allRases(cursor)
    New_str = ""
    for element in rases:
        New_str+=str(element+"\n")
    return hikari.Embed(title="RASES", description=New_str, color=random.choice(colors.colors_list))
    

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
                
def DataShowAll(conn, ctx, page):
    c = conn.cursor()
    if not data.ifInDataBase(c, ctx.author.id):
        return (
        hikari.Embed(title="You have 0 characters..", description="", color=random.choice(colors.colors_list))
        .set_thumbnail("Arts/Logos/DnD.png")
        .set_footer(" ".join([str(ctx.author), "●",str(time.strftime("%H:%M"))]))
    )
    c.execute("SELECT characters FROM USERS WHERE id = ?", (str(ctx.author.id),))
    j = c.fetchall()[0][0]
    embed = (hikari.Embed(title="".join([str(ctx.author), " you have ", str(j), " characters"]), description="", color=random.choice(colors.colors_list))
        .set_thumbnail("Arts/Logos/DnD.png")
        .set_footer(" ".join([str(ctx.author), "●",str(time.strftime("%H:%M"))])))
    c.execute("SELECT c.name, r.name, k.name, sk.name FROM CHARACTERS c, CLASS k, SUBCLASS sk, RASE r WHERE c.class=k.class_id AND c.subclass=sk.subclass_id AND c.rase=r.rase_id AND c.whoes = ?", (str(ctx.author.id),))
    dat = c.fetchall()
    k=1
    for i in range (j):
        if int(k/11)+1 != page:
            k+=1
            continue
        if k == (10*page)+1:
            break
        final = dat[i][1] + ", " + dat[i][2] + " - " + dat[i][3]
        embed.add_field("".join([str(k), " - " ,dat[i][0]]), final)
        k+=1
    return embed
    
def deleteFromJson(author, id):
    file = "".join(["json/data/", str(author), ".json"])
    if os.path.isfile(file):
        with open(file, 'r') as js:
            data = json.load(js)
            
        if data['count']<id:
            return False
        if id<=0:
            return False
        
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


def deleteFromData(conn, author, id):
    c = conn.cursor()
    conn.execute("BEGIN")
    c.execute("SELECT characters FROM USERS WHERE id = ?", (str(author.id),))
    fetchId = c.fetchall()[0][0]
    
    if id<=0:
        return False
    if fetchId<id:
        return False
    
    c.execute("UPDATE USERS SET characters = ? WHERE id = ?", (fetchId-1, str(author.id)))
    c.execute("SELECT id, stats FROM CHARACTERS WHERE whoes = ?", (str(author.id),))
    fetchId = c.fetchall()[id-1]
    c.execute("DELETE FROM CHARACTERS WHERE id = ?", (fetchId[0],))
    c.execute("DELETE FROM STATS WHERE stats_id = ?", (fetchId[1],))
    
    conn.commit()
    return True

    
        
def Check(author, id):
    file = "".join(["json/data/", str(author), ".json"])
    if os.path.isfile(file):
        with open(file, 'r') as js:
            data = json.load(js)
            
        if data['count']<id:
            return False
        if id<=0:
            return False
    return True
    
 
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
        Statystyki[list(Statystyki.keys())[i]] = score
        
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
        Statystyki[list(Statystyki.keys())[i]] = random.randint(1, 18)
        
    return Statystyki


def IntStats(primary):
    Statystyki = {
    'Strength': 0,
    'Dexterity': 0,
    'Constitution': 0,
    'Intelligence': 0,
    'Wisdom': 0,
    'Charisma': 0
}

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
    def __init__(self) -> None:
        pass
    
    def normal(self, inteligence, author, conn, rase) -> None:
        self.conn = conn
        self.author = author
        self.LosujKlasa()
        self.LosujSub()
        self.Plec = random.choice(["Melee", "Femelee"])
        if inteligence == "Autistic":
            self.Stats = AutisticStats()
        elif inteligence != "No":
            self.Stats = Stats()
        else:
            self.Stats = IntStats(self.Primary)
        self.LosujRasa(rase)
        # self.Opis
        self.LosujTraits()
        self.genName()
        self.saveToData()
        return self

        
    def from_file(self, author, id) -> None:
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
        return self
    
    def fromData(self, conn, author, id) -> None:
        self.conn = conn
        self.author = author
        c = self.conn.cursor()
        c.execute("SELECT id FROM CHARACTERS WHERE whoes = ?", (str(author.id),))
        fetchId = c.fetchall()[id-1][0]
        c.execute("SELECT c.name, c.sex, k.name, sk.name, r.name, c.traits, c.stats FROM CHARACTERS c, CLASS k, SUBCLASS sk, RASE r WHERE c.class=k.class_id AND c.subclass=sk.subclass_id AND c.rase=r.rase_id AND c.id = ?", (fetchId,))
        fetchId = c.fetchall()[0]
        self.Imie = fetchId[0]
        self.Plec = fetchId[1]
        self.Klasa = fetchId[2]
        self.Subklasa = fetchId[3]
        self.Rasa = fetchId[4]
        self.Traits = ast.literal_eval(fetchId[5])
        c.execute("SELECT * FROM STATS WHERE stats_id = ?", (fetchId[6],))
        fetchId = c.fetchall()[0]
        self.Stats = {
        'Strength': fetchId[1],
        'Dexterity': fetchId[2],
        'Constitution': fetchId[3],
        'Intelligence': fetchId[4],
        'Wisdom': fetchId[5],
        'Charisma': fetchId[6]
                    }
        fetchId = None
        return self
        
        
    def LosujKlasa(self):
        c = self.conn.cursor()
        c.execute("SELECT name, primary_att FROM CLASS ORDER BY RANDOM() LIMIT 1")
        row = c.fetchall()
        self.Klasa = row[0][0]
        self.Primary = row[0][1]
        # self.Klasa =  random.choice(list(class_dir.keys()))
    
    def LosujSub(self):
        c = self.conn.cursor()
        c.execute("SELECT name FROM SUBCLASS WHERE class = (SELECT class_id FROM CLASS WHERE name = ?) ORDER BY RANDOM() LIMIT 1 ", (self.Klasa,))
        row = c.fetchall()
        self.Subklasa = row[0][0]
        # self.Subklasa =  random.choice(class_dir[self.Klasa])
    
    def LosujRasa(self, rase):
        c = self.conn.cursor()
        if rase == "Random":
            c.execute("SELECT RASE.name, STATS.strength, STATS.dexterity, STATS.constitution, STATS.intelligence, STATS.wisdom, STATS.charisma, STATS.other FROM RASE JOIN STATS ON RASE.bonus_stats=STATS.stats_id ORDER BY RANDOM() LIMIT 1")
        else:
            c.execute("SELECT RASE.name, STATS.strength, STATS.dexterity, STATS.constitution, STATS.intelligence, STATS.wisdom, STATS.charisma, STATS.other FROM RASE JOIN STATS ON RASE.bonus_stats=STATS.stats_id WHERE RASE.name = ? LIMIT 1", (str(rase),))
        rows = c.fetchall()
        self.Rasa = rows[0][0]
        for i in range(0,6):
            self.Stats[list(self.Stats.keys())[i]]+=rows[0][i+1]
        for i in range (0,rows[0][7]):
            self.Stats[list(self.Stats.keys())[random.randrange(0,5)]]
        """
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
        """
        
    def LosujTraits(self):
        self.Traits = []
        rand = random.randrange(2,4)
        c = self.conn.cursor()
        c.execute("SELECT trait FROM TRAITS ORDER BY RANDOM() LIMIT ?", (rand,))
        rows = c.fetchall()
        for i in range(rand):
            self.Traits.append(rows[i][0])
        # for i in range(random.randint(2,4)):
        #     rand = random.choice(new_traits)
        #     if rand in self.Traits:
        #         i=-1
        #     self.Traits.append(rand)
    
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
                
    def saveToData(self):
        c = self.conn.cursor()
        self.conn.execute("BEGIN")
        if not data.ifInDataBase(c, self.author.id):
            c.execute("INSERT INTO USERS (id, name, characters) VALUES (?, ?, ?)", (str(self.author.id), str(self.author), 0))
        c.execute("SELECT characters FROM USERS WHERE id = ? LIMIT 1", (str(self.author.id),))
        row = c.fetchall()
        amout = row[0][0]+1
        c.execute("UPDATE USERS SET characters = ? WHERE id = ?", (amout, str(self.author.id)))
        c.execute("INSERT INTO STATS (strength, dexterity, constitution, intelligence, wisdom, charisma, other) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (self.Stats['Strength'],self.Stats['Dexterity'],self.Stats['Constitution'],self.Stats['Intelligence'],self.Stats['Wisdom'],self.Stats['Charisma'],0))
        c.execute("SELECT last_insert_rowid()")
        new_id = c.fetchone()[0]
        c.execute("INSERT INTO CHARACTERS (whoes, name, sex, class, subclass, rase, subrase, stats, traits) VALUES (?, ?, ?, (SELECT class_id FROM CLASS WHERE name = ?), (SELECT subclass_id FROM SUBCLASS WHERE name = ?), (SELECT rase_id FROM RASE WHERE name = ?), ?, ?,?)", 
                  (str(self.author.id), self.Imie, self.Plec, self.Klasa, self.Subklasa, self.Rasa, 1, new_id, str(self.Traits)))
        self.conn.commit()
        
                
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
            
    def DataChangeName(self, name):
        c = self.conn.cursor()
        self.conn.execute("BEGIN")
        c.execute("UPDATE CHARACTERS SET name = ? WHERE whoes = ? AND name = ?", (name, self.author.id, self.Imie))
        self.Imie = name
        self.conn.commit()
            
    def genName(self):
        c = self.conn.cursor()
        self.Imie = ""
        if self.Plec == "Femelee":
            c.execute("SELECT name FROM FEMELE_NAMES ORDER BY RANDOM() LIMIT 1")
            row = c.fetchall()
            self.Imie += row[0][0]
            self.Imie = self.Imie.rstrip('\n')
        else:
            c.execute("SELECT name FROM MELE_NAMES ORDER BY RANDOM() LIMIT 1")
            row = c.fetchall()
            self.Imie += row[0][0]
            self.Imie = self.Imie.rstrip('\n')
        c.execute("SELECT name FROM FEMELE_NAMES ORDER BY RANDOM() LIMIT 1")
        row = c.fetchall()
        self.Imie+=" "+row[0][0]
            
            
class ButtonViewDungeon(miru.View):
    def __init__(self, NDungeon,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.Dungeon = NDungeon
    @miru.button(label="Change Name")
    async def btn_punkty(self, button: miru.Button, ctx:miru.Context):
        if str(ctx.author.id) == str(self.Dungeon.author.id):
            modal = DungeonModal(NDungeon=self.Dungeon, title="Zmień imie!")
            await ctx.respond_with_modal(modal)
        else:
            pass
            
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        await self.message.edit(components=[])
        self.Dungeon=None
        self.stop()
        
class ButtonViewPages(miru.View):
    def __init__(self,conn, autid, page, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.page = page
        self.conn = conn
        self.author_id = autid
    @miru.button(emoji="⬅️", style=hikari.ButtonStyle.SUCCESS)
    async def btn_prev(self, button: miru.Button, ctx:miru.Context):
        if str(ctx.author.id) != str(self.author_id):
            pass
        else:
            if self.page == 1:
                pass
            else:
                self.page-=1
                await ctx.edit_response(DataShowAll(self.conn, ctx, self.page))
    @miru.button(label="PAGE", style=hikari.ButtonStyle.SUCCESS)
    async def btn_page(self, button: miru.Button, ctx:miru.Context):
        pass
    @miru.button(emoji="➡️", style=hikari.ButtonStyle.SUCCESS)
    async def btn_next(self, button: miru.Button, ctx:miru.Context):
        if str(ctx.author.id) != str(self.author_id):
            pass
        else:
            self.page+=1
            await ctx.edit_response(DataShowAll(self.conn, ctx, self.page))
    
    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True # Disable all items attached to the view
        # await self.message.edit(components=[])
        await self.message.delete()
        self.page=None
        self.conn=None
        self.stop()
        

        
        
class DungeonModal(miru.Modal):
    def __init__(self, NDungeon,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.Dungeon = NDungeon
    newName = miru.TextInput(label="Name", placeholder="Write down new name", required=True)

    

    async def callback(self, ctx: miru.ModalContext) -> None:
        name = "".join(["Arts/Stats/",str(ctx.author.id), ".png"])
        self.Dungeon.DataChangeName(self.newName.value)
        await ctx.edit_response(embed=self.Dungeon.ReturnEmbed(ctx, name))
        os.remove(name)
        