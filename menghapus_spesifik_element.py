fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'} 
print("fellowship:", fellowship) 
# output ➜ fellowship: {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'} 

fellowship.discard('boromir') 
print("fellowship:", fellowship) 
# output ➜ fellowship: {'legolas', 'pippin', 'sam', 'aragorn', 'gimli', 'frodo', 'gandalf', 'merry'} 

fellowship.remove('gandalf') 
print("fellowship:", fellowship) 
# output ➜ fellowship: {'legolas', 'pippin', 'sam', 'aragorn', 'gimli', 'frodo', 'merry'}