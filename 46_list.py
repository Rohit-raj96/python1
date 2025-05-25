
list1 = [10,30,20,40,20,30]
list2=["ram","paul","william","smith"]
list3=["ram",21,56.5]
list4= []

# list1.sort()
# list1.reverse()
x=list1.copy()
print(x)

# print(list1.count(30))

# print(list1.index(20))
# list1.pop(3)
# list1.append(7,8)
# list1.extend([7,8,9])
# list1.remove(30)
# list1.clear()
# list1.insert(2,32)

# for i in list1:
#     print(i)

# print(list1[0:3:1])

# print(list1[2])
# print(list1[-2])

# print(list1,list2,list3,list4,sep="\n")




#-------------------------------------------
# write a program to find the fruits whisch starts with 'a' and ends with 'e' from the list of fruits
fruits=["apple","banana","grape","mango","orange","pineapple"]
for i in fruits:
    if i[0]=="a" and i[-1]=="e":
        print(i)