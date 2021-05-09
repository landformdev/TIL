def solution(n, k, cmd):
    answer = "O" * n

    arr = [0] * n
    arr2 = [0] * n
    arr2[k] = 'x'
    cnt = 0
    for call in cmd:
        print(arr)
        print(arr2)

        if call[0] == 'U':
            check = arr2.index('x')
            arr2[check] = 0
            for up in range(int(call[2])):
                check -= 1
                if arr[check] != 0:
                    check -= 1
            arr2[check] = 'x'

        elif call[0] == 'D':
            check = arr2.index('x')
            arr2[check] = 0
            for up in range(int(call[2])):
                check += 1
                if arr[check] != 0:
                    check += 1
            arr2[check] = 'x'

        elif call[0] == 'C':
            cnt += 1

            check = arr2.index('x')
            arr2[check] = 0
            last = len(arr) - 1
            while arr[last] != 0:
                last -= 1

            arr[check] = cnt

            if check == last:
                check -= 1
                if arr[check] != 0:
                    check -= 1
                arr2[check] = 'x'

            else:
                check += 1
                if arr[check] != 0:
                    check += 1
                arr2[check] = 'x'

        elif call[0] == 'Z':
            arr[arr.index(cnt)] = 0
            cnt -= 1

    print(arr)
    print(arr2)
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))

# OOXOXOOO
