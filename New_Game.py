#Main      
import random
import sys

def welcome():
  
  showInformation("Welcome to: *** Stuck in the Catacombs *** Each time you enter a new room you will be facing north. "
  "When presented with choices you can always use the following commands: "
  "'help' to print this message again, and "
  "'exit' to leave the game.")
  return
  
  
def playerName(player):
  username = requestString("What is your name?")
  player.setName(username)
  showInformation("Hello " + player.getName() + ".")

#to access player name, newName['name']

""" Rooms """

def start(player=None):
  
  welcome()
  matches = Item('matches', 'make fire', 0)
  
  validChoices = ['north']
  #first room in the game needs this
  if player is None:
    player = Player()
    playerName(player)
    player.pickUp(matches)
    
  #make picture for map and player drawings
  map = makeEmptyPicture(500, 500, white)
   
  #draw entry w/ doors
  addLine(map, 210, 485, 210, 500, black)
  addLine(map, 265, 485, 265, 500, black)
  addLine(map, 210, 490, 235, 490, black)
  addLine(map, 240, 490, 265, 490, black)
  addLine(map, 210, 485, 235, 485, black)
  addLine(map, 240, 485, 265, 485, black)
  
  #draw player start
  addOvalFilled(map, 236, 495, 5, 5, black)
  
  #draw
  show(map)
  printNow("While exploring an underground crypt, you find a mysterious door.")
  printNow("Suddenly the ground trembles and there is a cave-in behind you. Your lungs fill with dust and sand, it is hard to breathe.")
  printNow("Finally the cave-in ends, you look back and see nothing but rocks piled up to the ceiling and only a small space around you.")
  printNow("The mysterious door is now your only hope for survival, you must go north through the door.")
  direction = requestString("Which direction would you like to go: ")
  
  #erase player start
  addOvalFilled(map, 236, 495, 5, 5, white)
  
  goDirection(player, 'start', validChoices, direction, map)
  
def entry(player, map):
  
  validChoices = ['north', 'west']
  key = Item('key', 'unlock', 0)
  torch = Item('torch', 'light', 0)
  addLine(map, 180, 485, 210, 485, black)
  addLine(map, 265, 485, 295, 485, black)
  addLine(map, 180, 450, 180, 485, black)
  addLine(map, 180, 285, 180, 400, black)
  addLine(map, 295, 485, 295, 365, black)
  addLine(map, 295, 200, 295, 320, black)
  addLine(map, 180, 100, 180, 235, black)
  addLine(map, 295, 100, 295, 150, black)
  addLine(map, 180, 100, 295, 100, black)
  
  #draw player entry
  addOvalFilled(map, 236, 460, 5, 5, black)
  repaint(map)
  creakingDoor()
  printNow("You are now in the entryway of a dark tunnel, you hear the door slam behind you, the only hope for survival lies ahead.")
  
  if not player.hasItem('torch'):
    printNow("You feel around the dark entryway with your hands, you find a torch on the wall.")
    printNow("You are very happy that you have a box of matches in your pocket")
    choice = requestString("Would you like to take and light the torch? Type yes or no")
    while choice.lower() not in ['yes', 'no']:
      choice = requestString("Please enter a valid response: ")
    if choice.lower() == "yes":
      player.pickUp(torch)
      printNow("You have picked up and lit the torch.")
    elif choice.lower() == "no":
      printNow("Okay. But you may regret it.")
     
  if not player.hasItem('key') and player.hasItem('torch'):
    printNow("Something shiny on the dust covered floor catches your eye.")
    printNow("It is a large golden key.")
    choice = requestString("Would you like to pick up the key? Type yes or no")
    while choice.lower() not in ['yes', 'no']:
      choice = requestString("Please enter a valid response: ")
    if choice.lower() == "yes":
      player.pickUp(key)
      printNow("You have picked up the key.")
    elif choice.lower() == "no":
      printNow("Okay.")
  
  printNow("You may go north further into the tunnel, or go west into the first room.")
  
  
  #erase player entry
  addOvalFilled(map, 236, 460, 5, 5, white)
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'entry', validChoices, direction, map)
  
