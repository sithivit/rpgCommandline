import cmd
from random import randint

class Item:
	def __init__(self):
		self.items = ["Sword", "Gun", "Armour", "Bow", "Arrow", "Ammo", "Shield"]
		self.store = {"Sword": 30, "Gun": 100, "Armour": 1000, "Bow": 50, "Arrow": 5, "Ammo": 2, "Shield": 20}

item = Item()

class Inventory:
	def __init__(self):
		self.items = item.items
		self.capacity = {}

	def add_item(self, item):
		if item in self.items:
			if item in self.capacity:
				self.capacity[item] = self.capacity[item] + 1 
			else:
				self.capacity[item] = 1
			print("Item: ", item, " has been added.")
		else:
			print("This item doesnt exist")

	def print_had_item(self):
		for key, value in self.capacity.items():
			print(key, value)
		print("Total items: ", sum(self.capacity.values()))

	def print_item(self):
		for element in self.items:
			print(element, end=" ")
		print()

class Character:
	def __init__(self):
		#recover of information will be implement later
		self.name = "Zoro"
		self.surname = "Roronoa"
		self.health = 100
		self.mana = 100
		self.money = 0
		self.level = 0

	def damage(self):
		damage = randint(5, 20)
		self.health = self.health - Damage
		return damage
	def mana(self):
		comsumption = randint(10,30)
		self.mana = self.mana - comsumption
		return consumption

	def working(self):
		gain = randint(30, 100)
		self.money = self.money + gain
		return gain

	def exercise(self):
		self.level = self.level + 1

character = Character()
item = Item()
inventory = Inventory()

class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, line):
        print('I do not understand that command. Type "help" for a list of commands.')

    # A very simple "quit" command to terminate the program:
    def do_quit(self, line):
        """Quit the game."""
        return True # this exits the Cmd application loop in TextAdventureCmd.cmdloop()

    def help_combat(self, line):
        print('Combat is not implemented in this program.')

    def do_introduce(self, line):
    	print("Hello my name is: ", character.surname,character.name)

    def do_working(self, line):
    	gain = character.working()
    	print("You gain: ", gain)

    def do_exercise(self, line):
    	xp = character.exercise()
    	print("You gain: 1 level")

    def do_buy(self, arg):
    	itemToAdd = arg
    	if itemToAdd in item.items:
    		if character.money >= item.store[itemToAdd]:
    			character.money = character.money - item.store[itemToAdd]
    			inventory.add_item(itemToAdd)
    		else:
    			print("You don't have enough money")
    	else:
    		print("We don't have this item")

    def do_inventory(self, line):
    	inventory.print_had_item()

    def do_item(self, line):
    	inventory.print_item()

    def do_money(self, line):
    	print("You have: ", character.money)

    def do_level(self, line):
    	print("Your level is: ", character.level)

if __name__ == '__main__':
    print('Text Adventure Demo!')
    print('====================')
    print()
    print('(Type "help" for commands.)')
    print()
    TextAdventureCmd().cmdloop()
    print('Thanks for playing!')
