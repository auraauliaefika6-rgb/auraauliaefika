numbers1 = [1, 2, 3, 4] 
numbers2 = numbers1 
numbers3 = numbers1[:] 

print("numbers1", numbers1, id(numbers1)) # statement 1 
print("numbers2", numbers2, id(numbers2)) # statement 2 
print("numbers3", numbers3, id(numbers3)) # statement 3