def tunnel1_front(player, map):
  validChoices = ['north', 'east', 'south']
  
  #draw player front tunnel1
  addOvalFilled(map, 236, 400, 5, 5, black)
  repaint(map)
  Wind1()
  printNow("You are now further into the dark tunnel you feel an ominous cold wind touch your skin.")
  printNow("You smell the stench of dead bodies, you hear the sound of howling wind, and the groans of some sort of creature.")
  printNow("You may go south to retreat, north further into the tunnel, or go east into another room.")
  
  #erase player front tunnel1
  addOvalFilled(map, 236, 400, 5, 5, white)
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'tunnel1_front', validChoices, direction, map)

def tunnel1_middle(player, map):
  validChoices = ['north', 'west', 'south']
  
  #draw player middle tunnel1
  addOvalFilled(map, 236, 275, 5, 5, black)
  repaint(map)
  Wind2()
  printNow("Going further into the tunnel the wind gets colder, the cold runs through you, you can feel down to your bones.")
  printNow("You may go south to retreat, go north further into the tunnel, or go west into a room.")
  
  #erase player middle tunnel1
  addOvalFilled(map, 236, 275, 5, 5, white)
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'tunnel1_middle', validChoices, direction, map)
  
def tunnel1_end(player, map):
  validChoices = ['east', 'south']
  
  #draw player end tunnel1
  addOvalFilled(map, 236, 165, 5, 5, black)
  repaint(map)
  
  printNow("You have reached a dead end, you are freezing cold, and you hear a loud awful terrifying moan.")
  printNow("You may go south back into the tunnel, or go east into a dark room.")
  
  #erase player end tunnel1
  addOvalFilled(map, 236, 165, 5, 5, white)
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'tunnel1_end', validChoices, direction, map)
  
def room1(player, map):
  validChoices = ['north', 'east']
  
  #draw room1
  addLine(map, 50, 450, 180, 450, black)
  addLine(map, 103, 405, 125, 405, black)
  addLine(map, 75, 405, 98, 405, black)
  addLine(map, 50, 400, 98, 400, black)
  addLine(map, 50, 400, 50, 450, black)
  addLine(map, 125, 400, 125, 405, black)
  addLine(map, 75, 400, 75, 405, black)
  addLine(map, 103, 400, 180, 400, black)
  
  #draw player in room1
  addOvalFilled(map, 150, 430, 5, 5, black)
  repaint(map)
   
  #setup an "Item", 
  sword = Item('sword', 'weapon', 80)

  printNow("As you enter the chamber, you stumble on a hole in the floor.")
  printNow("You fall and land in a puddle of putrid water.")
  printNow("Your torch is extinguished and you are now wet, cold and smell like a corpse.")
  printNow("Though you feel you now fit in with the other inhabitants, you are horrified as the darkness envelopes you.")
  printNow("You try to relight your candle, but it is to wet. You cast it aside in hope you will find another one.")
  printNow("You decide it is wise to save your matches in case of a more serious emergency.")
  printNow("You begin to feel around on the ground looking for the walls.")
  printNow("When you find the wall you trace them around the room feeling along the skulls as you go.")
  printNow("Luckily you find what feels like a torch.")
  printNow("You light a match and the torch illuminates the room.")
  printNow("Immediately you notice a suit of armor in the corner.")
  printNow("As you approach you see that dead eyes of the Knights skull inside his helmet.")
  
  if not player.hasItem('sword'):
    printNow("You also notice a bright shinny sword at his side.")
  
    choice = requestString("Would you like to pick up the sword? Type yes or no")
    while choice.lower() not in ['yes', 'no']:
      choice = requestString("Please enter a valid response: ")
    if choice.lower() == "yes":
      player.pickUp(sword)
      printNow("You have picked up the sword.")
    elif choice.lower() == "no":
      printNow("Okay. But you might regret it later.")
  
  printNow("You see a door next to the suit of armor.")
  printNow("You may go north to the door, or go east to return to the tunnel.")
 
  #erase player in room1
  addOvalFilled(map, 150, 430, 5, 5, white)
  
  direction = requestString("Which direction would you like to go: ")
    
  goDirection(player, 'room1', validChoices, direction, map)
  
  
