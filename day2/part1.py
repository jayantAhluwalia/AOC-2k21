with open("./input/inputs.txt", "r") as file:
    directions = list(map(lambda x: (x[0], int(x[1])), map(str.split, file.read().split("\n"))))

results = dict()

for dir in directions:
    movements, value = dir
    if movements in results:
        results[movements] += value
    else:
        results[movements] = value


def solution(results):
    return results["forward"] * (results["down"] - results["up"])

print(solution(results))
