res = ""
rows = int(input('How many rows is the tree? '))
for f in range(rows) :
    res += " "
res += "*\n"
count = rows-1
stars = 3
for i in range(rows) :
    for n in range(count) :
        res += " "
    count -= 1
    for f in range(stars) :
        res += "*"
    stars += 2
    res += "\n"
print(res)

input('press a key to exit')