def secret_tomb(player, map):
  validChoices = ['north', 'south']  
  printNow("You step inside the dark tomb and immediately hear a loud groan.")
    
  #draw secret tomb
  addLine(map, 75, 285, 75, 400, black)
  addLine(map, 125, 285, 125, 400, black) 
   
  #draw player in secret tomb
  addOvalFilled(map, 100, 380, 5, 5, black)
  repaint(map)
  
  #erase player in secret tomb
  addOvalFilled(map, 100, 380, 5, 5, white)
  
  if not player.inHistory('killed_mummy'):
    printNow("Suddenly a Mummy appears. Its threads hang about its body in tatters.")
    printNow("You realize that it will kill you if you don't do something quickly.")
    choice = requestString("Do you want to fight or run? Type fight or run")
    while choice.lower() not in ['fight', 'run']:
      choice = requestString("Please enter a valid response: ")
    if response == 'fight':
      printNow("You have:")
      player.listItems()
      response = requestString("Pick an item by name to use as a weapon.")
      if not player.hasItem(response.lower()):
        printNow("You don't have that item. It's now to late to find another, you will have to fight bare handed")
        
        # call fight control
        fightControl(player, 0, 'Mummy', 25)
        
      else:
        item = player.useItem(response.lower())
        
        # call fight control
        fightControl(player, item.getStrength(), 'Mummy', 25)
          
      if player.getHealth() < 1:
        sys.exit("Sorry, " + player.getName() + " you lose!")
      else: 
        player.addHistory("killed_mummy")
        printNow("You have killed the mummy! Good job!") 
        printNow("You may continue north and exit the secret tomb, or south to return.")
        direction = requestString("Which direction would you like to go: ")
        goDirection(player, 'secret_tomb', validChoices, direction, map)
    else:
      sys.exit("The Mummy is fast, he runs you down and kills you. Sorry " + player.getName() + " you lose!")
  
  
def room2(player, map):
  validChoices = ['west', 'north']
  #draw room2
  addLine(map, 295, 365, 420, 365, black)
  addLine(map, 295, 320, 370, 320, black)
  
  #draw player in room2
  addOvalFilled(map, 340, 340, 5, 5, black)
  repaint(map)
  printNow("You have entered a dark musty chamber about the size of a childs bedroom.")
  printNow("The air is heavy and smells of rotten flesh.")
  printNow("You hear small creatures rustling around and the sound of water dripping.")
  printNow ("You have discovered a small opening in the wall. It seems to lead to some sort of passage way.")
  printNow("You may go north into the passage way, or west to return to the main tunnel.")
  #erase player in room2
  addOvalFilled(map, 340, 340, 5, 5, white)
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'room3', validChoices, direction, map)
  



