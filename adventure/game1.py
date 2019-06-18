#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game
========

Intructions: 
Get to the Living Room with a key and a pistol in your inventory!
Avoid the monsters!

Commands:
  go [direction]
  get [item]
  exit 
''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {
    'Hall' : { 
        'directions': {
            'south' : 'Kitchen',
            'east' : 'Dining Room',
            'north' : 'Bathroom'
        },
        'item' : 'key'
    },
    'Kitchen' : {
        'directions': {
            'north' : 'Hall',
            'east' : 'Garden'
        },
        'item' : 'monster'
    },
    'Dining Room' : {
        'directions': {
            'west' : 'Hall',
            'south' : 'Garden',
            'north' : 'Living Room'
        },
        'item' : 'pistol'
    },
    'Garden' : {
        'directions': {
            'west' : 'Kitchen',
            'north' : 'Dining Room'
        },
        'item' : 'monster'
    },
    'Bathroom' : {
        'directions': {
            'south' : 'Hall',
            'east' : 'Living Room'
        },
        'item' : 'armor'
    },
    'Living Room' : {
        'directions': {
            'west' : 'Bathroom',
            'south' : 'Dining Room'
        }
    }
}

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>')

    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]['directions']:
            #set the current room to the new room
            currentRoom = rooms[currentRoom]['directions'][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
            #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    #if they want to exit the game
    if move[0] == 'exit':
        break

    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
      print('A monster has got you... GAME OVER!')
      break
    
    #player wins if they get to the garden with a key and a pistol
    if currentRoom == 'Living Room' and 'key' in inventory and 'pistol' in inventory:
      print('You escaped the house...YOU WIN!')
      break
