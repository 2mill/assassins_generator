import argparse, sys, random

parser = argparse.ArgumentParser(prog="py_ass", description="Can take a names list and generate a new list for an assassins game.", usage="py_ass -f [file]")

parser.add_argument('-f', '--file', type=str, required=True, help="Names list text file.")

args = parser.parse_args()

def file_to_list(file_name: str) -> list :
	with open(f"./{file_name}") as f:
		names = []
		for name in f:
			names.append(name.strip())
		return names

names = file_to_list(args.file)
random.shuffle(names)
print(names)
			
class Player:
	def __init__(self, name:str, target: object, dead=False, kills=0):
		self.name = name
		self.target = target
		self.dead = dead
		self.kills = kills
	def kill(self) -> object:
		self.dead = True
		return self.target
	def score(self) -> int:
		self.kills = self.kills + 1
		return self.kills
	def set_target(self, target:object) -> object:
		self.target = target
		return self.target
	def __str__(self) -> str:
		return f"{self.name} -> {self.target.name}"


def generate_persons(names: list) -> Player:
	first_player:Player = Player(names.pop(), target=None)
	previous_player: Player = first_player
	while len(names) > 0:
		previous_player = previous_player.set_target(names.pop(), target=None)
	return previous_player.set_target(first_player)
print(generate_persons(names))