def part1():
    A = list(map(int, input().split())) # 123
    j = 0
    for i in range(len(A)):
        j += 1
        print(j, ':', A[i])

    print('A: ', A)

part1()

def part2():
    A = list(map(int, input())) # 1, 2, 3
    j = 0
    print(A)

part2()
