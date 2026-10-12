data_str = "hello world" 
print(data_str[-1]) 
# output ➜ d 

print(data_str[-5]) 
# output ➜ w

data_str = "hello world" 
# slicing 3 karakter terakhir 
slice1 = data_str[-3:] 
print(slice1) 
# output ➜ rld 

# slicing dari index -5 hingga -2 
slice2 = data_str[-5:-2] 
print(slice2) 
# output ➜ wor 

# slicing dengan step negatif (reverse) 
slice3 = data_str[::-1] 
print(slice3) 
# output ➜ dlrow olleh