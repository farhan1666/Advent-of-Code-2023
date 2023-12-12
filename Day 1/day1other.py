import re

numbers = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def convert(value):
  if value is not None:
    if value.isdigit():
      return int(value)
    if value in numbers:
      return int(numbers.index(value))


with open('input.txt') as f:
  
  lines = f.readlines()

  count = 0

  for line in lines:
    dictionary = {}

    # Get digit indexes
    for index, c in enumerate(line): 
      if c.isdigit():
        dictionary[index] = convert(c)

    # Get numbers in words indexes
    for number in numbers:
      matches = re.finditer(number, line)

      for match in matches:
        dictionary[match.span()[0]] = convert(number)

    # Get first and last dictionary items
    keys = sorted(dictionary.keys())
    count += (dictionary[keys[0]] * 10) + dictionary[keys[-1]]

  print(count)