def room3(player, map):
  validChoices = ['west', 'north']  
  
  #draw room3
  addLine(map, 295, 150, 310, 150, black)
  addLine(map, 340, 150, 420, 150, black)
  addLine(map, 295, 200, 370, 200, black)
  
  #draw player in room3
  addOvalFilled(map, 340, 170, 5, 5, black)
  repaint(map)
  
  printNow ("You have entered into a large dome shaped catacomb. It is cold, hummid, and dusty.")
  printNow ("There does not seem to be anything in room other then large cloumbs of skulls stacked on both the right and left of you.")
  printNow ("You have descovered a small opening in the wall. It seems to lead to another tunnel.")
  printNow("You may go north into the newly discovered tunnel or west back into the main tunnel.")
  #erase player in room3
  addOvalFilled(map, 340, 170, 5, 5, white)
  
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'room3', validChoices, direction, map)
       
  
def room4(player, map):
  #function for room 4
  validChoices = ['east', 'north']   #west moves player back to main hall, north brings player to tunnel 2.
  #draw room4
  addLine(map, 103, 285, 180, 285, black)
  addLine(map, 20, 285, 98, 285, black)
  addLine(map, 20, 235, 75, 235, black)
  addLine(map, 125, 235, 180, 235, black)
  addLine(map, 20, 235, 20, 285, black)
  addLine(map, 75, 280, 75, 285, black)
  addLine(map, 125, 280, 125, 285, black)
  addLine(map, 75, 280, 98, 280, black)
  addLine(map, 103, 280, 125, 280, black)
  
  #draw player in room4
  addOvalFilled(map, 100, 255, 5, 5, black)
  repaint(map)
    
  printNow ("You have entered into a small stuffy catacomb. It is dark and cold.")
  printNow ("It is small and crampped. The ceiling is low and there is not much ")
  printNow ("room to move around. To the west side of the room, there is nothing")
  printNow ("but a bunch of old stacked bones.... There is also an old stone carving")
  printNow ("which says 'TU VAS MOURIR'.") #This means you will die in french. Is this a french catacomb? lol. I didnt know...
  printNow ("You have descovered a small opening in the wall. It seems to lead to another tunnel.")
  printNow("You may go north into the newly discovered tunnel or east back into the main tunnel.")
  
  #erase player in room4
  addOvalFilled(map, 100, 255, 5, 5, white)
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'room4', validChoices, direction, map)
  
  
  
def passage_way(player, map):
  validChoices = ['south', 'north']  
  
  #draw passageway1
  addLine(map, 370, 200, 370, 320, black)
  addLine(map, 420, 150, 420, 365, black)
  
  #draw player in passageway1
  addOvalFilled(map, 390, 260, 5, 5, black)
  repaint(map)
  
  printNow ("You begin to crawl inside. Bones snap and crack underneath your")
  printNow ("hands and knees. The shards of broken bone push threw the surface of your skin.")
  printNow ("You feel a hudge wave of anxiety, filling you stomach with an empty pit.")
  printNow ("Your heart begins to race. You have reached half way in the tunnel and see an opening at the other end.")
  printNow ("But now you begin to wounder.... 'Should I turn back?'")
  printNow("You can go south to turn back, or north to continue through the opening.")
  direction = requestString("Which direction would you like to go: ")
  
  #erase player in passageway1
  addOvalFilled(map, 390, 260, 5, 5, white)
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'passage_way', validChoices, direction, map)
           
def tunnel2_west():
  validChoices = ['south', 'north']  
  addLine(map, 340, 15, 340, 150, black)
  addLine(map, 310, 50, 310, 150, black)
  addLine(map, 125, 50, 310, 50, black)
  addLine(map, 340, 15, 265, 15, black)
  addLine(map, 75, 15, 210, 15, black)
  addLine(map, 75, 15, 75, 235, black)
  addLine(map, 125, 50, 125, 235, black)
  
  #draw player in west tunnel2
  addOvalFilled(map, 100, 130, 5, 5, black)
  repaint(map)
  
  printNow("You have entered a large arched tunnel, it is dry in here.")
  printNow("You can see a small amount of light ahead, you let out a huge sigh of relief.")
  printNow("Finally you may have found the way out, but your relief is broken by a loud groan.")
  printNow("You can't imagine what lies ahead and what made that groan.")
  printNow("You may go north to continue ahead, and south to go back to the room.")
  
  #erase player in west tunnel2
  addOvalFilled(map, 100, 130, 5, 5, white)
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'tunnel2_west', validChoices, direction, map)
  
