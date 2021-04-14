def rsp(a, b):
    if student[a] == 1 and student[b] == 2:
        return b
    elif student[a] == 1 and student[b] == 3:
        return a
    elif student[a] == 2 and student[b] == 1:
        return a
    elif student[a] == 2 and student[b] == 3:
        return b
    elif student[a] == 3 and student[b] == 1:
        return b
    elif student[a] == 3 and student[b] == 2:
        return a
    elif student[a] == student[b]:
        return a

def recur(start, end):
    if end-start==0:
        return end
    elif end-start==1:
        return rsp(start,end)
    return rsp(recur(start,(start+end)//2),recur((start+end)//2+1, end))

for tc in range(int(input())):
    N= int(input())
    student=list(map(int, input().split()))
    print('#{} {}'.format(tc+1, recur(0,N-1)+1))