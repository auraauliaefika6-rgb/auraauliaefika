fellowship = {'narya', 'nenya', 'nilya'} 

fellowship.pop() 
print("len:", len(fellowship), "data:", fellowship) 
# output ➜ len: 2 data: {'narya', 'nilya'} 

fellowship.pop() 
print("len:", len(fellowship), "data:", fellowship) 
# output ➜ len: 1 data: {'nilya'} 

fellowship.pop() 
print("len:", len(fellowship), "data:", fellowship) 
# output ➜ len: 0 data: set()