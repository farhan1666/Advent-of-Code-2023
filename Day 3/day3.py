#Code used to check what symbols are in input, does not need to be run each time
	# set_characters = set()
	# for line in f:
	# 	line.rstrip('\n')
	# 	for i in line:
	# 		set_characters.add(i)
	# for i in set_characters:
	# 	if not i.isnumeric():
	# 		symbols.append(i)
	# symbols.remove("\n")
	# symbols.remove(".")
	# print(symbols)


f = open("input.txt", "r").read().split('\n')

#Plan
	#function to find digit adjacent to symbol and return coords of digit
	#function to take coords of digit and find the full number
		#check left
			#if left is digit, add to start of string
			#if left is not digit, check coord, if coord exists, then discard, else record it, halt
		#check right
			#if right is digit, add to end of string
			#if right is not digit, halt
		#add digit to part numbers list
	#get sum


symbols = ['-', '/', '$', '@', '=', '*', '&', '%', '+', '#']

def get_adjacent_symbols(x, y):
	coords = []
	coords.append((x-1,y-1))
	coords.append((x,y-1))
	coords.append((x+1,y-1))
	coords.append((x-1,y))
	coords.append((x+1,y))
	coords.append((x-1,y+1))
	coords.append((x,y+1))
	coords.append((x+1,y+1))
	return coords
	#Visualisation
		#   x	0		1		2
		
		# y

		# 0		x-1,y-1	x,y-1	x+1,y-1

		# 1		x-1,y	x,y		x+1,y

		# 2		x-1,y+1	x,y+1	x+1,y+1

def get_digit_coords():
	coords = []
	for x,j in enumerate(f):
		for y,q in enumerate(j):
			if q in symbols:
				for i in get_adjacent_symbols(x,y):
					if f[i[0]][i[1]].isnumeric():
						coords.append(i)
	return coords

def get_gear_coords():
	coords = []
	num_coords = []
	for x,j in enumerate(f):
		for y,q in enumerate(j):
			if q == '*':
				temp = []
				for i in get_adjacent_symbols(x,y):
					if f[i[0]][i[1]].isnumeric():
						num_to_add = get_num_from_coords(*i)
						if num_to_add:
							temp.append(num_to_add)
				if len(temp) == 2:
					num_coords.append(temp)
	return num_coords

checked = set()

def get_num_from_coords(x,y):
	num = f[x][y]
	lpoint = y-1
	rpoint = y+1
	if not f[x][lpoint].isnumeric():
		checked.add((x,y))
	try:
		while f[x][rpoint].isnumeric():
			num = num + f[x][rpoint]
			rpoint += 1
	except IndexError:
		pass
	while f[x][lpoint].isnumeric():
		if (x, lpoint) in checked:
			return None
		num = f[x][lpoint] + num
		lpoint -= 1
	else:	
		checked.add((x, lpoint+1))
	return num
nums = []


# for i in get_digit_coords():
# 	num_to_add = get_num_from_coords(*i)
# 	if num_to_add:
# 		nums.append(int(num_to_add))

sum = 0

for i in get_gear_coords():
	sum += int(i[0])*int(i[1])

print(sum)
