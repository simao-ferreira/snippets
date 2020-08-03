import re

lines = []
value = 'nr:'
pattern = re.compile(value, re.IGNORECASE)          # Compile a case-insensitive regex

with open ('lorem.txt', 'rt') as my_file:           # Open file
    for line in my_file:
        if pattern.search(line) != None:            # If a match is found 
            res = line.split(value)[-1]             # Split the line by string
            lines.append(re.findall('\d+', res)[0]) # Find all numbers in substr and append the first

lines = list(dict.fromkeys(lines))                  # Remove duplicates
for number in lines:                                # Iterate over the list of tuples
    print(number)                                   # Select first number