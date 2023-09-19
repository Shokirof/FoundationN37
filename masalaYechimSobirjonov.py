"""#IELTS
s, w, l, r = map(float, input().split())

average_score = (s + w + l + r) / 4

fractional_part = average_score % 1

if 0.1 <= fractional_part < 0.25:
    ielts_score = int(average_score)
elif 0.25 <= fractional_part < 0.75:
    ielts_score = int(average_score) + 0.5
else:
    ielts_score = int(average_score) + 1

print(ielts_score)
"""

'''
#Robot
N = int(input())
moves = list(map(int, input().split()))

x, y = 0, 0
direction = "N"

directions = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}

def turn_clockwise(curr_direction):
    if curr_direction == "N":
        return "E"
    elif curr_direction == "E":
        return "S"
    elif curr_direction == "S":
        return "W"
    else:
        return "N"

for move in moves:
    dx, dy = directions[direction]
    
    x += move * dx
    y += move * dy
    
    direction = turn_clockwise(direction)

print(x, y)

'''