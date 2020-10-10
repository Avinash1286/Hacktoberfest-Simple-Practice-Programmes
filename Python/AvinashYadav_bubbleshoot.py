numbers=[]
print('Enter five numbers :')
for i in range(5):
    val=int(input())
    numbers.append(val)

print('shorting the value...')

for i in range(5):
    for j in range(5):
        if numbers[i]<numbers[j]:
            temp=numbers[j]
            numbers[j]=numbers[i]
            numbers[i]=temp
            print(i,j,numbers)

print('sorted list',numbers)