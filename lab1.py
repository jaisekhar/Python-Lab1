#Taking array length from the user
num = int(input("Enter Array Length: >>"))
print("Enter Values:")
list = []
sublist = []

#Taking input of num values
for i in range(0, num):
    ele = int(input())
    list.append(ele)

#looping all the numbers and sublisting by slicing
for i in range(num+1):
    for j in range(i + 1, num + 1):
        sub = list[i:j]
        sublist.append(sub)

print(sublist)
