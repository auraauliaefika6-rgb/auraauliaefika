data_str = "hello world" 
print(data_str) 
# output ➜ hello world

data_str = "hello world" 
slice1 = data_str[0:3] 
print(slice1) 
# output ➜ hel

slice2 = data_str[2:8] 
print(slice2) 
# output ➜ llo wo

slice3 = data_str[:5] 
print(slice3) 
# output ➜ hello

slice4 = data_str[4:]
print(slice4)

slice5 = data_str[3:7:1] 
print(slice5) # output ➜ lo w

slice6 = data_str[2:9:2] 
print(slice6) 
# output ➜ lowr

slice7 = data_str[:] 
print(slice7) 
# output ➜ hello world

slice8 = data_str[::2] 
print(slice8) 
# output ➜ hlowrd