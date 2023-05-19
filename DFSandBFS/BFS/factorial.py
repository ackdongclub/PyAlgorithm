# 팩토리얼 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i #팩토리얼 함수로 n부터 1까지를 곱한다
       # print(result)
    return result

def factorial_recursive(n):
    if n <= 1: 
        return 1 # n이 1보다 작거나 같으면 1을 반환
    return n * factorial_recursive(n-1) # n - 1을 반복하며 n이 1이 되면 1을 반환해서 멈춤
print('반복적으로 구현: ', factorial_iterative(5))
print('반복적으로 구현: ', factorial_recursive(5))