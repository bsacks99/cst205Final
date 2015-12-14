
#Main      
import random
import sys
import os

doorOpened = false  #Global variable for gmae. Not sure if you guy want to change this logic. Ok with whatever u decide!:)

def welcome():
  Hell_Intro()
  printNow("Welcome to:")
  printNow("*** Stuck in the Catacombs ***")
  printNow("When presented with choices you can always use the following commands:")
  printNow("'help', to print this message again")
  printNow("'exit', to leave the game")
  return
  
""" Rooms """
def entry(player=None):

  #first room in the game needs this
  if player is None:
    player = Player()
    
  # setup your valid directional choices for this room
  validChoices = ['north', 'east', 'west','south']
  showInformation("You have entered a courtyard in a from  the back of an alley, there's a door on your left,a Fire ladder on right a Dead end behind you, and a creepy clown with a rusty meat cleaver covered in blood in front of you, which way do you want to go?")
  if doorOpened == false:
    goDirection(player, room3, validChoices, direction)
  elif doorOpened == true:
    goDirection(player, 'entry', validChoices, direction)
    
def tunnel1(player):
  #function for tunnel1
  creakingDoor()
  Wind2()
  zombie_quite()
  printNow("You are a dank tunnel with an ominous wind,with the stench of dead bodies, you hear the sound of howling wind,and groans ofsome sort of creature")
  validChoices = ['north', 'east', 'south','west']   # player enters the main corridor  they can go north, east, south, west
  #If door isnt opened
  if doorOpened == false:
    printNow("There is a door on the left,choose your direction") 
    goDirection(player, room3, validChoices, direction)
  #If user Chooses to go into the first room or further navigate tunnel
  elif doorOpened == true:
    goDirection(player, tunnel1, validChoices, direction)
  else:
    printNow("Choose a direction")
    
def tunnel1_2(player):
  #function for tunnel1_2
  Wind2()
  zombie_L1()
  printNow("You further along in the dank tunnel with an ominous wind,with the stench of dead bodies, you hear the sound of howling wind,and groans ofsome sort of creature")
  printNow("you have a door on your right, and a dark tunnel ahead, which way wouldyou like to go?")
  validChoices = ['north','east', 'south']   # player is in the main corridor  they can go north, east, or south
  #If door isnt opened
  if doorOpened == false:
    printNow(" Choose your direction") 
    goDirection(player, room3, validChoices, direction)
  #If user Chooses to go into the first room or further navigate tunnel
  elif doorOpened == true:
    goDirection(player, tunnel1_2, validChoices, direction)
  else:
    printNow("Choose your direction")

def tunnel1_3(player):
  #function for tunnel1_3
  Wind2()
  zombie_L2()
  printNow("You further along in the dank tunnel with an ominous wind,with the stench of dead bodies, you hear the sound of howling wind,and groans of some sort of creature")
  printNow("you have a door on your left, and a dark tunnel ahead, which way would you like to go?")
  validChoices = ['north','west', 'south']   # player is in the main corridor  they can go north, west, or south
  #If door isnt opened
  if doorOpened == false:
    printNow(" Choose your direction") 
    goDirection(player, room3, validChoices, direction)
  #If user Chooses to go into the first room or further navigate tunnel
  elif doorOpened == true:
    goDirection(player, tunnel1_3, validChoices, direction)
  else:
    printNow("Choose your direction" )    

def room1(player=None):
  creakingDoor()
  Wind1()
  #first room in the game needs this
  if player is None:
    player = Player()
    
  # setup your valid directional choices for this room
  validChoices = ['south']

  printNow("You have entered a dark musty chamber about the size of a childs bedroom.")
  
  printNow("The air is heavy and smells of rotten flesh.")
  printNow("You hear small creatures rustling around and the sound of water dripping.")
  
  # if player has torch
  printNow("As you move your torch around you notice a pile of bones in center of the room as tall as you are.")
  
  printNow("As you make your way further into the room you notice, in the faint light, that the walls are lined with skulls.")
  printNow("A deep chill enters your body and shakes you to your core.")
  
  printNow("You you see a doorway to your south. It is the only direction you can travel.")
  direction = requestString("Which direction would you like to go: ")
  
  goDirection(player, 'room1', validChoices, direction)
 

  
