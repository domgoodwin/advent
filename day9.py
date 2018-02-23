import re

f = open('inputs/day9.txt', 'r')
score = 0
garbage = 0
stack = 0

def remove_garbage(g):
    global garbage
    garbage += len(g.group())-2 # Don't count the opening '<' and '>'
    return ""

rawIn = f.read()

# remove cancel chars !.
rawIn = re.sub('!.', '', rawIn)
# remove garbage chars, non greedy
rawIn = re.sub('<[^>]*>', remove_garbage, rawIn)

for char in rawIn:
    if char == "{":
        stack+=1
    if char == "}" and stack > 0: # The stack condition is so we ignore '}' when there is no corresponding '{'
        score+=stack
        stack-=1
print(score)
print(garbage)

print(rawIn)

