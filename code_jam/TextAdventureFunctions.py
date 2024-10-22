import random
import os

inventory = ["Nothing", "Nothing", "Nothing", "Nothing"]
location = ["cabin", "woods", "crossroad", "well", "left", "right", "mineEntrance", "mine", "amuletRoom"]
name = []

def commands():
  print()
  print("\t1. Look. type 'look' in order to get a better description of the area and any possible things of interest that might help you on your journey.")
  print()
  print("\t2. Take. Type 'take' followed by the name of the object you'd like to take with you for the confirm prompt in order to add it to your inventory.")
  print()
  print("\t3. Use. Type 'use' in order to open your inventory and see what items you currently have on you. Then type what item you'd like to use in the comfirm prompt to select it.")
  print()
  print("\t4. Left or Right. Type 'left' or 'right' when you have finished exploring the area and have decided on which direction you would like to go.")
  print()
  print("\t5. Continue. Type 'continue' when going forwards is the only directional option, and you are commited to the path you've chosen.")
  print()
  print("\t6. Help. Type 'help' at any time when you forget these commands and would like to see this screen again.")
  print()


def username():
    user = input("Enter your name, adventurer: ")
    name.append(user)
    os.system('cls')
    

def look(currentlocation, lanternOn):
  os.system('cls')
  print()
  if currentlocation == "cabin" and inventory[0] != "axe" and inventory[1] != "lantern":
    print("You look around your cabin, there's a small table and chair, your messy bed, and your cooling fireplace. Your axe rests up against the wall by the door, as your lantern sits on the small wooden table next to it.")
    print()
  elif currentlocation == "cabin" and inventory[0] != "axe" and inventory[1] == "lantern":
    print("You look around your cabin, there's a small table and chair, your messy bed, and your cooling fireplace. Your axe rests up against the wall by the door.")
    print()
  elif currentlocation == "cabin" and inventory[0] == "axe" and inventory[1] != "lantern":
    print("You look around your cabin, there's a small table and chair, your messy bed, and your cooling fireplace. Your lantern sits on the small wooden table next to the door.")
    print()
  elif currentlocation == "cabin" and inventory[0] == "axe" and inventory[1] == "lantern":
    print("You look around your cabin, there's a small table and chair, your messy bed, and your cooling fireplace. There's not much else of notice.")
    print()
  if currentlocation != "cabin" and lanternOn == False:
      print("It's too dark to see anything, it's getting colder and you don't know where to go.")
      print()
  elif currentlocation == "woods" and lanternOn == True:
    print("You see a faint outline of a dirt path in the distance leading deeper into the woods. It doesn't look familiar at all. Any attempt at finding your cabin you know would end with your death. It seems you only have one option.")
    print()
  elif currentlocation == "crossroad" and lanternOn == True:
    print("There seems to be two paths. The left is winding and it quickly becomes unclear where the path begins and ends, and in the distance you can just barely see that it becomes blocked by large sticks and tree branches. It's clearly")
    print("been abandoned and has decayed by the passage of time. While the right side is a long, clear, stone path into the darkness, leading into the unknown. Or you could continue forward and check out the old well.")
    print()
  elif currentlocation == "left" and lanternOn == True:
    print("You lift your lantern up towards the branches and sticks, but in your carelessness you drop your lantern and it breaks. Suddenly, the woods catch fire and quickly encircle you in a tomb of flames. Your lungs are scortched by")
    print("the fumes as you gasp for breath. Wheezing, you collapse to the ground dead.")
    print()
    for x in range(2):
      inventory.append("Nothing")
      inventory.pop(0)
      x += 1
    lanternOn = False
    cabin()
  elif currentlocation == "right" and lanternOn == True:
    print("You decide to get closer to get a better look. The body of what you presumed was a dead animal is now burned into your brain. You're horrified to realize that the corpse is human, and what remains of its head is just a red mush,")
    print("as if it exploded. Judging by the man's attire, he was once a miner. In fact, by his side you see the faint outline of his dull pickaxe.")
    print()
  elif currentlocation == "mineEntrance" and lanternOn == True:
    print("You look around, and realize that surrounding the mine is corpses of the miners. Their heads are nothing but red mush, as if they were crushed, or perhaps even exploded. Perhaps they saw something they shouldn't have inside.")
    print()
  elif currentlocation == "mine" and lanternOn == True:
    print("You look closer at the wall, and realize that it is not a solid formation of rock, but a clear pile of multiple rocks blocking a path further into the mine to what you pray to be an exit. Perhaps with the right tool you could")
    print("clear the way.")
    print()
  elif currentlocation == "amuletRoom" and lanternOn == True:
    print("The shimmering amulet in the darkness has a natural glow to it, and if you listen very closely, you can just barely hear whispers eminating from it, but you can't quite make out what they say.")
    print()
  """
  elif currentlocation == "well" and lanternOn == True:
    print("You try to lean over the well holding your lantern as far down as you can reach to see if you can get a better look of the bottom, but the darkness goes on seemingly forever. Instead, you decide to grab a nearby rock and throw")
    print("it inside to test the depth. You drop the rock and wait for an uncomfortably long time until eventually it hits the ground with a faint thud. Just how deep does this well go?")
    print()
  """

