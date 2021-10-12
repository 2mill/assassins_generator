#!usr/bin/python
import argparse, sys, random, os 
from datetime import date


parser = argparse.ArgumentParser(prog="py_ass", description="Can take a names list and generate a new list for an assassins game.", usage="py_ass -f [file]")

parser.add_argument('-f', '--file', type=str, required=True, help="Names list text file.")
parser.add_argument('-l', '--letter', action="store_true", required=False, help="Generate player letters.")
parser.add_argument('--rules', type=str, required=False, help="If custom rules have been written, they can be applied to the player letter at the end of the letter.")
args = parser.parse_args()

def file_to_list(file_name: str) -> list :
	with open(f"./{file_name}") as f:
		names = []
		for name in f:
			names.append(name.strip())
		return names

names = file_to_list(args.file)
random.shuffle(names)
			
class Player:
	def __init__(self, name:str, dead=False, kills=0) -> object:
		self.name = name
		self.target = None
		self.dead = dead
		self.kills = kills

	# I don't understand python, so just leave this please for god's sake.
	def get_player(self) -> object: return self

	def kill(self) -> object:
		self.dead = True
		return self.target
	def score(self) -> int:
		self.kills = self.kills + 1
		return self.kills
	def set_target(self, target:object) -> None:
		self.target = target
	def __str__(self) -> str:
		return f"{self.name} status: {'dead' if self.dead else 'alive'} target: {self.target.name} score: {self.kills}"
	def str_human(self) -> str:
		double_space = "  "
		return f"{self.name}\n{double_space}status:{'dead' if self.dead else 'alive'}\n{double_space}target:{self.target.name}\n{double_space}score:{self.kills}"

class PlayerList:
	def __init__(self, names):
		self._generate_players(names)
		self.player_list = self._assign_targets(self._generate_players(names))

	def _generate_players(self, names) -> list: 
		player_list = []
		for i in range(len(names)):
			name = names[i]
			player_list.append(Player(name))

		return player_list
	def _assign_targets(self, player_list:list) -> list:
		random.shuffle(player_list)
		for i in range(len(player_list)):
			if i == len(player_list) - 1:
				player_list[i].target = player_list[0]
			else:
				player_list[i].target = player_list[i + 1]
		return player_list
	def str_type(self, version) -> str:
		collection = ""
		for player in self.player_list:
			if version == "human":
				collection = f"{collection}{player.str_human()}\n"
			else:
				collection = f"{collection}{player}\n"
		return collection
	def str_human(self):
		return self.str_type("human")
	def __str__(self):
		return self.str_type()
	def __iter__(self):
		return self.player_list.__iter__()




player_list = PlayerList(names)
with open(f"assassin_game-{date.today()}.txt", "w") as f:
	f.write(player_list.str_human())
	f.close()

# Generate letters here.

if args.letter:
	letter = []
	rules_file = args.rules 
	rules = [] if rules_file is None else open(f"./{rules_file}", 'r').readlines()
	directory_path = f"./letters-{date.today()}"
	if not os.path.exists(directory_path):
		os.mkdir(directory_path)
	for player in player_list:
		with open(f"{directory_path}/{player.name}-letter.txt", 'w') as f:
			f.write(f"Hello {player.name},\n")
			f.write(f"Your target is: {player.target.name}\n\n")
			f.write("===RULES===\n")
			for line in rules: f.write(line)
			f.write("Good Luck!")
			f.close()

		


