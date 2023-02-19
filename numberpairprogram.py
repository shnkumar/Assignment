# Handling string
InputStr = input("Enter a String : ")
splitstr = InputStr.split(",")
sumlist = []

length = len(splitstr)
print(" original string is :", InputStr)
print(" Split list is :", splitstr)
print(" Split list length is  :", length)


def findsum(listarg):
    flen = len(listarg)
    j = 0
    fsum = 0
    print("listarg :", listarg)
    print("flen : ", flen)

    while j < flen:
        # print (listarg[j])
        # print (" Value of J is ", j)

        fsum = fsum + int(listarg[j])
        j += 1

    # print ("lstarg is : ",listarg, " fsum is : ", fsum)
    return fsum


j = 0
while j < length:
    print(splitstr[j])
    # print (" Value of J is ", j)
    # print(findsum(splitstr[j]))
    sumlist.insert(j, findsum(splitstr[j]))
    j = j + 1

print("sumlist is ", sumlist)
sumlist.sort()
# print ("sorted list- sumlist is ",sumlist)


sortedlist = sumlist.copy()
print("sorted list is :", sortedlist, " length of sorted sorted list : ", len(sortedlist))

j = 0
z = 0
result = 0
for j in range(len(sortedlist) - 1):

    # print ("print value of j before the statement :", j, " z is ",z)
    if sortedlist[z] == sortedlist[z + 1]:
        result = result + 1
        print("compared the values :", sortedlist[z], " and ", sortedlist[z + 1], " result is :", result)
        z = z + 2
        # print ("  z when increamented by 2 :" , z)

    else:
        z = z + 1
    if z >= len(sortedlist):
        break

if result > 0:
    print(" No of equal pairs  is :", result)
else:
    print("-1")



