from PIL import Image, ImageDraw, ImageFont

def Paint(Statystyki, name):

  img = Image.open('Arts/Stats/DnDAE.png')
  I1 = ImageDraw.Draw(img)

  # colour_black = (0,0,0)
  colour = (128, 113, 85)
  colour_mod = (128, 113, 85)
  font_mod = ImageFont.truetype("Arts/font/Quick.ttf", 70)
  DnD_mod = {1:"-5", 2:"-4", 3:"-4", 4:"-3", 5:"-3", 6:"-2", 7:"-2", 8:"-1", 9:"-1", 10:"+0", 11:"+0", 12:"+1", 13:"+1", 14:"+2", 15:"+2", 16:"+3", 17:"+3", 18:"+4", 19:"+4", 20:"+5"}
  font = ImageFont.truetype("Arts/font/Quick.ttf", 150)
  
  p = Statystyki['Strength']
  s = str(Statystyki['Strength'])
  if p > 19:
    I1.text((55, 70), s ,font=font, fill=colour)
  elif p == 11:
    I1.text((85, 70), s ,font=font, fill=colour)
  elif p > 9 and p!= 11:
    I1.text((65, 70), s ,font=font, fill=colour)
  elif p > 1:
    I1.text((90, 70), s ,font=font, fill=colour)
  else:
    I1.text((105, 70), s ,font=font, fill=colour)

  if DnD_mod[p] == "-1" or DnD_mod[p] == "+1":
    I1.text((100, 210), DnD_mod[p], font=font_mod, fill=colour_mod)
  else:
    I1.text((92, 210), DnD_mod[p], font=font_mod, fill=colour_mod)


  p = Statystyki['Dexterity']
  s = str(Statystyki['Dexterity'])
  if p > 19:
    I1.text((300, 70), s ,font=font, fill=colour)
  elif p == 11:
    I1.text((330, 70), s ,font=font, fill=colour)
  elif p > 9 and p!= 11:
    I1.text((320, 70), s ,font=font, fill=colour)
  elif p > 1:
    I1.text((340, 70), s ,font=font, fill=colour)
  else:
    I1.text((355, 70), s ,font=font, fill=colour)

  if DnD_mod[p] == "-1" or DnD_mod[p] == "+1":
    I1.text((345, 210), DnD_mod[p], font=font_mod, fill=colour_mod)
  else:
    I1.text((337, 210), DnD_mod[p], font=font_mod, fill=colour_mod)

  p = Statystyki['Constitution']
  s = str(Statystyki['Constitution'])
  if p > 19:
    I1.text((550, 70), s ,font=font, fill=colour)
  elif p == 11:
    I1.text((580, 70), s ,font=font, fill=colour)
  elif p > 9 and p!= 11:
    I1.text((570, 70), s ,font=font, fill=colour)
  elif p > 1:
    I1.text((590, 70), s ,font=font, fill=colour)
  else:
    I1.text((605, 70), s ,font=font, fill=colour)

  if DnD_mod[p] == "-1" or DnD_mod[p] == "+1":
    I1.text((595, 210), DnD_mod[p], font=font_mod, fill=colour_mod)
  else:
    I1.text((587, 210), DnD_mod[p], font=font_mod, fill=colour_mod)


  p = Statystyki['Intelligence']
  s = str(Statystyki['Intelligence'])
  if p > 19:
    I1.text((55, 365), s ,font=font, fill=colour)
  elif p == 11:
    I1.text((85, 365), s ,font=font, fill=colour)
  elif p > 9 and p!= 11:
    I1.text((65, 365), s ,font=font, fill=colour)
  elif p > 1:
    I1.text((90, 365), s ,font=font, fill=colour)
  else:
    I1.text((105, 365), s ,font=font, fill=colour)

  if DnD_mod[p] == "-1" or DnD_mod[p] == "+1":
    I1.text((100, 510), DnD_mod[p], font=font_mod, fill=colour_mod)
  else:
    I1.text((92, 510), DnD_mod[p], font=font_mod, fill=colour_mod)


  p = Statystyki['Wisdom']
  s = str(Statystyki['Wisdom'])
  if p > 19:
    I1.text((300, 365), s ,font=font, fill=colour)
  elif p == 11:
    I1.text((340, 365), s ,font=font, fill=colour)
  elif p > 9 and p!= 11:
    I1.text((320, 365), s ,font=font, fill=colour)
  elif p > 1:
    I1.text((340, 365), s ,font=font, fill=colour)
  else:
    I1.text((355, 365), s ,font=font, fill=colour)

  if DnD_mod[p] == "-1" or DnD_mod[p] == "+1":
    I1.text((345, 510), DnD_mod[p], font=font_mod, fill=colour_mod)
  else:
    I1.text((337, 510), DnD_mod[p], font=font_mod, fill=colour_mod)

  p = Statystyki['Charisma']
  s = str(Statystyki['Charisma'])
  if p > 19:
    I1.text((550, 365), s ,font=font, fill=colour)
  elif p == 11:
    I1.text((590, 365), s ,font=font, fill=colour)
  elif p > 9 and p!= 11:
    I1.text((570, 365), s ,font=font, fill=colour)
  elif p > 1:
    I1.text((590, 365), s ,font=font, fill=colour)
  else:
    I1.text((605, 365), s ,font=font, fill=colour)

  if DnD_mod[p] == "-1" or DnD_mod[p] == "+1":
    I1.text((595, 510), DnD_mod[p], font=font_mod, fill=colour_mod)
  else:
    I1.text((587, 510), DnD_mod[p], font=font_mod, fill=colour_mod)
    
  img.save(name)
  img.close()