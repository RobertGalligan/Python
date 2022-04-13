num_list = [4,2,5,1]
new_list = []
for i in range (len(num_list)):     #(len(num_list)) makes its 1, 2, 3, 4 because the normal list is 0,1,2,3
    j = 0
    product = 1
    while (j < i):
        product *= num_list[j]
        j += 1
    j += 1
    while (j < len(num_list)):
        product *= num_list[j]
        j += 1
    new_list.append(product)
print (new_list)