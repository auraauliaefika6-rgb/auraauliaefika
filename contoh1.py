seq = [] 
for i in range(5): 
    seq.append(i * 2) 
    print(seq) 
    # output ➜ [0, 2, 4, 6, 8]

seq = [i * 2 for i in range(5)] 
print(seq) 
# output ➜ [0, 2, 4, 6, 8]