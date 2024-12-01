a = []
b = []


with open('01/inputs/20241201a.txt') as f:
    for line in f:
        a.append(int(line.split('   ')[0]))
        b.append(int(line.split('   ')[1]))

print(a)
print(b)

a.sort()
b.sort()
dist = 0
for i in range(len(a)):
    dist += abs(a[i] - b[i])

print(dist)

element_count = {}
for i in range(len(b)):
    if b[i] in element_count:
        element_count[b[i]] += 1
    else:
        element_count[b[i]] = 1

similarity_count = 0
for j in range(len(a)):
    if a[j] in element_count:
        similarity_count += a[j] * element_count[a[j]]

print(similarity_count)