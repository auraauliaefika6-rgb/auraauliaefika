def create_sorcerer(name, age, race, era): 
    return { 
        "name": name, 
        "age": age, 
        "race": race, 
        "era": era, 
        }
    
obj1 = create_sorcerer("Sukuna", 1000, "incarnation", "heian") 
print(obj1) 
# output ➜ {'name': 'Sukuna', 'age': 1000, 'race': 'incarnation', 'era': 'heian'}

obj4 = create_sorcerer("400 year ago", 400, "human", "Hajime Kashimo") 
print(obj4) 
# output ➜ {'name': '400 year ago', 'age': 400, 'race': 'human', 'era': 'Hajime Kashimo'}

obj5 = create_sorcerer("Sukuna", 1000, "incarnation", "heian") 
print(obj5) 
# output ➜ {'name': 'Sukuna', 'age': 1000, 'race': 'incarnation', 'era': 'heian'} 

obj6 = create_sorcerer(name="Kenjaku", age=1000, race="human", era="1000+ year ago") 
print(obj6)