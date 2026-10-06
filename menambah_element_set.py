fellowship = set() 

fellowship.add('aragorn') 
print("len:", len(fellowship), "data:", fellowship) 
# output ➜ len: 1 data: {'aragorn'} 

fellowship.add('gimli') 
print("len:", len(fellowship), "data:", fellowship) 
# output ➜ len: 2 data: {'gimli', 'aragorn'} 

fellowship.add('legolas') 
print("len:", len(fellowship), "data:", fellowship) 
# output ➜ len: 3 data: {'gimli', 'legolas', 'aragorn'}