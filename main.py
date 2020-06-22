import pprint 
message = 'It was a cold fck day '
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)