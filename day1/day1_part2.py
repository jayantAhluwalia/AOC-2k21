with open("./input/inputs.txt", "r") as file:
    measurements = [int(i.strip()) for i in file.readlines()]

#print(measurements)
# FUNCTION TO CHECK IF INCREASED
def if_increased(pair):
    return pair[1] > pair[0]

# FUNCTION TO GET PAIRS
def makePairs(measurements):
    return list(zip(measurements, measurements[3::1]))

def solution(measurements):
    return sum([if_increased(pair) for pair in makePairs(measurements)])

print(solution(measurements))
