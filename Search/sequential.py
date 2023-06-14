def sequential_search(n, target, array):
    for i in range(n): # 순차적으로 데이터 확인
        if array[i] == target:
            return i + 1 # 데이터와 타겟 데이터가 동일하면 +1을 리턴 (배열은 0부터 시작하니까)
print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.')
input_data = input().split()
n = int(input_data[0]) # 원소 개수
target = input_data[1] # 타겟 데이터

print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.')
array = input().split()

print(sequential_search(n, target, array))