def tunnel2_east():
  validChoices = ['south', 'north']  
  addLine(map, 340, 15, 340, 150, black)
  addLine(map, 310, 50, 310, 150, black)
  addLine(map, 125, 50, 310, 50, black)
  addLine(map, 340, 15, 265, 15, black)
  addLine(map, 75, 15, 210, 15, black)
  addLine(map, 75, 15, 75, 235, black)
  addLine(map, 125, 50, 125, 235, black)
  
  #draw player in east tunnel2
  addOvalFilled(map, 325, 100, 5, 5, black)
  repaint(map)
  
  printNow("You have entered a large arched tunnel, it is dry in here.")
  printNow("You can see a small amount of light ahead, you let out a huge sigh of relief.")
  printNow("Finally you may have found the way out, but your relief is broken by a loud groan.")
  printNow("You can't imagine what lies ahead and what made that groan.")
  printNow("You may go north to continue ahead, and south to go back to the room.")
    
  #erase player in east tunnel2
  addOvalFilled(map, 325, 100, 5, 5, white)
  direction = requestString("Which direction would you like to go: ")
  goDirection(player, 'tunnel2_east', validChoices, direction, map)
  
def tunnel2_exit():
  validChoices = ['north'] 
  #draw exit w/ doors
  addLine(map, 210, 15, 210, 0, black)
  addLine(map, 265, 15, 265, 0, black)
  addLine(map, 210, 10, 235, 10, black)
  addLine(map, 240, 10, 265, 10, black)
  addLine(map, 210, 15, 235, 15, black)
  addLine(map, 240, 15, 265, 15, black)
  
  #draw player at exit 
  addOvalFilled(map, 235, 35, 5, 5, black)
  repaint(map)
  
  battle_axe = Item('battle axe', 'weapon', 89)
  
  if not player.hasItem('battle axe'):
    printNow("As you enter, you see an ancient battle axe hanging on the wall.")
    choice = requestString("Would you like to pick up the battle axe? Type yes or no")
    while choice.lower() not in ['yes', 'no']:
      choice = requestString("Please enter a valid response: ")
    if choice.lower() == "yes":
      player.pickUp(battle_axe)
      printNow("You have picked up the battle axe.")
    elif choice.lower() == "no":
      printNow("Okay. But you might regret it later.")
  printNow("You approach the small beam of light you saw, there appears to be a door with light shining through the edges.")
  printNow("Finally, you start to go toward the door, but suddenly a zombie appears in front of the door.")
  printNow("The zombie stinks like rotting flesh, the stench makes you want to vomit.")
  printNow("You hear the zombie utter, 'I want your brains', you know in order to get to the door you will have to fight off the zombie.")
  choice = requestString("Did you come all this way to fail now, will you fight the zombie or run? : Type fight or run")
  
  while choice.lower() not in ['fight', 'run']:
    choice = requestString("Please enter a valid response: ")
    if response == 'fight':
      printNow("You have:")
      player.listItems()
      response = requestString("Pick an item by name to use as a weapon.")
      if not player.hasItem(response.lower()):
        printNow("You don't have that item. It's now to late to find another, you will have to fight bare handed")
        
        # call fight control
        fightControl(player, 0, 'Zombie', 35)
        
      else:
        item = player.useItem(response.lower())
        
        # call fight control
        fightControl(player, item.getStrength(), 'Zombie', 35)
          
      if player.getHealth() < 1:
        sys.exit("Sorry, " + player.getName() + " you lose!")
      else: 
        player.addHistory("killed_zombie")
        printNow("You have killed the zombie! Good job!") 
        printNow("You may continue north and exit the catacombs.")
        direction = requestString("Which direction would you like to go: ")
        #erase player at exit 
        addOvalFilled(map, 235, 35, 5, 5, white)
        goDirection(player, 'tunnel2_exit', validChoices, direction, map)
    else:
      sys.exit("The Zombie is too fast, he runs you down and kills you. Sorry " + player.getName() + " you lose!")


"""function goDirection keeps track of the player allowed directions and checks their validity 
it also keeps track of doors and contains the win and lose conditions"""


