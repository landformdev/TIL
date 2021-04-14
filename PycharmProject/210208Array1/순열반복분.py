N = 3
card = [4, 5, 6]

#run?
#triplet?

run = False
tri = False

for i in range(N):
    for j in range(N):
        if i != j:
            for k in range(N):
                if k != i and k != j:
                    print(card[i], card[j], card[k])
                    
                    #run검사
                    if card[i] + 1 == card[j] and card[i] + 2 == card[k]:
                        run = True
                    #triplet검사
                    if card[i] == card[j] and card[i] == card[k]:
                        tri = True
                        
                    if run:
                        print("런")
                        
                    if tri:
                        print("트리플렛")
