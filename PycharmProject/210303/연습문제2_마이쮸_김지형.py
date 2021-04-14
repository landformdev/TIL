my = 20

line = [(1, 0)]

new_person = 1
ans = 0

while my > 0:
    person, my_num = line.pop(0)

    ans = person
    my_num += 1
    my -= my_num

    new_person += 1

    line.append((person, my_num))
    line.append((new_person, 0))

print(ans)
