def create_sorcerer(name, age, race, era): 
    return { 
        "name": name, 
        "age": age, 
        "race": race, 
        "era": era, 
        }
    
obj4 = create_sorcerer("400 year ago", 400, "human", "Hajime Kashimo") 
print(obj4) 
# output ➜ {'name': '400 year ago', 'age': 400, 'race': 'human', 'era': 'Hajime Kashimo'}

obj5 = create_sorcerer("Sukuna", 1000, "incarnation", "heian") 
print(obj5) 
# output ➜ {'name': 'Sukuna', 'age': 1000, 'race': 'incarnation', 'era': 'heian'} 

obj6 = create_sorcerer(name="Kenjaku", age=1000, race="human", era="1000+ year ago") 
print(obj6)

obj8 = create_sorcerer(era="1000+ year ago", age=1000, name="Kenjaku", race="human") 
print(obj8) 
# output ➜ {'name': 'Kenjaku', 'age': 1000, 'race': 'human', 'era': '1000+ year ago'}

obj9 = create_sorcerer("Hajime Kashimo", 400, era="400 year ago", race="human") 
print(obj9) 
# output ➜ {'name': 'Hajime Kashimo', 'age': 400, 'race': 'human', 'era': '400 year ago'}