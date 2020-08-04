# Extract id's from string in a text file
# Version 0.2
import re

lines = []
value = 'id: '
pattern = re.compile(value, re.IGNORECASE)          # Compile a case-insensitive regex

with open ('lorem.txt', 'rt') as my_file:           # Open file
    for line in my_file:
        if pattern.search(line) != None:            # If a match is found 
            parted = re.findall(value + '\d+', line)        # Find all value + number (to ignore other numbers) 
            for part in parted:
                lines.append(re.findall('\d+', part)[0])    # Find all numbers in substr and add to list

lines = list(dict.fromkeys(lines))                  # Remove duplicates
for number in lines:                                # Iterate over the list of tuples
    print(number)                                   # Select first number