def take(currentlocation):
  os.system('cls')
  if currentlocation == "cabin":
    print()
    print("What would you like to take?")
    takingitem = input("")
    if takingitem == "axe":
      if inventory[0] == "axe":
        print()
        print("You already have that.")
        print()
      else:
        print()
        print(takingitem+" was added to your inventory.")
        inventory.pop(0)
        inventory.insert(0, takingitem)
        print()
    elif takingitem == "lantern": 
      if inventory[1] == "lantern":
        print()
        print("You already have that.")
        print()
      else:
        print()
        print(takingitem+" was added to your inventory.")
        inventory.pop(1)
        inventory.insert(1, takingitem)
        print()
    else: 
      print()
      print("You can't take that.")
      print()
  elif currentlocation == "woods" or currentlocation == "crossroad" or currentlocation == "left" or currentlocation == "mineEntrance":
    print()
    print("Nothing to take.")
    print()
  elif currentlocation == "right":
    print()
    print("What would you like to take?")
    takingitem = input("")
    if takingitem == "pickaxe":
      if inventory[2] == "pickaxe":
        print()
        print("You already have that.")
        print()
      else:
        print()
        print(takingitem+" was added to your inventory.")
        inventory.pop(2)
        inventory.insert(2, takingitem)
        print()
    elif takingitem == "axe":
      if inventory[0] == "axe":
        print()
        print("You already have that.")
        print()
    elif takingitem == "lantern":
      if inventory[1] == "lantern":
        print()
        print("You already have that.")
        print()
    else:
      print()
      print("You can't take that.")
      print()
  elif currentlocation == "amuletRoom":
    print()
    print("What would you like to take?")
    takingitem = input("")
    if takingitem == "axe" or takingitem == "lantern" or takingitem == "pickaxe":
      print()
      print("You already have that.")
      print()
    elif takingitem == "amulet":
      print()
      print("You pick up the amulet. It's somehow warm to the touch, and gives you a feeling of safety that makes you feel nostalgic, and comforted.")
      inventory.pop(3)
      inventory.insert(3, takingitem)
    else:
      print()
      print("You can't take that.")
      print()


def openInventory(userinput):
  if userinput == "use":
    print()
    for x in inventory:
      print(x)
    print()
    print("What item would you like to use?")
    using = input("")
    os.system('cls')
    print()
    return(using)


def cabin():   
  currentlocation = location[0]
  print()
  print("You gently open your eyes.")
  print()
  print()
  print("The storm rages on outside of your small log cabin. Your fire crackles quietly, now a dull flicker of embers as raindrops tap on your window and the roaring winds try to break inside. It's cold, you won't make it through the night")
  print("unless you get some more firewood.")
  print()
  while True:
    print()
    print("What would you like to do?")
    userinput = input("")
    userinput = userinput.lower()
    while userinput != "look" and userinput != "take" and userinput != "use" and userinput != "help" and userinput != "continue":
      userinput = input("Try again: ")
    if userinput == "look":
      look(currentlocation, False)
    elif userinput == "take":
      take(currentlocation)
    elif userinput == "use":
      x = openInventory(userinput)
      if x == "nothing" or x == "Nothing":
        print()
      else:
        print("You can't use that here.")
        print()
    elif userinput == "help":
      commands()
    elif userinput == "continue":
      woods()
      break


