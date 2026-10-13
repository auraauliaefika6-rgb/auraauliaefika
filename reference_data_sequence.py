numbers1 = [1, 2, 3, 4] 
print("numbers1", id(numbers1), numbers1) 
# output ➜ numbers1 2269649131136 [1, 2, 3, 4] 

numbers2 = numbers1 
print("numbers1", id(numbers1), numbers1) 
# output ➜ numbers1 2269649131136 [1, 2, 3, 4] 

print("numbers2", id(numbers2), numbers2) 
# output ➜ numbers2 2269649131136 [1, 2, 3, 4]