def goDirection(player, roomName, validChoices, playerChoice, map):

  choices = ['help', 'exit']
  choices.extend(validChoices)

  while playerChoice.lower() not in choices:
    playerChoice = requestString("Please enter a valid direction: ")
  
  if playerChoice.lower() == "help":
    welcome()
    
  if playerChoice.lower() == "exit":  
    sys.exit("Goodbye. Thank you for playing.")
      
  if roomName == 'start':
    if playerChoice.lower() == "north":
      entry(player, map)
      
  #entry choices here
  elif roomName == 'entry':
    if playerChoice.lower() == "north":
      tunnel1_front(player, map)
    elif playerChoice.lower() == "west":
      room1(player, map)
  
  elif roomName == 'tunnel1_front':
    if playerChoice.lower() == "north":
      tunnel1_middle(player, map)
    elif playerChoice.lower() == "east":
      room2(player, map)
    elif playerChoice.lower() == "south":
      entry(player, map)
  
  elif roomName == 'tunnel1_middle':
    if playerChoice.lower() == "north":
      tunnel1_end(player, map)
    elif playerChoice.lower() == "west":
      room4(player, map)
    elif playerChoice.lower() == "south":
      tunnel1_front(player, map)
  
  elif roomName == 'tunnel1_end':
    if playerChoice.lower() == "south":
      tunnel1_middle(player, map)
    elif playerChoice.lower() == "east":
      room3(player, map)
   
      
  # room1 choices here 
  elif roomName == "room1":
    if playerChoice.lower() == "east":
      entry(player, map)
    elif playerChoice.lower() == "north":
      #draw player at entry of secret tomb
      addOvalFilled(map, 100, 410, 5, 5, black)
      repaint(map)
      printNow("The door is locked")
      if player.hasItem('key'):
        choice = requestString("Would you like to use the key? Type yes or no: ")
        while choice.lower() != "yes" and choice.lower() != "no":
          choice = requestString("Please enter a valid response: ")
        if choice.lower() == 'yes':
          if player.useItem('key') == 'unlock':
            printNow("You have opened the door to a secret tomb.")
            #erase player at entry of secret tomb
            addOvalFilled(map, 100, 410, 5, 5, white)
            secret_tomb(player, map)
        elif choice.lower() == 'no':
          printNow("Okay, returning to room.")
          room1(player, map)
      else:
        printNow("You do not have the key.")
        printNow("Returning to the room.")
        room1(player, map)
      #erase player at entry of secret tomb
      addOvalFilled(map, 100, 410, 5, 5, white)
  
  elif roomName == 'secret_tomb':
    if playerChoice.lower() == "north":
      printNow("The door slams and disappears into the wall behind you. There is no going back.")
      creakingDoor()
      room4(player, map)
    elif playerChoice.lower() == "south":
      secret_tomb(player, map)
      
  # room2 choices here
  elif roomName == 'room2':
    if playerChoice.lower() == "north":
      doorGame(player, map)
    elif playerChoice.lower() == "west":
      tunnel1_front(player, map)
      
      
  # room3 choices here
  elif roomName == 'room3':
    if playerChoice.lower() == "north":
      tunnel2_east(player, map)
    elif playerChoice.lower() == "west":
      tunnel1_end(player, map)
       
  # room4 choices here
  elif roomName == 'room4':
    if playerChoice.lower() == "north":
      tunnel2_west(player, map)  
    if playerChoice.lower() == "east":
      tunnel1_middle(player, map)  
      
  # tunnel2 west choices here
  elif roomName == 'tunnel2_west':
    if playerChoice.lower() == "north":
      tunnel2_exit(player, map)  
    if playerChoice.lower() == "south":
      room4(player, map)  
      
  # tunnel 2 east choices here
  elif roomName == 'tunnel2_east':
    if playerChoice.lower() == "north":
      tunnel2_exit(player, map)  
    if playerChoice.lower() == "south":
      room3(player, map)  
      
  elif roomName == 'tunnel2_exit':
    if playerChoice.lower() == "north":
        #draw player after exit at end
        addOvalFilled(map, 235, 5, 5, 5, black)
        repaint(map)
        creakingDoor()
        showInformation("Congratulations, " + player.getName() + " you have WON!!!")
     
   
 #Passage way choices here
  elif roomName == 'passage_way':
    if playerChoice.lower() == "south":
      printNow ("\nYou have decided to turn back.\n")
      room2(player, map)
    if playerChoice.lower() == "north":
      printNow("\nYou decided to move forward and now you have reached the end of the passage way.")
      printNow("You continue through the opening at the end of the tunnel into a room.")
      printNow("The passage way collapses behind you, you are safe, but you cannot go back.")
      room3(player, map)
      
                               
