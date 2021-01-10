count = 0
sum = 0
print('before iteratinb' , count ,sum)
for i in range(1,20):
    count += 1
    sum = sum + i
    print(count, sum, i)
print("after", count, sum , sum/ count)

