f = open("input.txt", "r")

def getcalibrationvalue(digits):
	code = digits[0] + digits[-1]
	return int(code)

def getdigits(line):
	digits = ""
	current_string = ""
	string_digits = ['notzero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	for char in line:
		if char.isnumeric():
			digits += char
			current_string = ""
		else:
			current_string += char
			for index,word in enumerate(string_digits):
				if word in current_string:
					digits += str(index)
					current_string = current_string[-1]
	return digits

def linetovalue(line):
	digits = getdigits(line)
	cal_val = getcalibrationvalue(digits)
	return cal_val

calibration_values = []
for line in f:
	calibration_values.append(linetovalue(line))
print(sum(calibration_values))