def woods():
  os.system('cls')
  currentlocation = location[1]
  lanternOn = False
  print()
  print("You leave your cabin, the cold air nips at your face. Surrounding you are uncountable trees, dozens of feet high. You've only walked for what you've though was thirty seconds and yet your cabin is completely out of sight and you've")
  print("lost your way. You've been swallowed by the woods. The haunting sounds of unknown wildlife and the faint glow of the moon on countless trees is about all you can make out.")
  print()
  while True:
    print()
    print("What would you like to do?")
    userinput = input("")
    userinput = userinput.lower()
    while userinput != "look" and userinput != "take" and userinput != "use" and userinput != "help" and userinput != "continue":
      userinput = input("Try again: ")
    if userinput == "look":
      if lanternOn == False:
        look(currentlocation, False)
      else:
        look(currentlocation, True)
    elif userinput == "take":
      take(currentlocation)
    elif userinput == "use":
      x = openInventory(userinput)
      if x == "nothing" or x == "Nothing":
        print()
      elif x == "lantern" and inventory[1] == "lantern":
        if lanternOn == True:
          print("You extinguish your lantern.")
          lanternOn = False
          print()
        else:
          lanternOn = True
          print("You light your lantern")
          print()
      else:
        print()
        print("You can't use that here.")
        print()
    elif userinput == "help":
      commands()
    elif userinput == "continue":
      if lanternOn != False:
        crossroad()
        break
      else:
        freezing()
        cabin()
        break
      

def crossroad():
  os.system('cls')
  lanternOn = True
  currentlocation = location[2]
  print()
  print("You continue onwards with your trusty lamp guiding your way. Your footsteps crunch through the snow as the path becomes more clear. Holding up your lantern, you see that you've ended up at a crossroads, with the road leading to two somewhat")
  print("defined paths leading to the left and the right. Or, you could continue forward and check out the old run-down well dead ahead.")
  print()
  while True:
    print()
    print("What would you like to do?")
    userinput = input("")
    userinput = userinput.lower()
    while userinput != "look" and userinput != "take" and userinput != "use" and userinput != "help" and userinput != "left" and userinput != "right" and userinput != "continue":
      userinput = input("Try again: ")
    if userinput == "look":
      look(currentlocation, lanternOn)
    elif userinput == "take":
      take(currentlocation)
    elif userinput == "use":
      x = openInventory(userinput)
      if x == "nothing" or x == "Nothing":
        print()
      elif x == "lantern" and inventory[1] == "lantern":
        if lanternOn == True:
          print("You extinguish your lantern.")
          lanternOn = False
          print()
        else:
          print("You light your lantern.")
          lanternOn = True
          print()
      else:
        print()
        print("You can't use that here.")
        print()
    elif userinput == "help":
      commands()
    elif userinput == "left":
      if lanternOn != False:
        left()
        break
      else:
        freezing()
        cabin()
        break
    elif userinput == "right":
      if lanternOn != False:
        right()
        break
      else:
        freezing()
        cabin()
        break
    """
    elif userinput == "continue":
      if lanternOn != False:
        well()
        break
      else:
        freezing()
        cabin()
        break
    """

"""
def well():
  os.system('cls')
  currentlocation = location[3]
  lanternOn = True
  print()
  print("You decide to continue forward to check out the old well. It emits a foul odor and seems to go deep into the ground into a shadowy abyss, far to dark to see the bottom.") 
  print()
  while True:
    print()
    print("What would you like to do?")
    userinput = input("")
    userinput = userinput.lower()
    while userinput != "look" and userinput != "take" and userinput != "use" and userinput != "help" and userinput != "continue":
      userinput = input("Try again: ")
    if userinput == "look" and lanternOn == True:
      look(currentlocation, lanternOn)
    elif userinput == "use":
      x = openInventory(userinput)
      if x == "nothing" or x == "Nothing":
        print()
      elif x == "lantern" and inventory[1] == "lantern":
        if lanternOn == True:
          print("You extinguish your lantern.")
          lanternOn = False
          print()
        else:
          print("You light your lantern.")
          lanternOn = True
          print()
    elif userinput == "help":
      commands()
"""

