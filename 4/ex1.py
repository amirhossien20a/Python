import math

scores = [12, 18, 15, 20, 9, 17]

print(f"Count of scores are = {len(scores)}")

def MaxNumber():
    bigNum = 0
    for i in scores:
        for j in range(len(scores)):
            if i > scores[j] and i > bigNum:
                bigNum = i
    return f"Max Number is = {bigNum}"
                

print(MaxNumber())

def MinNumber():
    smallNum = float('inf')
    for i in scores:
        for j in range(len(scores)):
            if i < scores[j] and i < smallNum:
                smallNum = i
    return f"Min number is = {smallNum}"

print(MinNumber())

def avg():
    result = 0
    for i in scores:
        result += i
    return f"Avg is = {result / len(scores)}"

print(avg())

scores.append(20)

print(scores)

scores.remove(9)

print(scores)
