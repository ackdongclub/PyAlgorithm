# my answer  
n = int(input())
array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
def setting(data):
    return data[1]

result = sorted(array, key=setting)

for i in result:
    print(i[0], end=' ')
#
#
#---------------------------------------------------------------------------------------------------------------------
#
#
# book answer
n = int(input()) # N값 받기

array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]))) # (string int) 형태로 배열에 값을 입력 받음

array = sorted(array, key=lambda name : name[1]) # lambda를 사용해 name라는 매개뱐수를 생성해 name[1] <- 점수를 기준으로 정렬을 한다
# key는 정렬기준

for i in array:
    print(i[0], end=' ')

