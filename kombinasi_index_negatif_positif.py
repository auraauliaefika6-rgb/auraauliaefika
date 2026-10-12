data_list = [2, 4, 6, 7, 9, 11, 13] 

# dari index 1 hingga 2 element terakhir 
list1 = data_list[1:-2] 
print(list1) 
# output ➜ [4, 6, 7, 9] 

# 3 element terakhir 
list2 = data_list[-3:] 
print(list2) 
# output ➜ [9, 11, 13] 

# seluruh element kecuali 2 terakhir 
list3 = data_list[:-2] 
print(list3) 
# output ➜ [2, 4, 6, 7, 9] 

# reverse list 
list4 = data_list[::-1] 
print(list4) 
# output ➜ [13, 11, 9, 7, 6, 4, 2]