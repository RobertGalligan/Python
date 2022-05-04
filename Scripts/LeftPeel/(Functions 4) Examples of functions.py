# Mean (average), median(middle), mode(most often), and range(difference between 
# the largest and smallest)

from logging import NullHandler
from random import sample


def mean(lst):
    return sum(lst) / len(lst)

def rnge(lst):
    lst.sort()  # This will sort the list from smallest to largest
    return lst[len(lst) - 1] - lst[0]
    print(lst)

def median(lst):
    lst.sort()
    print(len(lst) / 2)
    print(len(lst) / 2 - 1)
    if len(lst) % 2 == 0:
        return (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]) / 2
    else:
        return lst[int(len(lst) / 2)]

def mode(lst):
    mode_num = lst[0]
    mode_count_max = 1
    for num in lst:
        if lst.count(num) > mode_count_max:
            mode_num = num
            mode_count_max = lst.count(num)
    if mode_count_max == 1:
        return None
    else: 
        return mode_num

def data_analysis(lst):
    return mean(lst), median(lst), mode(lst), rnge(lst)
            


print("-----------------------------------------------------------------------")
sample_data = [5, 6, 0, 10, 9]
print("Mean: " + str(mean(sample_data))) # sample_data is the parameter inside the mean function now.
# The sample_data is the added and then divided by the length of the list to give you the mean.
# Mean: 6.0

print("-----------------------------------------------------------------------")

sample_data = [5, 6, 0, 10, 9, 100, 256] # if you change the data you will get a new Mean
print("Mean: " + str(mean(sample_data)))
# Mean: 55.142857142857146

print("-----------------------------------------------------------------------")

sample_data = [5, 6, 0, 10, 9]
rnge(sample_data)
# [0, 5, 6, 9, 10]
print("Range: " + str(rnge(sample_data)))
# Range: 10

print("-----------------------------------------------------------------------")

sample_data = [5, 6, 0, 10, 9, 4]   # So the median will take the 2 middle values and divide them by
# 2 to get the median
median(sample_data)
# 3.0
# 2.0
print("Median: " + str(median(sample_data)))
# Median: 5.5

sample_data = [5, 6, 0, 10, 9, 4, 10, 48]   # So the median will take the 2 middle values and divide them by
# 2 to get the median
median(sample_data)
# 4.0
# 3.0
print("Median: " + str(median(sample_data)))
# Median: 7.5

sample_data = [5, 6, 0, 10, 9,]   # So the median will take the 2 middle values and divide them by
# 2 to get the median
median(sample_data)
# 2.5
# 1.5
print("Median: " + str(median(sample_data)))
# Median: 6

print("-----------------------------------------------------------------------")

mode(sample_data)
# 0: 1
# 5: 1
# 6: 1
# 9: 1
# 10: 1

print("Mode: " + str(mean(sample_data))) 
# Mode: 6.0 

print("-----------------------------------------------------------------------")

sample_data = [5, 6, 0, 10, 9, 9, 9, 9, 10, 10, 10]
print(data_analysis(sample_data))