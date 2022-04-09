list_1= [3,7,6,5,3]
list_2 =list_1[0:-1]
# -1 means it will go all the to the last element but not the last element
print(list_1,list_2)
list_2 =list_1[:]
print(list_1,list_2)
list_2.append(33)
print(list_1,list_2)
list_2 = list_1
print(list_1,list_2)
list_2.append(27)  
#this will cause the 27 to be added to both list 1 and list 2 since list 2 equals list 1
print(list_1,list_2)
