n =187


factor =0
i =1
while i<=n:
    if n%i==0:
        factor+=1
    i +=1
print("prime"if factor==2 else "composite" )
print(factor)
print(i)






# n =187

# for i in range(2,n):
#     n%i==0
#     i+=1
# print(' not prime')
