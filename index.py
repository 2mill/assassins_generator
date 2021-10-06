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
	def __new__(self, name:str, dead=False, kills=0) -> object:
		self.name = name
		self.target = None
		self.dead = dead
		self.kills = kills
		return self

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
		return f"{self.name} -> {self.target.name}"
	def __next__(self) -> object:
		if self.target is None: return StopIteration
		return self.target
	def __str__(self) -> str:
		return f"{self.name} status: {self.dead} target: {self.target} score: {self.kills}"
	def __iter__(self) -> str:
		self.n = 0
		return self

class PlayerList:
	def __init__(self, names):
		self.first = self._player_chain(names)
	def _player_chain(self, names) -> Player:
		name = names.pop()
		print(names)
		if len(names) == 0:
			player = Player(name)
			print(f"last {player.name}")
			return player
		player = Player(name)
		print(player.name)
		# player.set_target(self._player_chain(names))
		temp = self._player_chain(names)
		print(f"{player.name} has {temp.name}")
		# print(f'{player.name} has {player.target.name}\n')
		return player
	def __iter__(self):
		self.n = 0
		return self.first

PlayerList(names)

	


	