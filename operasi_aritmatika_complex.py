cmp1 = 120-2j 
cmp2 =-19+4j 

res = cmp1 + cmp2 
print(f"angka complex: {res}") 
# output ➜ angka complex: (101+2j) 

res = cmp1 + cmp2 + 23 
print(f"angka complex: {res}") 
# output ➜ angka complex: (124+2j) 

res = (cmp1 + cmp2 + 23) / 0.5 
print(f"angka complex: {res}")