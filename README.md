# SenatorJunior - verion alfa 2.1

Bot for a Dungeons and Dragons 5e game, (and exalted rolls)

INVITE - https://discord.com/api/oauth2/authorize?client_id=818488309353283624&permissions=964220537920&scope=bot%20applications.commands


# DUNGEONS AND DRAGONS
"/dnd make" - makes a randomly generated character for a 5e. Rolls all races and classes. Also adds API from races to scores.

It also have a button for changing name if you want.

It have intelligence based for scores and putting highest for a main. The base roll is the 3 highest out of 4d6.

An example

![image](https://user-images.githubusercontent.com/69533622/212430302-a97200f3-761f-4468-92af-441b8c681675.png)
![image](https://user-images.githubusercontent.com/69533622/212430367-37bb54ec-03b1-4ac8-89e8-c060d87e9bdd.png)


It accepts an optional variable - intelligence

![image](https://user-images.githubusercontent.com/69533622/212430147-2063b819-4fdc-4641-9904-eb19439db33e.png)
![image](https://user-images.githubusercontent.com/69533622/212430168-299bc7f1-a4b6-4c85-a427-e7abc6d9b5a4.png)


"Turn off"

You can use it if you don't really want good character. The bot will randomly distribute all stats without taking character class into account.

"Autistic"

Oh boy, you hate good character, you like to see 1 on some stats? This is the mode for you. Bot will randomly roll 1d18 for each stat! If you're lucky, you'll get more than one "1" on a stat!


"/dnd show-all" - will show you a full list of the characters you made, you can check the character id here.

![image](https://user-images.githubusercontent.com/69533622/212433189-93a93267-d757-4e0c-94dc-56173121bb54.png)

"/dnd show" - takes an additional argument - id and shows full character like /dnd make, you can also change character name here.

"/dnd delete" - takes an additional argument - id and exactly as you think it deletes the character from the database - PERMANENTLY!

# LAST UPDATE 
alfa2.0 -> alfa2.1

Changed whole structure, we're adding whole database for a name, character, values etc. Previously bot worked with json files and number of these files was increasing fast. So here it is brand new sqlite structure. Nothing has changed for a normal user, everything looks and works the same as before.

# TO DO
✅Switch to the sqlite database system

❌Add subclasses

✅Change to class based system

✅Add character database

❌Add character customization (change by race/class imput)

✅Add random name generator

❌Add favorite character marker

❌Probable character limit for users, it's not needed

Long term to do:

❌Add full character creation