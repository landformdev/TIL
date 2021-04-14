# input() 문자열이 입력 되더라
tmp = input()
print(tmp, type(tmp))

# 정수 하나를 입력 받자
N = int(input())

# 4 5 6
a, b, c = map(int, input().split())

arr = list(map(int, input().split()))

#가, 나, 다
tmp = input().split(',')
print(tmp)

#가나다라
tmp = input().split('') # 이게 아니고
tmp = list(input())

#1234231
tmp = list(map(int, input()))