def fightControl(player, strength, monster, penalty):
  while not fight(strength):
    printNow("You strick the "+monster+", but the "+monster+" strikes back")
    player.decrementHealth(penalty)
    printNow("You have lost "+str(penalty)+" health points")
    if player.getHealth() < 1:
      return
    printNow("You have "+ str(player.getHealth()) +" health points left.")
  return

def fight(weaponStrength):
  
  fightScore = random.randint(weaponStrength, 100)
  
  if fightScore > 90:
    return True
    
  return False
  
            
  
"""Class Item represents items in the game"""
class Item:
  name = None
  action = None
  strength = 0
  
  def __init__(self, name, action, strength=0):
    self.name = name
    self.action = action
    self.strength = strength
  
  """Method getName returns string name of an item"""
  def getName(self):
    return self.name
  
  """Method getAction returns string action of an item"""
  def getAction(self):
    return self.action
    
  """Method getStrength returns numeric strength of an item"""
  def getStrength(self):
    return self.strength

"""Class Player represents players in the game"""
class Player:
  
  def __init__(self):
    self.trackHistory = []
    self.knapsack = [];
    self.health = 100
  
  """Method setName player's name"""
  def setName(self, name=None):
    self.name = name

  """Method getName return player's name"""
  def getName(self):
      return self.name
  
  """Method pickUp adds item to player knapsack"""
  def pickUp(self, item):
    self.knapsack.append(item)

  """Method hasItem return bolean if player has item with name"""
  def hasItem(self, name):
    for item in self.knapsack:
      if item.getName() == name:
        return True
    return False

  """Method discardItem remove an item from player knapsack"""
  def discardItem(self, item):
    count = 0
    for item in self.knapsack:
      if item.getName() == name:
        self.knapsack.pop(count) 
      count = count + 1

  """Method useItem use an item from player knapsack"""
  def useItem(self, name):
    for item in self.knapsack:
      if item.getName() == name:  
        return item

  """Method listItems list items in player knapsack"""
  def listItems(self):
    for item in self.knapsack:
      if item is not None:
        printNow(item.getName() + ", cabability: " + item.getAction())
    return

  """Method decrementHealth lose heath points"""
  def decrementHealth(self, loss):
    self.health = self.health - loss
    return  

  """Method getHealth return heath points"""
  def getHealth(self):
    return self.health
    
  """Method addHistory adds a note to a players history"""  
  def addHistory(self, note):
    self.trackHistory.append(note)
    
  """Method inHistory check if a note is in a players history"""    
  def inHistory(self, note):
    return (note in self.trackHistory)
      
       
         
