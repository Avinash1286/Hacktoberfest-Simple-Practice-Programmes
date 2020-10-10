print('Enter a number:')
n=input()
sum=0
for i in range(len(n)):
    sum=sum+int(n[i])

print('Sum of the digits : '+str(sum))