def room2(player):
  creakingDoor()
  Wind1()
  # setup your valid directional choices for this room
  validChoices = ['north']
  
  # setup an "Item", 
  sword = Item('sword', 'weapon', 80)


  printNow("As you enter the chamber, you stumble on a hole in the foor.")
  
  printNow("You fall and land in a puddle of putrid water.")
  printNow("Your torch is extinguished and you are now wet, cold and smell like a corps.")
  
  printNow("Though you feel you now fit in with the other inhabitants, you are horrified as the darkness envelopes you.")
  printNow("You try to re-light your candle, but it is to wet. You cast it asside in hope you will find another one.")
  printNow("You decide it is wise to save your matches in case of a more serous emergency.")
  printNow("You begin to feel around on the ground looking for the walls.")
  printNow("When you find the wall you trace them around the room feeling along the skulls as you go.")
  printNow("Luckily you find what feels like a torch.")
  printNow("You light a match and the torch illuminates the room.")
  
  printNow("Immediately you notice a suit of armor in the corner.")
  printNow("As you approach you see that dead eyes of the Knights skull inside his helmit.")
  
  if not player.hasItem('sword'):
    printNow("You also notice a bright shinny sword at his side.")
  
    response = requestString("Do you want to pick up the sword. (yes or no)")
    response = response.lower()
    if response == 'yes' or response == 'y':
      player.pickUp(sword)
    
  if not player.inHistory('killed_mummy'):
    printNow("Suddenly a Mummy breaks through the wall of skulls. It's threads a hang about it's body in tatters.")
    printNow("You realize that it will kill you if you don't do something quickly.")
    
    response = requestString("Do you want to fight or run? (fight or run)")
    response = response.lower()
    if response == 'fight' or response == 'f':
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
        sys.exit("You lose!")
      else: 
        player.addHistory("killed_mummy")
        printNow("You have killed the mummy! Good job!") 
    else:
      sys.exit("The Mummy is fast, he runs you down and kills you.")
      
  printNow("You you see a doorway to your north. It is the only direction you can travel.")
  direction = requestString("Which direction would you like to go: ")
    
  goDirection(player, 'room2', validChoices, direction)



def room3(player):
  creakingDoor()
  Wind1()
  zombie_L2()
  #function for room 3
  validChoices = ['west', 'south', 'north']   #west moves player back to main hall, south brings playyer to puzzle game, which open passageway.  
  
  #If Door to passageway is closed...
  if doorOpened == false:
    printNow ("\n************************************************************************************")
    printNow ("You have entered into a large dome shaped catacomb. It is cold, hummid, and dusty.")
    printNow ("There does not seem to be anything in room other then large cloumbs of skulls stacked")
    printNow ("on both the right and left of you. In front of you, there seems to be somthing carved")
    printNow ("into the stone.")
    goDirection(player, room3, validChoices, direction)
  #If game is completed and door is open...
  elif doorOpened == true:
    printNow ("You are back into the large dome shaped catacomb. It is cold, hummid, and dusty.")
    printNow ("There does not seem to be anything in room other then large cloumbs of skulls stacked")
    printNow ("on both the right and left of you. In front of you, the skull door appears to be open")
    goDirection(player, room3, validChoices, direction)
  else:
    printNow("Door error: see line 121-135")

       
  
def room4(player):
  creakingDoor()
  Wind2()
  zombie_L2()
  #function for room 4
  validChoices = ['west', 'north']   #west moves player back to main hall, north brings player to tunnel 2.
  printNow ("\n************************************************************************************")
  printNow ("You have entered into a small stuffy catacomb. It is dark and cold.")
  printNow ("it is small and crampped. The celing is low and there is not much ")
  printNow ("room to move around. To the west side of the room, there is nothing")
  printNow ("but a bunch of old stacked bones.... There is also an old stone carving")
  printNow ("which says 'TU VAS MOURIR'.") #This means you will die in french. Is this a french catacomb? lol. I didnt know...
  goDirection(player, room4, validChoices, direction)
  
  
  
def passageWay1(player):
  #function for passage way 1. 
  Wind2()
  validChoices = ['south', 'north']  #South: room 2; Norht: Back to room 3
  printNow ("\n************************************************************************************")
  printNow ("You have descovered a small opening in the wall. It seems to lead to some sort of")
  printNow ("passage way. You begin to crawl inside. Bones snap and crack underneath your")
  printNow ("hands and knees. The shards of broken bone push threw the surface of your skin.")
  printNow ("You feel a hudge wave of anxiety, filling you stomach with an epmpty pit.")
  printNow ("Your heart begins to race. You have reached half way in the tunnel and now you")
  printNow ("begin to wounder.... 'Should I turn back?'")
  goDirection(player, room4, validChoices, direction)
           
                  
"""function goDirection keeps track of the player allowed directions and checks their validity 
it also keeps track of doors and contains the win and lose conditions"""


