# my answer
n, k = map(int, input().split())

a = list(map(int, input().split())) # a 배열의 합이 최대가 되어야 한다
b = list(map(int, input().split()))

# a를 내림차순 정렬
a.sort()
# b를 오름차순 정렬
b.sort(reverse=True)
# 동일한 index끼리 k번 교환
for i in range(k):
    a[i], b[i] = b[i], a[i]

print(sum(a))
#
# 
#---------------------------------------------------------------------------- 
# 
# book answer
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
