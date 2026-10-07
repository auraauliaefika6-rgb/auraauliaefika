profile = { 
    "name": "mario", 
    } 
print("len:", len(profile), "data:", profile) 
# output ➜ len: 1 data: {'name': 'mario'} 


profile["favourite_color"] = "red" 
print("len:", len(profile), "data:", profile) 
# output ➜ len: 2 data: {'name': 'mario', 'favourite_color': 'red'}

profile.update({"race": "italian"}) 
print("len:", len(profile), "data:", profile) 
# output ➜ len: 3 data: {'name': 'mario', 'favourite_color': 'red', 'race': 'italian'}