def goDirection(player, roomName, validChoices, playerChoice):

  choices = ['help', 'exit']
  choices.extend(validChoices)

  while playerChoice.lower() not in choices:
    playerChoice = requestString("Please enter a valid direction: ")
  
  if playerChoice.lower() == "help":
    welcome()
    
  if playerChoice.lower() == "exit":  
    sys.exit("Goodbye. Thank you for playing.")
      
  # Entry choices here 
  elif roomName == 'entry':
    if doorOpened == false: 
      if playerChoice.lower() == "north":
        clown()
        showInformation("Hey Bud I'm looking for a Halloween Party, Do you know where 317 Spooner St is? But hey why you can't go this way!")
        entry(player)
      if playerChoice.lower() == "south":
        showInformation("Thats a Dead end behind you, you can't go that way!")
        entry(player=None)
      if playerChoice.lower() == "east":
         showInformation("Thats a fire ladder, you can't go that way!")
         entry(player)
    else:
      if playerChoice.lower() == "west":
        tunnel1(player)
        
  #tunnel1 choices
  elif roomName == 'tunnel1':
    if doorOpened == false: 
      if playerChoice.lower() == "south":
         playerChoice = requestString("Do you want to restart the game: Select Yes ('Y') or No('N')")
         if (playerChoice.lower()== "yes") or (playerChoice.lower() == "y"):
           entry()
         elif (playerChoice.lower()== "no") or (playerChoice.lower() == "n"):
           tunnel1()
    else:
      if playerChoice.lower() == "west":
        room1(player)
      if playerChoice.lower() == "north":
        playerChoice = requestString("Which way do you want to go?")
        if playerChoice.lower() == "north":
          tunne11_2(player)
      else:
        printNow("you can only go north")
        
  # tunnel1_2 choices
  elif roomName == 'tunnel1_2':
    if doorOpened == false: 
      if playerChoice.lower() == "south":
        tunnel1(player)
      elif playerChoice.lower() == "east":
        room2(player)
      elif playerChoice.lower() == "north":
         tunne11_3(player)
      else:
         printNow("you can only go north") 
         
  # tunnel1_3 choices
  elif roomName == 'tunnel1_3':
    if doorOpened == false: 
      if playerChoice.lower() == "south":
        tunnel1_2(player)
      elif playerChoice.lower() == "east":
        printNow("You Can't go that way")        
      elif playerChoice.lower() == "west":
        room4(player)
      elif playerChoice.lower() == "north":
         tunne11_4(player)
      else:
         printNow("choose a direction") 
         
  # tunnel1_4 choices
  elif roomName == 'tunnel1_4':
    if doorOpened == false: 
      if playerChoice.lower() == "south":
        tunnel1_4(player)
      elif playerChoice.lower() == "west":
        printNow("You Can't go that way")  
      elif playerChoice.lower() == "north":
        printNow("You Can't go that way") 
      elif playerChoice.lower() == "east":
        room3(player)
      
      else:
         printNow("choose a direction") 
  #Room 1 Choices here  
  if roomName == 'room1':
    if playerChoice.lower() == "south":
      room2(player)
      
  # room2 choices here
  elif roomName == 'room2':
    if playerChoice.lower() == "north":
      room1(player)
    
      
      
  # room3 choices here
  elif roomName == 'room3':
    if "doorOpen" not in self.trackHistory: 
      if playerChoice.lower() == "south":
        doorGame()
      if playerChoice.lower() == "north":
        tunnel2(player)
      if playerChoice.lower() == "west":
        tunnel1(player)
    else:
      if playerChoice.lower() == "south":
        passageWay1(player)
      if playerChoice.lower() == "north":
        tunnel2(player)
      if playerChoice.lower() == "west":
        tunnel1(player)
       
  # room4 choices here
  elif roomName == 'room4':
    if playerChoice.lower() == "north":
      tunnel2(player)  
    if playerChoice.lower() == "east":
      tunnel1(player)  
   
  #Passage way 1 choices here
  elif roomName == 'passage way one' :
    if playerChoice.lower() == "north":
      printNow ("\nYou have decided to turn back\n")
      room3(player)
    if playerChoice.lower() == "south":
      printNow("\nYou decided to move forward and now you have reached the end of the tunnel.\n")
      room2(player)


#***************************Fight***Logic*************************************************

                               
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
    self.name = ''
  

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
      
       
         
