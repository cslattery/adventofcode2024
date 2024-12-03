import re

with open('inputs/03/input.txt') as f:
    data = f.read().splitlines()

#pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)" # part a
pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)"
matches = [re.findall(pattern, line) for line in data]

print(matches)

# sum = 0                                       # part a
# for line in matches:
#     for exp in line:
#         nums = re.findall(r"\d+", exp)
#         sum += (int(nums[0]) * int(nums[1]))
# print(sum)

sum = 0
calculate = True
for line in matches:
    for exp in line:
        if exp == "do()":
            calculate = True
            continue
        elif exp == "don't()":
            calculate = False
            continue
        if calculate:
            nums = re.findall(r"\d+", exp)
            sum += (int(nums[0]) * int(nums[1]))
print(sum)