def left():
  os.system('cls')
  currentlocation = location[4]
  lanternOn = True
  print()
  print("You decide to head left. As you walk the crossroad disappears behind you into the unending darkness, and the path becomes more and more unpaved. As you wander, the sticks and branches seem to multiply, blocking increasingly more of")
  print("your path as they seem to twist and entangle themselves. Eventually you come to a complete stop, the broken tree limbs and sticks form a wall that no matter how hard you look, you can't seem to find an end to.")
  print()
  while True:
    print()
    print("What would you like to do?")
    userinput = input("")
    userinput = userinput.lower()
    while userinput != "look" and userinput != "take" and userinput != "use" and userinput != "help" and userinput != "continue":
      userinput = input("Try again: ")
    if userinput == "look" or inventory[0] == "Nothing":
      look(currentlocation, lanternOn)
    elif userinput == "take":
      take(currentlocation)
    elif userinput == "use":
      x = openInventory(userinput)
      if x == "nothing" or x == "Nothing":
        print()
      elif x == "lantern" and inventory[1] == "lantern":
        if lanternOn == True:
          print("You extinguish your lantern.")
          lanternOn = False
          print()
        else:
          print("You light your lantern.")
          lanternOn = True
          print()
      elif x == "axe" and lanternOn == True:
        print("You chop away at the tree limbs and branches with your axe as you slowly clear a path into the unknown.")  
        print()
        path = random.randint(0, 1)
        if path == 0:
          mineEntrance()
          break
        else:
          cave(name)
          break
      elif x == "axe" and lanternOn == False:
        print("You can't see what you need to chop.")
        print()
      else:
        print()
        print("You can't use that here.")
        print()
    elif userinput == "help":
      commands()
    elif userinput == "continue":
      print()
      print("You cannot continue, your path is blocked.")
      print()


def right():
  os.system('cls')
  currentlocation = location[5]
  lanternOn = True
  islooking = False
  print()
  print("You decide to head right. The path is long, and a thick fog clouds more and more of your vision as you continue onwards. Eventually you can barely see passed your nose even with your lamp, and as you wander aimlessly evenually you bump")
  print("into something with your foot. It's somewhat squishy, and you know with enough effort you could move it aside, or easily step over it. But far before you reached it you could smell its awful stench. Is this a dead animal?")
  print()
  while True:
    print()
    print("What would you like to do?")
    userinput = input("")
    userinput = userinput.lower()
    while userinput != "look" and userinput != "take" and userinput != "use" and userinput != "help" and userinput != "continue":
      userinput = input("Try again: ")
    if userinput == "look":
      if lanternOn == True:
        if inventory[2] == "pickaxe":
          print()
          print("The miner lays dead with nothing more to take.")
          print()
        else:
          islooking = True
          look(currentlocation, lanternOn)
      else:
        look(currentlocation, lanternOn)
    elif userinput == "take" and islooking == False:
      print()
      print("You don't know if there is anything to take until you have a closer look.")
      print()
    elif userinput == "take" and islooking == True:
      take(currentlocation)
    elif userinput == "use":
      x = openInventory(userinput)
      if x == "nothing" or x == "Nothing":
        print()
      elif x == "lantern" and inventory[1] == "lantern":
        if lanternOn == True:
          print("You extinguish your lantern.")
          lanternOn = False
          print()
        else:
          print("You light your lantern.")
          lanternOn = True
          print()
      else:
        print()
        print("You can't use that here.")
        print()
    elif userinput == "help":
      commands()
    elif userinput == "continue": 
      if lanternOn != False:
        path = random.randint(0, 1)
        if path == 0:
          mineEntrance()
          break
        elif path == 1:
          cave()
          break
      else:
        freezing()
        cabin()
        break


