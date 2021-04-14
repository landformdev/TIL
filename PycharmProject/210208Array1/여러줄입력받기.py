# 3 # 전체 테스트 케이스의 수
# 9 # 아래의 원소 수
# 7 4 2 0 0 6 0 7 0 # 원소들(리스트)
# 9
# 7 4 2 0 0 6 7 7 0
# 20
# 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for i in range(N):
    print(int(input()))
    print(list(map(int, input().split())))