def doorGame():
#mini Game to open passageway function
                     
  hiddenWord = "matchstick"                                      #Secret Word: Can be changed to anything you like and will still work!
  wordDashes = "?" * len(hiddenWord)                             #Display dashes for secret word                                       
  guessedLetters = ""                                            #holds on to the guessed letters 
  correctLetters = 0                                             #correct letters incriminator 
  wrongAnswers = 0                                               #Holds wrong letter incriminator
  quitGame = false 
  possibleLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  
  #Game Logic
  printNow("\n You approach the wall, when suddenly a rolling grey fog begins to form in front of the door.")
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
       printNow("Stupid mortal, ha! That to many letters....")
       printNow("I won't count this one against you!")
     elif guessedLetter in guessedLetters:
       printNow("Stupid mortal, ha! You have already guessed that letter....")
       printNow("I won't count this one against you!")
     elif guessedLetter not in possibleLetters:
       printNow("You begin to lose your concentration. That's not a letter")
     elif wrongAnswers >= 5:
       sys.exit("The spirit laughs...Suddenly the floor opens and drops you to your death... YOU LOOSE!")
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
             correctLetters = correctLetters + 1 #then moves to the next even index using times x2. This keeps the blank spaces... 
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
       printNow("You have opened a door....")
       self.trackHistory.append(doorOpen)
       
       
       
       
#***************************Sound***Logic*************************************************
def creakingDoor():
   file = os.path.dirname(os.path.realpath(__file__)) + "sounds/Creaking Door.wav" 
   sound = makeSound(file)
   for sample in getSamples(sound):
      value  = getSampleValue(sample)
      setSampleValue(sample, value * 6 )
   play(sound)

def Wind1():
   file = "sounds/wind.wav" 
   sound = makeSound(file)
   for sample in getSamples(sound):
      value  = getSampleValue(sample)
      setSampleValue(sample, value * 8 )
   play(sound)
   
def Wind2():
   file = "sounds/wind2.wav" 
   sound = makeSound(file)
   for sample in getSamples(sound):
     value  = getSampleValue(sample)
     setSampleValue(sample, value * 8 )
   play(sound)
def clown(): #Plays Clown at normal sample value
  file = "sounds/cackle1PreMod.wav"
  sound = makeSound(file)
  for sample in getSamples(sound):
     value = getSampleValue(sample)
     setSampleValue(sample , value)
  play(sound)
  
def zombie_quite():
  file = "sounds/I Want Brains.wav"
  sound = makeSound(file)
  for sample in getSamples(sound):
     value = getSampleValue(sample)
     setSampleValue(sample , value)
  play(sound)
  
def zombie_L1():
  file = "sounds/I Want Brains.wav"
  sound = makeSound(file)
  for sample in getSamples(sound):
     value = getSampleValue(sample)
     setSampleValue(sample , value * 5)
  play(sound) 
  
def zombie_L2():
  file = "sounds/I Want Brains.wav"
  sound = makeSound(file)
  for sample in getSamples(sound):
     value = getSampleValue(sample)
     setSampleValue(sample , value * 7)
  play(sound)

def zombie_L3():
  file = "sounds/I Want Brains.wav"
  sound = makeSound(file)
  for sample in getSamples(sound):
     value = getSampleValue(sample)
     setSampleValue(sample , value * 10)
  play(sound)   
def Heart_Beatsound_reg(): #heart beat sound
  file = "sounds/heartbeat.wav"
  sound = makeSound(file) 
  for sample in getSamples(sound):
     value = getSampleValue(sample)
     setSampleValue(sample, value * 20)
  play(sound)
  
def intro():
   file = "sounds/intro.wav" 
   sound = makeSound(file)
   for sample in getSamples(sound):
      value  = getSampleValue(sample)
      setSampleValue(sample, value * 6 )
   play(sound)  

def Hell_Intro():
  file = "sounds/hellIntro.wav"
  sound = makeSound(file) 
  for sample in getSamples(sound):
     value = getSampleValue(sample)
     setSampleValue(sample, value )
  play(sound)
  
def Mummy_Norm():
  file = "sounds\Mummy.wav" 
  sound = makeSound(file)
  for sample in getSamples(sound):
     value  = getSampleValue(sample)
     setSampleValue(sample, value * 2 )
  play(sound)
  
def Mummy_low():
  file = "sounds/Mummy.wav" 
  sound = makeSound(file)
  for sample in getSamples(sound):
     value  = getSampleValue(sample)
     setSampleValue(sample, value *0.1 )
  play(sound)
  
def Monster():
  file = "sounds/Monster.wav"
  sound = makeSound(file)
  for sample in getSamples(sound):
     value  = getSampleValue(sample)
     setSampleValue(sample, value)
  play(sound)
  
  
  
  
printNow(os.path.dirname(os.path.realpath(__file__)) + "sounds/Creaking Door.wav" )
#welcome()
#room1()

