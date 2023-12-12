f = open("input.txt", "r")

powers = []
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
	bluemax = 1
	redmax = 1
	greenmax = 1
	for i in gamestatsfinal:
		if i[1] == 'blue':
			if int(i[0]) > bluemax:
				bluemax = int(i[0])
		elif i[1] == 'red':
			if int(i[0]) > redmax:
				redmax = int(i[0])
		elif i[1] == 'green':
			if int(i[0]) > greenmax:
				greenmax = int(i[0])
	power = bluemax * redmax * greenmax
	powers.append(power)

print(sum(powers))