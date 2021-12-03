with open("./input/inputs.txt", "r") as file:
    directions = list(map(lambda x: (x[0], int(x[1])), map(str.split, file.read().split("\n"))))

horizontal, depth, aim = 0, 0, 0

for dir in directions:
    movement, value = dir
    if movement == "down":
        aim += value
    if movement == "up":
        aim -= value
    if movement == "forward":
        horizontal += value
        depth += value * aim
def solution(horizontal, depth):
    return horizontal * depth 

print(solution(horizontal, depth))