def cave():
  os.system('cls')
  print()
  print("Walking along the path you start to hear whispers calling out to you. ")
  for x in name:
    print(f"'{x}...'")
    print(f"'{x}...'")
    print(f"'{x}...'")
  print()
  print("The voice gets louder and louder, until eventually you find the source of the mysterious calling and end of the path. It's a cave, with voices echoing from deep inside. You decide to investigate. The echoing voice and dripping of water from")
  print("stalactites is thunderous, as well as your own breath and quickening heart rate. Eventually you find the source of the voice, and what you see is indescribable. A nightmarish, enormous, human-shaped creature, with an animal skull but far too")
  print("long appendages. You've never seen anything like this before, and yet you know for a fact that it is a DEMON.")
  print()
  print(f"'Hello {name[0]} ...' it says. 'We meet again it seems.' What is it talking about? You know damned well that if you saw something like that before, you would remember it. 'Still in a loop eh?' It snickers as your body shakes with fear")
  print("and mind races with confusion. 'Judging by the look on your face I shouldn't waste my breath explaining everything. Oh well, better luck next time!' In a single visceral instant, it slams its monstrous hand down, crushing you and every bone in")
  print("your body like a fly before you even have time to think.")
  print()
  for x in range(3):
    inventory.append("Nothing")
    inventory.pop(0)
    x += 1
  lanternOn = False
  cabin()


def mineEntrance():
  os.system('cls')
  currentlocation = location[6]
  lanternOn = True
  print()
  print("After a while you finally find the end of the path. An abandoned mine stands before you, its hastily been boarded up.")
  print()
  while True:
    print()
    print("What would you like to do?")
    userinput = input("")
    userinput = userinput.lower()
    while userinput != "look" and userinput != "take" and userinput != "use" and userinput != "help" and userinput != "continue":
      userinput = input("Try again: ")
    if userinput == "look":
      look(currentlocation, lanternOn)
    elif userinput == "take":
      take(currentlocation)
    elif userinput == "use":
      x = openInventory(userinput)
      if x == "nothing" or x == "Nothing":
        print()
      elif x == "lantern" and inventory[1] == "lantern":
        if lanternOn == True:
          print("You extinguish your lantern.")
          lanternOn = False
          print()
        else:
          print("You light your lantern.")
          lanternOn = True
          print()
      elif x == "axe" and lanternOn == True and inventory[0] == "axe":
        print("You chop away at the wooden boards. The more open the mine entrance gets however, the more anxious you feel. Something in your brain is telling you that you are in great danger. You take a deep breath and finish removing the last board.")
        print("The mine is now open to explore.")  
        print()
      elif x == "axe" and lanternOn == False:
        print("You can't see what you need to chop.")
        print()
      elif x == "axe" and inventory[0] == "Nothing":
        print("You realize that you forgot to bring your axe, and have no way of clearing the mine entrance. You decide to wander off the path and check to see if any of the miners have something that can help you. However, you get lost for an agonizingly")
        print("stressful period of time, searching desperately for a landmark you recognize. With incredible luck you manage to find what you believe to be the same path you were on and decide to follow it back to the mine to retrace your steps, but something")
        print("doesn't seem right.")
        cave()
        break
      else:
        print()
        print("You can't use that here.")
        print()
    elif userinput == "help":
      commands()
    elif userinput == "continue" and lanternOn == True:
      print()
      print("You step through the newly opened doorway into the abandonend mine. What could have possibly been so dangerous to cause the gruesome deaths of those men and for someone to board up the entrance? Are the boards to keep someone or something out,")
      print("or in? Just thinking about it makes your skin crawl.")
      print()
      mine()
      break
    elif userinput == "continue" and lanternOn == False:
      print()
      print("You won't continue before you light your lamp.")
      print()


