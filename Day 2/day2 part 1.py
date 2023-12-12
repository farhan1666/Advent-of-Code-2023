f = open("input.txt", "r")

possibles = []

for i in f:
	#split by colon
	#split by semicolons
	#split by commas
	#split by space
	#store
	line = i.rstrip("\n")
	game, stats = line.split(":")
	id = game.lstrip("Game ")
	full_game = {}
	games = stats.split(";")
	gamestats = []
	for i in games:
		gamestats.append(i.split(","))
	gamestatsfinal = []
	for i in gamestats:
		for j in i:
			gamestatsfinal.append(j.lstrip(" ").split(" "))
	for i in gamestatsfinal:
		possible = True
		if i[1] == 'blue':
			if int(i[0]) > 14:
				possible = False
				break
		elif i[1] == 'red':
			if int(i[0]) > 12:
				possible = False
				break
		elif i[1] == 'green':
			if int(i[0]) > 13:
				possible = False
				break
	possibles.append(possible)

possible_ids = [0]

for i,j in enumerate(possibles):
	if j:
		possible_ids.append(i+1)
print(sum(possible_ids))