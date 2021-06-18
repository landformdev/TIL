# eydbkmiqugjxlvtzpnwohracsf
# Kifq oua zarxa suar bti yaagrj fa xtfgrj

key = input()
string = input()
answer = ''

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in string:
    if i == ' ':
        answer += i
    else:
        j = alpha.index(i.lower())
        answer += key[j]
print(answer)