def doorGame(player, map):
#mini Game to open passageway function
                     
  hiddenWord = "matchstick"                                      #Secret Word: Can be changed to anything you like and will still work!
  wordDashes = "?" * len(hiddenWord)                             #Display dashes for secret word                                       
  guessedLetters = ""                                            #holds on to the guessed letters 
  correctLetters = 0                                             #correct letters incriminator 
  wrongAnswers = 0                                               #Holds wrong letter incriminator
  quitGame = false 
  possibleLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  
  #Game Logic
  printNow("\n You approach the passage way, when suddenly a rolling grey fog begins to form in front of the opening.")
  printNow("The fog starts to cluster and take the form of a old, weathered woman. Through the fog, her face takes")
  printNow("form. Her eyes are black, void of any light. Suddenly she speaks. Her voice is soft and chilling... 'Foolish mortal, it appears you have")
  printNow("fallen into my trap....' You begin to feel your own heart begin to beat out of your chest. 'You look")
  printNow("frightened.... good! But there is hope for you see... just answer my question and you can go free...")
  printNow("'And because I am so generous I will even help you! You can guess letters to the answer and I will tell")
  printNow("you if your getting close.....")
  printNow("However, if you guess more than five letter incorrectly..... well.... ha ha ha....'")
  printNow("\n 'Ready? Tear one off and scratch my head what was red is black instead! WHAT AM I!'")
  printNow(wordDashes) 
  quiteGame  = false                                        #Displays the proper - of hiddenWord

  while quitGame == false :
     guessedLetter = requestString("What letter do you think is in the answer?." )  
     guessedLetter = guessedLetter.lower()   
     
     #error Checking for user input, exit feature, end game logic...
     if guessedLetter == "quit":
       quitGame = true
     if len(guessedLetter) != 1:
       printNow("Stupid mortal, ha! That is too many letters....")
       printNow("I won't count this one against you!")
     elif guessedLetter in guessedLetters:
       printNow("Stupid mortal, ha! You have already guessed that letter....")
       printNow("I won't count this one against you!")
     elif guessedLetter not in possibleLetters:
       printNow("You begin to lose your concentration. That's not a letter")
     elif wrongAnswers >= 5:
       sys.exit("The spirit laughs...Suddenly the floor opens and drops you to your death... SORRY " + player.getName() + " YOU LOSE!")
     else:
       printNow("You guessed: " + guessedLetter)
       guessedLetters = guessedLetter + guessedLetters

      
       #if guessed letter is correct
       if guessedLetter in hiddenWord:
         guessedLetters = guessedLetters + guessedLetter
         printNow("\nYou are getting close mortal! '" + guessedLetter + "' is in the answer\n")
         #Begin to display word Dashes...
         for i in range(len(hiddenWord)):
           if guessedLetter in hiddenWord[i]: 
             wordDashes = wordDashes[:i] + hiddenWord[i] + wordDashes[i+1:] #travels through the array and splices string to correct letter in index i..
             correctLetters = correctLetters + 1                                                          #then moves to the next even index using times x2. This keeps the blank spaces... 
         printNow(wordDashes)
       
       #Wrong Answer Logic
       else:
           wrongAnswers = wrongAnswers + 1
           printNow("'HAHAHAHAHA! That's wrong!'")
           printNow ("'The question is... Tear one off and scratch my head what was red is black instead! WHAT AM I!'")
           printNow(wordDashes)   
                      
     #Winning statement: 
     if correctLetters== len(hiddenWord):
       printNow("Suddenly the spirit screams! \n 'AHHHHHH!' \n Then disappears, leaving the room like it once was before.")
       printNow("The correct answer was:  " + hiddenWord)
       printNow("You place a burning match in the skulls mouth, and")
       printNow("The catacomb wall begins to shake...")
       printNow("You are now allowed into the passage way....")
       passage_way(player, map)

start()

def creakingDoor():
   file = "cst205Final/sounds/Creaking Door.wav" 
   sound = makeSound(file)
   for sample in getSamples(sound):
      value  = getSampleValue(sample)
      setSampleValue(sample, value * 6 )
   play(sound)

def Wind1():
   file = "cst205Final/sounds/wind.wav" 
   sound = makeSound(file)
   for sample in getSamples(sound):
      value  = getSampleValue(sample)
      setSampleValue(sample, value * 8 )
   play(sound)

def Wind2():
   file = "cst205Final/sounds/wind2.wav" 
   sound = makeSound(file)
   for sample in getSamples(sound):
     value  = getSampleValue(sample)
     setSampleValue(sample, value * 8 )
   play(sound)

