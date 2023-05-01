n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for i in coin_types:
    count += n // i # 각 동전의 개수를 더함
    n %= i # 각 동전을 차례대로 빼고 남은 돈

print(count)