def mine():
  os.system('cls')
  currentlocation = location[7]
  lanternOn = True
  islooking = False
  rubbleCleared = False
  print("You continue through the mine, your steps echo as you slowly make your way down. However, not long after you made your way in, the ground begins to shake, and dirt and pebbles fall from the ceiling as you are assaulted by the loudest sound you've")
  print("ever heard. The crumbling of rocks can be heard, and your realize that only exit has been blocked off. Your heart sinks, but you don't waste any time trying to break out, you just continue forward praying their is a second exit to the mine. However,")
  print("after an hour of walking, the mine comes to an abrupt end. You look left and right desperately hoping that there's another path you missed, but no such exit exists.")
  print()
  while True:
    print()
    print("What would you like to do?")
    userinput = input("")
    userinput = userinput.lower()
    while userinput != "look" and userinput != "take" and userinput != "use" and userinput != "help" and userinput != "continue":
      userinput = input("Try again: ")
    if userinput == "look":
      if lanternOn == True and rubbleCleared == False:
        islooking = True
        look(currentlocation, lanternOn)
      else:
        look(currentlocation, lanternOn)
    elif userinput == "take":
      print()
      print("Nothing to take.")
      print()
    elif userinput == "use":
      x = openInventory(userinput)
      if x == "nothing" or x == "Nothing":
        print()
      elif x == "lantern":
        if lanternOn == True:
          print("You extinguish your lantern.")
          lanternOn = False
          print()
        else:
          print("You light your lantern.")
          lanternOn = True
          print()
      elif x == "pickaxe" and inventory[2] == "pickaxe":
        if islooking == True and lanternOn == True:
          print("You swing you pickaxe at the rubble repeatedly. The rock chips and breaks to so that you can easily use your hands to clear away the excess stone. After some time the gap is just big enough to walk through.")
          print()
          amuletRoom()
          break
        else:
          print("You don't know where you should use the pickaxe.")
          print()
      else:
        print()
        print("You can't use that here.")
        print()
    elif userinput == "help":
      commands()
    elif userinput == "continue":
      print()
      print("You cannot continue, there is no where else to go but here.")
      print()
    if islooking == True and inventory[2] == "Nothing":
      print()
      print("Your mind begins to race as you realize that your only two paths for escape are completely blocked off. You run as fast as you can back towards the entrance, and begin pounding at the rubble with your axe. It does nothing, so instead you get on")
      print("your knees and try clawing at the smaller rocks at the foundation, but all this does is tear and blister your fingers and palms and break your fingernails. In defeat, you collapse on the ground and simply wait for your life to end. Days pass as")
      print("you get weaken, until you are no more.")
      print()
      for x in range(2):
        inventory.append("Nothing")
        inventory.pop(0)
        x += 1
      cabin()
      break


def amuletRoom():
  os.system('cls')
  currentlocation = location[8]
  lanternOn = True
  print("You step through the opening and discover that it is not an exit like you had hoped, but instead a small square stone room with hundreds of red symbols painted on the walls. In the center is an altar with a small wooden box on top, containing an amulet")
  print("with a large red jewel.")
  print()
  while True:
    print()
    print("What would you like to do?")
    userinput = input("")
    userinput = userinput.lower()
    while userinput != "look" and userinput != "take" and userinput != "use" and userinput != "help" and userinput != "continue":
      userinput = input("Try again: ")
    if userinput == "look":
      look(currentlocation, lanternOn)
    elif userinput == "take":
      take(currentlocation)
      print()
    elif userinput == "use":
      x = openInventory(userinput)
      if x == "nothing" or x == "Nothing":
        print()
      elif x == "lantern":
        if lanternOn == True:
          print("You extinguish your lantern.")
          lanternOn = False
          print()
        else:
          print("You light your lantern.")
          lanternOn = True
          print()
      elif x == "amulet" and inventory[3] == "amulet":
        print()
        print("You put on the amulet, and grip the jewel tightly in your fist. You close your eyes and think for a second, then you tear at necklace, breaking its starp and throw it onto the floor. You then crush the jewel with your boot into a fine powder,")
        print("and hear a loud scream, or potentially hundreds of simultaneous screams as it breaks. Suddenly you blink, and your back at your cabin. Your fire crackles loudly as the fresh firewood begins to burn. The raindrops tap at your window, soothing your")
        print("mind and its pointless thoughts. You climb into bed and gently close your eyes.")
        print()
        print("THE END!")
        break
      else:
        print()
        print("You can't use that here.")
        print()
    elif userinput == "help":
      commands()
    elif userinput == "continue":
      print()
      print("You cannot continue, there is no where else to go but here.")
      print()


def freezing():
  os.system('cls')
  print()
  print("Without any light you get even more lost. You stray further and further from any sign of human life as your body become more and more numb. Eventually you stop feeling cold, as well as anything at all besides tiredness. You lay down up against a tree")
  print("on top of a pile of snow. You are buried as you freeze to death, and are never seen again.")
  print()
  for x in range(2):
    inventory.append("Nothing")
    inventory.pop(0)
    x += 1
  lanternOn = False