str1 = 'Indonesia' 
str2 = "Indonesia" 

print(f"id str1: {id(str1)}, id str2: {id(str2)}") 
# output ➜ id str1: 133983722110320, id str2: 133983722110320 

print(f"str1 == str2: {str1 == str2}") 
# output ➜ str1 == str2: True 

print(f"str1 is str2: {str1 is str2}") 
# output ➜ str1 is str2: True
